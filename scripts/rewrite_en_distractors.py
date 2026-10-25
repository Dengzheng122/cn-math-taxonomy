# -*- coding: utf-8 -*-
"""把英语题里明显不通的干扰项改成同一形式的典型错误。只改错误选项文字。"""
from __future__ import annotations

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH = os.path.join(ROOT, "data", "questions.json")

PERSON_BE = [
    (re.compile(r"\bI am\b"), "I is"),
    (re.compile(r"\bI was\b"), "I were"),
    (re.compile(r"\bHe is\b"), "He are"),
    (re.compile(r"\bShe is\b"), "She are"),
    (re.compile(r"\bIt is\b"), "It are"),
    (re.compile(r"\bThis is\b"), "This are"),
    (re.compile(r"\bThat is\b"), "That are"),
    (re.compile(r"\bThey are\b"), "They is"),
    (re.compile(r"\bWe are\b"), "We is"),
    (re.compile(r"\bYou are\b"), "You is"),
    (re.compile(r"\bThese are\b"), "These is"),
    (re.compile(r"\bThose are\b"), "Those is"),
    (re.compile(r"\bThey were\b"), "They was"),
    (re.compile(r"\bWe were\b"), "We was"),
    (re.compile(r"\bHe was\b"), "He were"),
    (re.compile(r"\bShe was\b"), "She were"),
]

# 星期、时段的介词搭配，改了一定错
PREP_SWAPS = [
    (re.compile(r"\bon (Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b"), r"in \1"),
    (re.compile(r"\bin the (morning|afternoon|evening)\b"), r"on the \1"),
    (re.compile(r"\bat night\b"), "in night"),
    (re.compile(r"\bin Class\b"), "at Class"),
    (re.compile(r"\bgood at\b", re.I), "good in"),
    (re.compile(r"\bdepend on\b"), "depend of"),
    (re.compile(r"\blisten to\b"), "listen at"),
    (re.compile(r"\barrive in\b"), "arrive to"),
    (re.compile(r"\barrive at\b"), "arrive to"),
    (re.compile(r"\binterested in\b"), "interested on"),
    (re.compile(r"\blook forward to\b"), "look forward for"),
    (re.compile(r"\bmarried to\b"), "married with"),
    (re.compile(r"\bdifferent from\b"), "different of"),
    (re.compile(r"\bwait for\b"), "wait to"),
    (re.compile(r"\bsorry for\b"), "sorry of"),
    (re.compile(r"\bfull of\b"), "full with"),
    (re.compile(r"\bafraid of\b"), "afraid to"),
    (re.compile(r"\bproud of\b"), "proud on"),
    (re.compile(r"\binstead of\b"), "instead than"),
    (re.compile(r"\bbecause of\b"), "because with"),
]

WEEKDAY = {
    "Monday": "Friday",
    "Tuesday": "Sunday",
    "Wednesday": "Monday",
    "Thursday": "Saturday",
    "Friday": "Monday",
    "Saturday": "Wednesday",
    "Sunday": "Thursday",
}

MODAL = r"\b(can|could|shall|should|will|would|may|might|must)\b"

# 集合名词：The band is / The band are 都可能被接受，不用来做干扰项
COLLECTIVE = {
    "band", "team", "family", "class", "group", "audience", "staff", "police",
    "crowd", "government", "public", "committee", "crew", "company", "army",
}


def norm(text):
    s = str(text).strip().lower()
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"[.!\s]+$", "", s)
    return s


def split_punct(text):
    s = text.strip()
    m = re.match(r"^(.*?)([.?!])$", s)
    if m and m.group(1).strip():
        return m.group(1), m.group(2)
    return s, ""


def join_punct(body, punct):
    body = re.sub(r"\s+", " ", body).strip()
    body = re.sub(r"\s+([,;:])", r"\1", body)
    return body + punct


def sub_once(pattern, repl, text):
    if isinstance(pattern, str):
        pattern = re.compile(pattern)
    m = pattern.search(text)
    if not m:
        return None
    return pattern.sub(repl, text, count=1)


def be_agreement(body):
    for pat, repl in PERSON_BE:
        got = sub_once(pat, repl, body)
        if got and got != body:
            return got
    # 普通单数主语 + is → are；复数 + are → is。避开 there is / there are 的可接受换法以外，there is + 复数才算错，这里只做明显的。
    # band/team 等集合名词在英式英语里可以接复数，is→are 不算稳定的错项
    m = re.search(r"\bThe\s+([a-z]+)\s+is\b", body)
    if m and not m.group(1).endswith("s") and m.group(1).lower() not in COLLECTIVE:
        return body[: m.start()] + "The " + m.group(1) + " are" + body[m.end() :]
    m = re.search(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+)?)\s+is\b", body)
    if m and m.group(1) not in ("He", "She", "It", "This", "That", "There", "What", "Who", "Where", "How", "The"):
        return body[: m.start()] + m.group(1) + " are" + body[m.end() :]
    m = re.search(r"\b([A-Z][a-z]+s)\s+are\b", body)
    if m:
        return body[: m.start()] + m.group(1) + " is" + body[m.end() :]
    if re.search(r"\bname is\b", body):
        return sub_once(r"\bname is\b", "name are", body)
    if re.search(r"\bpeople are\b", body):
        return sub_once(r"\bpeople are\b", "people is", body)
    if re.search(r"\bpeople need\b", body):
        return sub_once(r"\bpeople need\b", "people needs", body)
    return None


def verb_form(body):
    # 情态动词后面用了过去式或 -ing
    m = re.search(MODAL + r"\s+([a-z]+)\b", body)
    if m and m.group(2) not in ("not", "be", "to"):
        verb = m.group(2)
        if verb.endswith("ing") and len(verb) > 4:
            wrong = ing_to_base(verb)
            if wrong == verb:
                wrong = verb + "ed"
        elif verb.endswith("ed") or verb in ("went", "ran", "won", "left", "made", "had", "did", "was", "were"):
            wrong = {"went": "go", "ran": "run", "won": "win", "left": "leave", "made": "make",
                     "had": "have", "did": "do", "was": "be", "were": "be"}.get(verb, verb[:-2] if verb.endswith("ed") else verb + "ing")
        else:
            if verb == "control":
                wrong = "controlled"
            elif verb.endswith("e"):
                wrong = verb + "d"
            elif verb.endswith("y") and len(verb) > 2 and verb[-2] not in "aeiou":
                wrong = verb[:-1] + "ied"
            else:
                wrong = verb + "ed"
        if wrong and wrong != verb:
            return body[: m.start(2)] + wrong + body[m.end(2) :]
    # am/is/are/was/were + V-ing → 动词原形
    m = re.search(r"\b(am|is|are|was|were)\s+(not\s+)?([a-z]+ing)\b", body)
    if m and m.group(3) != "being":
        base = ing_to_base(m.group(3))
        if base and base != m.group(3):
            return body[: m.start(3)] + base + body[m.end(3) :]
    # have/has/had + 过去分词 → 原形（常见规则变化）
    m = re.search(r"\b(have|has|had)\s+(not\s+|already\s+|just\s+|never\s+)?([a-z]+ed)\b", body)
    if m:
        pp = m.group(3)
        base = pp[:-1] if pp.endswith("ed") and pp[:-2].endswith("e") else pp[:-2]
        irregular = {"been": "be", "done": "do", "gone": "go", "written": "write", "made": "make"}
        base = irregular.get(pp, base)
        if base and base != pp and len(base) >= 2:
            return body[: m.start(3)] + base + body[m.end(3) :]
    # Let's + 原形 → Let's to
    m = re.search(r"\bLet's\s+([a-z]+)\b", body)
    if m and m.group(1) not in ("to",):
        return body[: m.start(1)] + "to " + m.group(1) + body[m.end(1) :]
    # would like / want / need to → 丢掉 to
    got = sub_once(r"\b(would like|want|needs|need|like)\s+to\s+", r"\1 ", body)
    if got:
        return got
    # 第三人称少 -s
    m = re.search(r"\b(He|She|It|This|That|Everyone|Somebody|Nobody)\s+([a-z]+s)\b", body)
    if m and m.group(2) not in ("is", "was", "has", "does", "this") and m.group(2).endswith("s") and not m.group(2).endswith("ss"):
        return body[: m.start(2)] + m.group(2)[:-1] + body[m.end(2) :]
    m = re.search(r"\b([A-Z][a-z]+ing|[A-Z][a-z]+)\s+(helps|makes|means|comes|gives|takes|likes|wants|needs|goes|does|sounds|keeps|seems)\b", body)
    if m:
        return body[: m.start(2)] + m.group(2)[:-1] + body[m.end(2) :]
    # 单数名词 + 第三人称 -s，漏掉 -s：diet helps → diet help
    m = re.search(
        r"\b([A-Za-z]+)\s+(helps|makes|means|comes|gives|takes|likes|wants|needs|goes|does|sounds|keeps|seems|shows|starts|looks|carries|follows|describes|records|points|supports|introduces)\b",
        body,
    )
    if m and m.group(1).lower() not in {"i", "you", "we", "they", "people"} and not m.group(1).endswith("s"):
        return body[: m.start(2)] + m.group(2)[:-1] + body[m.end(2) :]
    # I/You/We/They + 动词原形 → 误加 -s
    m = re.search(r"\b(I|You|We|They)\s+(like|want|need|go|have|do|play|read|know|think|help|make)\b", body)
    if m:
        return body[: m.start(2)] + m.group(2) + "s" + body[m.end(2) :]
    return None


def prep_error(body):
    for pat, repl in PREP_SWAPS:
        got = sub_once(pat, repl, body)
        if got and got != body:
            return got
    return None


def article_error(body):
    m = re.search(r"\ba\s+([aeiou][a-z]+)\b", body, re.I)
    if m and m.group(1).lower() not in ("university", "unit", "european", "one", "used"):
        art = "an" if m.group(0)[0].islower() else "An"
        # 保持 a/A 的大小写位置
        if m.group(0)[0] == "A":
            art = "An"
        else:
            art = "an"
        return body[: m.start()] + art + " " + m.group(1) + body[m.end() :]
    m = re.search(r"\ban\s+([^aeiou\s][a-z]+)\b", body, re.I)
    if m and m.group(1).lower() not in ("hour", "honest", "honour", "honor"):
        art = "A" if m.group(0)[0] == "A" else "a"
        return body[: m.start()] + art + " " + m.group(1) + body[m.end() :]
    m = re.search(r"\ba\s+([b-df-hj-np-tv-z][a-z]+)\b", body)
    if m:
        return body[: m.start()] + "an " + m.group(1) + body[m.end() :]
    return None


def plural_error(body):
    m = re.search(r"\b([2-9]|[1-9]\d+)\s+([a-z]+s)\b", body)
    if m and m.group(2).endswith("s") and not m.group(2).endswith("ss"):
        return body[: m.start(2)] + m.group(2)[:-1] + body[m.end(2) :]
    if re.search(r"\bmany people\b", body):
        return sub_once(r"\bmany people\b", "many peoples", body)
    if re.search(r"\binformations\b", body) is None and re.search(r"\binformation\b", body):
        return sub_once(r"\binformation\b", "informations", body)
    if re.search(r"\badvice\b", body) and not re.search(r"\badvices\b", body):
        return sub_once(r"\badvice\b", "advices", body)
    return None


TO_VERBS = {
    "meet", "join", "tell", "check", "write", "go", "see", "learn", "protect", "say",
    "run", "walk", "help", "make", "take", "give", "come", "look", "keep", "speak",
    "read", "study", "play", "visit", "buy", "try", "use", "do", "leave", "stay",
    "book", "rest", "train", "apply", "improve", "reduce", "ask", "call", "find",
    "get", "put", "turn", "open", "close", "show", "move", "live", "work", "start",
    "stop", "feel", "know", "think", "want", "need", "like", "love", "have", "be",
}


# -ing 前丢掉的 e（leave → leaving）。只收双元音后面还要补 e 的词，其余双元音词干保持原样。
_E_AFTER_DIGRAPH = {
    "leav": "leave",
    "pleas": "please",
    "breath": "breathe",
    "choos": "choose",
    "rais": "raise",
    "teas": "tease",
    "freez": "freeze",
    "believ": "believe",
    "receiv": "receive",
    "achiev": "achieve",
    "arriv": "arrive",
    "creat": "create",
    "increas": "increase",
    "decreas": "decrease",
    "los": "lose",
    "us": "use",
    "dy": "die",
    "ly": "lie",
    "ty": "tie",
}


def ing_to_base(ing):
    """把 V-ing 收成原形。bleeding→bleed，writing→write，running→run。不要造出 bleede。"""
    stem = ing[:-3]
    if not stem:
        return ing
    if stem in _E_AFTER_DIGRAPH:
        return _E_AFTER_DIGRAPH[stem]
    # running → run；seeing 的 ee 不是双写辅音
    if len(stem) >= 2 and stem[-1] == stem[-2] and stem[-1] not in "aeiou":
        return stem[:-1]
    if stem.endswith(("e", "y")) or stem.endswith(("ee", "o", "w")) or len(stem) < 3:
        return _E_AFTER_DIGRAPH.get(stem, stem)
    # bleed/read/eat/speak：词干已是「双元音 + 辅音」，直接用，不再加 e
    if len(stem) >= 3 and stem[-3] in "aeiou" and stem[-2] in "aeiou" and stem[-1] not in "aeiou":
        return stem
    # write→writ, make→mak, come→com
    if stem[-1] not in "aeiou" and stem[-2] in "aeiou":
        return stem + "e"
    return stem


def infinitive_s(body):
    """to meet → to meets：不定式后面误加 -s。"""
    m = re.search(r"\bto\s+([a-z]+)\b", body)
    if not m or m.group(1) not in TO_VERBS or m.group(1).endswith("s"):
        return None
    return body[: m.end(1)] + "s" + body[m.end(1) :]


def to_ing(body):
    m = re.search(r"\bto\s+([a-z]{2,})\b", body)
    if not m or m.group(1) not in TO_VERBS:
        return None
    verb = m.group(1)
    if verb.endswith("ie"):
        ing = verb[:-2] + "ying"
    elif verb.endswith("e") and not verb.endswith("ee"):
        ing = verb[:-1] + "ing"
    else:
        ing = verb + "ing"
    return body[: m.start(1)] + ing + body[m.end(1) :]


def swap_last_two(body):
    words = body.split()
    if len(words) >= 3:
        words[-2], words[-1] = words[-1], words[-2]
        got = " ".join(words)
        return got if got != body else None
    if len(words) == 2 and re.fullmatch(r"[A-Za-z]+", words[0]) and re.fullmatch(r"[A-Za-z]+", words[1]):
        if words[0].lower() == "good" and not words[1].endswith("s"):
            return words[0] + " " + words[1] + "s"
        return words[1] + " " + words[0].lower()
    return None


# 对调字母时碰巧变成的真词，不能拿来当“拼写错误”
SPELL_BLOCK = {
    "preforming", "wroth", "three", "there", "their", "where", "write", "right",
    "light", "night", "thing", "think", "other", "about", "could", "would",
    "should", "house", "horse", "world", "water", "after", "before", "people",
    "friend", "school", "change", "charge", "please", "place", "peace", "pont",
    "form", "from", "trial", "trail", "bread", "beard", "stone", "notes",
    "perform", "forming", "inform", "farmer", "former", "formal",
}


def _spell_variants(word):
    """相邻字母对调，或删掉一个中间字母。只动长度不少于 5 的词。"""
    if not re.fullmatch(r"[A-Za-z]{5,}", word):
        return []
    letters = list(word)
    raw = []
    a = letters[:]
    a[1], a[2] = a[2], a[1]
    raw.append("".join(a))
    if len(letters) >= 6:
        b = letters[:]
        b[-3], b[-2] = b[-2], b[-3]
        raw.append("".join(b))
        c = letters[:]
        del c[2]
        raw.append("".join(c))
    elif len(letters) == 5:
        c = letters[:]
        del c[3]
        raw.append("".join(c))
    out = []
    seen = {word.lower()}
    for item in raw:
        if item.lower() in seen or item.lower() in SPELL_BLOCK:
            continue
        seen.add(item.lower())
        out.append(item)
    return out


def spell_slips(body):
    """在原句最长的实词上做拼写相近的错误，不引入新词。"""
    words = body.split()
    ranked = []
    for i, word in enumerate(words):
        m = re.fullmatch(r"([^A-Za-z]*)([A-Za-z]+)([^A-Za-z]*)", word)
        if not m or m.group(2).lower() in CLOSED:
            continue
        if len(m.group(2)) < 5:
            continue
        ranked.append((len(m.group(2)), i, m))
    ranked.sort(key=lambda row: (-row[0], row[1]))
    out = []
    for _, i, m in ranked[:2]:
        for var in _spell_variants(m.group(2)):
            nxt = words[:]
            nxt[i] = m.group(1) + var + m.group(3)
            out.append(" ".join(nxt))
    return out


def more_fallbacks(body):
    """问候语的数和拼写，以及原句实词的拼写相近错误。不做随机抛词。"""
    out = []
    words = body.split()
    if len(words) == 2 and words[0].lower() == "good" and words[1].lower() in {"morning", "afternoon", "evening", "night"}:
        out.append(words[0] + " " + words[1] + "s")
        # morning → moring / monring：少一个字母，或相邻字母对调
        w = words[1]
        if len(w) >= 5:
            out.append(words[0] + " " + w[:2] + w[3:])
            letters = list(w)
            letters[2], letters[3] = letters[3], letters[2]
            out.append(words[0] + " " + "".join(letters))
    out.extend(spell_slips(body))
    return out


def plural_last(body):
    words = body.split()
    if not words:
        return None
    last = words[-1].strip(",;:")
    if not re.fullmatch(r"[A-Za-z]+", last):
        return None
    if last.lower() in {"is", "am", "are", "was", "were", "be", "to", "a", "the", "not", "too", "of", "in", "on", "at"}:
        return None
    if last.endswith("s") and not last.endswith("ss"):
        words[-1] = last[:-1]
    else:
        words[-1] = last + "s"
    return " ".join(words)


def adverb_order(body):
    m = re.search(r"\b(have|has|had)\s+(already|just|never)\s+([a-z]+)\s+(the|a|an|my|your|his|her|our|their)\b", body)
    if m:
        return (
            body[: m.start()]
            + "%s %s %s %s" % (m.group(1), m.group(3), m.group(2), m.group(4))
            + body[m.end() :]
        )
    m = re.search(r"^(Never|Always|Often|Usually)\s+([a-z]+)\b", body)
    if m:
        return m.group(2).capitalize() + " " + m.group(1).lower() + body[m.end() :]
    return None


def extra_to(body):
    # will / should + to + verb，典型多余 to
    m = re.search(MODAL + r"\s+(?!to\b)([a-z]+)\b", body)
    if m and m.group(2) not in ("not", "be"):
        return body[: m.start(2)] + "to " + m.group(2) + body[m.end(2) :]
    return None


def pronoun_slip(body):
    # 只在句子以 I / My 谈自己时，换成 your，避免把正确句又说成另一种也对的介绍
    if re.match(r"My\b", body):
        return sub_once(r"^My\b", "Your", body)
    if re.match(r"I am\b", body):
        return sub_once(r"^I am\b", "He is", body)
    if re.match(r"I have\b", body):
        return sub_once(r"^I have\b", "He have", body)
    if re.search(r"\bmy name\b", body):
        return sub_once(r"\bmy name\b", "your name", body)
    return None


def word_order_not(body):
    # 在主语后直接加 not，没有助动词：I not am / The flood not is
    m = re.match(r"^(I|You|We|They|He|She|It)\s+(?!not\b)(\w+)\b", body)
    if m:
        return body[: m.end(1)] + " not " + body[m.end(1) + 1 :]
    return None


def fact_change(body):
    for src, dst in WEEKDAY.items():
        if re.search(r"\b" + src + r"\b", body):
            return re.sub(r"\b" + src + r"\b", dst, body, count=1)
    swaps = [
        (r"\bwon\b", "lost"),
        (r"\blost\b", "won"),
        (r"\bmusic\b", "football"),
        (r"\bfootball\b", "music"),
        (r"\bClass 3\b", "Class 9"),
        (r"\bClass 9\b", "Class 1"),
        (r"\ba medal\b", "a ticket"),
        (r"\brest\b", "train"),
    ]
    for pat, repl in swaps:
        got = sub_once(pat, repl, body)
        if got and got != body:
            return got
    m = re.search(r"\b(is|are|am|was|were|has|have|can|will|should)\b", body)
    if m and not re.search(r"\bnot\b|n't", body):
        return body[: m.end()] + " not" + body[m.end() :]
    return None


def drop_clause(body):
    if " and " in body:
        left = body.rsplit(" and ", 1)[0].rstrip(",")
        if len(left.split()) >= 3:
            return left
    if ", " in body:
        left = body.split(", ", 1)[0]
        if len(left.split()) >= 3:
            return left
    return None


def apply_fns(body, fns):
    out = []
    seen = {norm(body)}
    for fn in fns:
        got = fn(body)
        if not got:
            continue
        got = re.sub(r"\s+", " ", got).strip()
        if norm(got) in seen:
            continue
        if got == body:
            continue
        seen.add(norm(got))
        out.append(got)
    return out


def candidates(answer, prompt, level, difficulty):
    body, punct = split_punct(answer)
    # 中文答案不在这里自动改写
    if re.search(r"[\u4e00-\u9fff]", body) and not re.search(r"[A-Za-z]", body):
        return []
    keypoint = "要点" in prompt
    consistent = ("一致" in prompt) or ("短文" in prompt and "哪一句" in prompt)
    basic = difficulty == "basic" or level in ("p", "j")

    if keypoint:
        raw = []
        dropped = drop_clause(body)
        if dropped:
            raw.append(dropped)
        changed = fact_change(body)
        if changed:
            raw.append(changed)
        # 再给一个语法错误，但先丢掉一个分句，避免「语法错但仍包含全部要点」
        if dropped:
            err = be_agreement(dropped) or verb_form(dropped) or article_error(dropped)
            if err:
                raw.append(err)
        fns_extra = apply_fns(body, [plural_error, article_error])
        raw.extend(fns_extra)
        raw.extend(more_fallbacks(body))
    elif consistent:
        raw = []
        changed = fact_change(body)
        if changed:
            raw.append(changed)
        raw.extend(apply_fns(body, [fact_change, be_agreement]))
        # fact_change 第二次可能得到同一个；下面再试否定
        neg = fact_change(body)
        if neg:
            neg2 = fact_change(neg)
            if neg2:
                raw.append(neg2)
        raw.extend(more_fallbacks(body))
    else:
        if basic or level in ("p", "j"):
            order = [be_agreement, verb_form, prep_error, to_ing, infinitive_s, plural_error,
                     article_error, extra_to, word_order_not]
        else:
            # 高中 standard：优先介词搭配、副词位置、动词形式，仍保证不合格
            order = [prep_error, adverb_order, verb_form, to_ing, infinitive_s, extra_to,
                     be_agreement, article_error, plural_error]
        if re.search(r"自己|想表达|想告诉|想说|应回答|你愿意|想礼貌", prompt):
            order.append(pronoun_slip)
        raw = apply_fns(body, order)
        # 拼写相近优先于整句换位：换最后两词有时会变成另一句也对的话
        raw.extend(more_fallbacks(body))
        swapped = swap_last_two(body)
        if swapped:
            raw.append(swapped)

    out = []
    seen = set()
    for item in raw:
        text = join_punct(item, punct)
        if norm(text) in seen or norm(text) == norm(answer):
            continue
        # 不要生成新的胡话
        if re.search(r"\b(ate|earthquake|hurricane|drought)\b", text, re.I) and not re.search(
            r"\b(ate|earthquake|hurricane|drought)\b", answer, re.I
        ):
            continue
        seen.add(norm(text))
        out.append(text)
    return out


SALAD_PATTERNS = [
    re.compile(r"\bate\b", re.I),
    re.compile(r"\bran me\b", re.I),
    re.compile(r"^(In conclusion|Therefore|However)\b", re.I),
    re.compile(
        r"^Please\s+(?!be\b|open\b|close\b|look\b|listen\b|sit\b|stand\b|help\b|stop\b|read\b|write\b|come\b|go\b|do\b|don't\b|take\b|give\b|tell\b|ask\b|keep\b|wait\b|try\b|use\b|make\b|let\b|turn\b|put\b|bring\b|call\b|show\b|check\b|remember\b|mind\b|excuse\b|wash\b|clean\b|speak\b|say\b|repeat\b|protect\b|don\b)",
        re.I,
    ),
    re.compile(r"\bis eating\b|\beating the tradition\b|\beating homework\b|\bis online eating\b", re.I),
    re.compile(r"\bI am in a flood\b|\bhave a hurricane\b|\bClose the hurricane\b|\bYou are my locker\b", re.I),
    re.compile(r"^Good (?!morni|monin|monri|afternoo|evenin|night\b|bye\b|idea\b|luck\b|job\b)", re.I),
    re.compile(
        r"\b(am|are|was|were)\s+(a|an|my|your)\s+(map|locker|book|medal|flood|diet|temple|wallet|castle|brochure|shelter|password|stadium|earthquake|hurricane|drought|volunteer|grade|hunter|reserve)\b",
        re.I,
    ),
    re.compile(r"^Sit on the name\b", re.I),
    re.compile(r"Class \d+ likes\b", re.I),
    re.compile(r"passed the quiz", re.I),
    re.compile(r"yesterday\s+tomorrow|tomorrow\s+yesterday", re.I),
    re.compile(r"^Yesterday please\b", re.I),
    re.compile(r"\bis a book\b", re.I),
    re.compile(r"castle eat|Where did the castle", re.I),
    re.compile(r"\bare (lockers|earthquakes|droughts|habitats)\b", re.I),
    re.compile(r"\bI (earthquake|drought|flood)\b", re.I),
    re.compile(r"^Eat the warning\b|^The drought won\b", re.I),
    re.compile(r"No, I am a brochure", re.I),
    re.compile(r"You are a (new earthquake|medal|duty|character)\b|You are an earthquake", re.I),
    re.compile(r"Diet is a marathon|The locker is a grade|Yesterday is a volunteer", re.I),
    re.compile(r"What is your pen\?", re.I),
    re.compile(r"\bI am a book\b", re.I),
    re.compile(r"Protected is a hunter|Please extinct|Agree is extinct|Buy is a reserve|Do not is a plain", re.I),
    re.compile(r"Deleted is an identity|Shall is an instrument|Shall is gravity", re.I),
    re.compile(r"Watch is a feast|Connected is a firework|Moon is used to origin|Classroom is a firework", re.I),
    re.compile(r"Return is a virtue|You are used to error|Different is a belief|Tell me photo or not|May is a costume", re.I),
    re.compile(r"Greeting means no person|Different is rude always|Take a loan is charity|Value is a bargain only", re.I),
    re.compile(r"Enough is a variable|First is a method only|First is homesick|Chopsticks are a flavour", re.I),
    re.compile(r"Plain is a delay|The frost is your fault always|Pressure is an ambulance|At once is a wound", re.I),
    re.compile(r"Canvas is an exhibition|Refresh is nutrition|Policy is a melt|Friday is a résumé|Friday is a resume", re.I),
    re.compile(r"Smiling sat the song|Add them before never|I protect because password", re.I),
    re.compile(r"\bis an? (medal|locker|temple|diet|wallet|castle|brochure|shelter|password|flood|battle|relic|blog|stadium|verb|prize|frown|crop|host|chopstick|carriage|brush|canvas|guide|nod|wetland|hunter|reserve|plain|grade|volunteer|marathon|firework|virtue|belief|costume|variable|flavour|delay|ambulance|wound|exhibition|nutrition|melt|hurricane|earthquake|drought)\b", re.I),
    re.compile(r"\bflood the\b|\bflood won\b|\bflood ended\b", re.I),
    re.compile(r"^Good night, close the door$", re.I),
    re.compile(r"^Survivors are lockers$|^Visitors are earthquakes$|^Visitors are droughts$|^Hunters are habitats$", re.I),
    re.compile(r"^I am a (drought|vocabulary|dynasty|shelter|brochure)$", re.I),
    re.compile(r"^You joined a earthquake$", re.I),
    re.compile(r"^Identity is online eating$|^Club is eating homework$|^Saturday is eating$|^Class 3 is eating$|^Xi'an is eating Friday$", re.I),
]


def is_vocab_prompt(prompt):
    return bool(re.search(r"哪个单词|的中文意思是哪一个|选择表示「", prompt))


CLOSED = {
    "a", "an", "the", "to", "of", "in", "on", "at", "for", "from", "with", "by",
    "not", "do", "does", "did", "be", "is", "am", "are", "was", "were", "been",
    "he", "she", "it", "we", "they", "you", "your", "my", "his", "her", "our",
    "their", "this", "that", "these", "those", "and", "or", "but", "so", "if",
    "when", "where", "who", "which", "what", "how", "yes", "no", "too", "very",
    "please", "let", "lets", "me", "him", "them", "us", "about", "into", "than",
    "as", "because", "before", "after", "there", "here",
}
COUNTABLE = {
    "morning", "afternoon", "evening", "night", "minute", "blanket", "visitor",
    "wall", "survivor", "character", "shelter", "student", "rule", "ticket",
    "day", "club", "name", "custom", "dinner", "voyage", "landmark", "person",
    "people", "injury", "hour", "week", "month", "year", "book", "school",
    "friend", "animal", "product", "volunteer", "gesture", "step",
}


def _toks(text):
    return [t.lower().replace("'", "") for t in re.findall(r"[A-Za-z']+", text)]


def _close_spell(tok, base):
    """相邻字母对调，或只少一个字母。用来接受 morning→moring / monring 这类拼写。"""
    if len(base) < 5 or abs(len(tok) - len(base)) > 1:
        return False
    if len(tok) == len(base):
        diffs = [i for i, (a, b) in enumerate(zip(tok, base)) if a != b]
        if len(diffs) == 2 and diffs[1] == diffs[0] + 1 and tok[diffs[0]] == base[diffs[1]] and tok[diffs[1]] == base[diffs[0]]:
            return True
    if len(tok) == len(base) - 1:
        for i in range(len(base)):
            if base[:i] + base[i + 1 :] == tok:
                return True
    return False


def tokens_ok(cand, answer):
    """新选项里的词必须来自原句、功能词，或原句单词的常见形态变化。"""
    base = set(_toks(answer))
    for tok in _toks(cand):
        if tok in base or tok in CLOSED:
            continue
        ok = False
        for b in base:
            if tok in {b + "ed", b + "d", b + "ing"}:
                ok = True
            elif (tok == b + "s" or tok == b + "es") and (b in COUNTABLE or b in TO_VERBS):
                ok = True
            elif b.endswith("e") and tok == b[:-1] + "ing":
                ok = True
            elif b.endswith("ed") and tok in {b[:-2], b[:-1]} and len(tok) >= 2:
                ok = True
            elif b.endswith("s") and not b.endswith("ss") and tok == b[:-1] and len(tok) >= 3:
                ok = True
            elif b.endswith("y") and tok == b[:-1] + "ied":
                ok = True
            elif b.endswith("ing") and tok == ing_to_base(b):
                ok = True
            elif b == "control" and tok == "controlled":
                ok = True
            elif tok == "football" and "music" in base:
                ok = True
            elif tok == "monday" and "friday" in base:
                ok = True
            elif _close_spell(tok, b):
                ok = True
        # 星期对调
        if tok in {w.lower() for w in WEEKDAY} or tok in {w.lower() for w in WEEKDAY.values()}:
            if any(w.lower() in base for w in WEEKDAY):
                ok = True
        if not ok:
            return False
    return True


def whitelisted(text):
    t = text.strip()
    if " " not in t and "\t" not in t:
        return True  # 单词选项：词汇干扰或词形，如 eated、gooder
    if t.lower() in {"good time", "big dog", "stop class", "look at"}:
        return True
    if re.match(r"(?i)^(They|He|She|We|I|It|Tom|The children|The students|My parents)\b.*\beating\b", t):
        return True
    if re.match(r"(?i)^Don't eating\b", t):
        return True
    if re.match(r"(?i)^Please (is|to be|being|be)\b", t):
        return True
    if re.search(r"[\u4e00-\u9fff]", t):
        return True
    return False


def is_salad(text, prompt, answer=""):
    if is_vocab_prompt(prompt) or whitelisted(text):
        return False
    # 干扰项里的名词如果就是正确答案里的词，多半是语序或搭配尝试，不是胡乱拼词
    if answer:
        ans_toks = {t.lower() for t in re.findall(r"[A-Za-z']+", answer)}
        m = re.search(r"\bis an? ([a-z]+)\b", text, re.I)
        if m and m.group(1).lower() in ans_toks and not re.search(
            r"\b(ate|earthquake|hurricane|Please )\b", text, re.I
        ):
            # 仍可能是 "is a medal" 这类；名词在答案里则先放过，交给别的模式
            text_for_isa = re.sub(r"\bis an? [a-z]+\b", "is an item", text, count=1, flags=re.I)
        else:
            text_for_isa = text
    else:
        text_for_isa = text
    return any(p.search(text_for_isa.strip()) for p in SALAD_PATTERNS)


def main():
    apply = "--apply" in sys.argv
    with open(PATH, encoding="utf-8") as f:
        questions = json.load(f)

    changes = []
    failed = []
    for q in questions:
        qid = str(q.get("id", ""))
        if not qid.startswith(("cne_p", "cne_j", "cne_h")) or q.get("type") != "choice":
            continue
        level = qid.split("_")[1][0]
        answer = next(c["text"] for c in q["choices"] if c["key"] == q["answer"])
        pool = candidates(answer, q["prompt"], level, q.get("difficulty") or "basic")
        used = {norm(c["text"]) for c in q["choices"]}
        # 正确项占用
        for c in q["choices"]:
            if c["key"] == q["answer"]:
                continue
            old = c["text"]
            if not is_salad(old, q["prompt"], answer):
                continue
            pick = None
            for cand in pool:
                if norm(cand) in used or norm(cand) == norm(answer):
                    continue
                if not tokens_ok(cand, answer):
                    continue
                pick = cand
                break
            if pick is None:
                failed.append((qid, old, answer, q["prompt"][:40]))
                continue
            used.add(norm(pick))
            changes.append({
                "id": qid,
                "key": c["key"],
                "difficulty": q.get("difficulty"),
                "level": level,
                "prompt": q["prompt"],
                "answer": answer,
                "old": old,
                "new": pick,
            })
            if apply:
                c["text"] = pick

    print("changes", len(changes), "questions", len({c["id"] for c in changes}), "failed", len(failed))
    by = {}
    for c in changes:
        by[c["level"]] = by.get(c["level"], 0) + 1
    print("by level options", by)
    if failed:
        print("--- failed ---")
        for row in failed:
            print(row)

    out = "/tmp/distractor_changelog.json"
    with open(out, "w", encoding="utf-8") as f:
        json.dump({"changes": changes, "failed": failed}, f, ensure_ascii=False, indent=2)
        f.write("\n")

    if apply:
        # 回读校验
        for q in questions:
            if q.get("type") != "choice":
                continue
            texts = [c["text"].strip() for c in q["choices"]]
            if len(set(texts)) != len(texts):
                raise SystemExit("duplicate text " + q["id"])
            if len({norm(t) for t in texts}) != len(texts):
                raise SystemExit("norm duplicate " + q["id"])
        with open(PATH, "w", encoding="utf-8") as f:
            json.dump(questions, f, ensure_ascii=False, indent=2)
            f.write("\n")
        print("wrote", PATH)
    else:
        # 打印前 40 和后 15
        for c in changes[:25]:
            print("\n%s [%s/%s] %s" % (c["id"], c["level"], c["difficulty"], c["prompt"][:70]))
            print("  A:", c["answer"])
            print("  -", c["old"])
            print("  +", c["new"])
        print("\n... total", len(changes))


if __name__ == "__main__":
    main()
