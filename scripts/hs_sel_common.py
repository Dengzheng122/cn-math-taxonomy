"""高中选择性必修数据的登记表。由 scripts/hs_sel_build.py 编译进 data/*.json。

不和 scripts/hs_common.py 共用列表，避免和已编译的必修草稿混在一起。
"""
from __future__ import annotations

TOPICS = []
QUESTIONS = {}
EDGES = []
STANDARDS = []


def standard(code, domain, theme, section, clause, text):
    STANDARDS.append({
        "code": code,
        "domain": domain,
        "theme": theme,
        "section": section,
        "clause": clause,
        "text": text,
    })


def topic(key, book, chapter, section, name, domain, typ, desc, crit, std, conf="exact", note=None):
    if any(t["key"] == key for t in TOPICS):
        raise SystemExit("知识点 key 重复：%s" % key)
    if book not in (1, 2, 3):
        raise SystemExit("%s 的册次必须是 1、2 或 3" % key)
    if not (2 <= len(crit) <= 3):
        raise SystemExit("%s 掌握标准须 2–3 条" % key)
    TOPICS.append({
        "key": key,
        "book": book,
        "chapter": chapter,
        "section": section,
        "name": name,
        "domain": domain,
        "type": typ,
        "description": desc,
        "mastery_criteria": list(crit),
        "std": std,
        "confidence": conf,
        "note": note,
    })


def questions(key, items):
    if key in QUESTIONS:
        raise SystemExit("题目重复：%s" % key)
    if len(items) != 4:
        raise SystemExit("%s 需要 4 道题，实际 %d" % (key, len(items)))
    QUESTIONS[key] = items


def edge(src, dst, strength, reason):
    EDGES.append((src, dst, strength, reason))


def hard(src, dst, reason):
    edge(src, dst, "hard", reason)


def soft(src, dst, reason):
    edge(src, dst, "soft", reason)
