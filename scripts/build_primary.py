#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把小学目录编译进 data/。可重复运行：初中知识点、初中题、初中之间的先修边保持原对象。

小学 id 按目录顺序从 cnm_p001 编号。旧 cnm_ext_* 不进 topics.json，写到 data/id-aliases.json。
"""
import copy
import hashlib
import json
import os
import sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from primary_g12 import TOPICS as T12
from primary_g34 import TOPICS as T34
from primary_g46 import TOPICS as T46
from primary_g56 import TOPICS as T56
from primary_std import ITEMS as PRIMARY_ITEMS
from primary_recheck import expected_numeric, eval_zh, fmt_value, solve_question
import verify_questions as VQ

DATA = os.path.join(ROOT, "data")
ZH = "一二三四五六"

# (初中 id, 旧外部 id) -> 小学 slug 列表。强度沿用原来的边。
# 理由在编译时用「原理由 + 具体小学知识点」写成完整句子。
RETARGET = {
    ("cnm_001", "cnm_ext_006"): ["neg_know"],
    ("cnm_003", "cnm_ext_002"): ["frac_meaning"],
    ("cnm_003", "cnm_ext_003"): ["dec_meaning"],
    ("cnm_023", "cnm_ext_003"): ["dec_approx"],
    ("cnm_025", "cnm_ext_007"): ["letter"],
    ("cnm_027", "cnm_ext_009"): ["qty_rel"],
    ("cnm_044", "cnm_ext_008"): ["lcm"],
    ("cnm_048", "cnm_ext_004"): ["pct_discount"],
    ("cnm_050", "cnm_ext_012"): ["cuboid", "cylinder"],
    ("cnm_051", "cnm_ext_015"): ["observe"],
    ("cnm_053", "cnm_ext_014"): ["line_seg"],
    ("cnm_056", "cnm_ext_013"): ["angle_measure"],
    ("cnm_057", "cnm_ext_009"): ["time_hms"],
    ("cnm_064", "cnm_ext_014"): ["perp"],
    ("cnm_067", "cnm_ext_014"): ["parallel"],
    ("cnm_072", "cnm_ext_015"): ["translate"],
    ("cnm_081", "cnm_ext_016"): ["coord_pair"],
    ("cnm_102", "cnm_ext_017"): ["stat_table"],
    ("cnm_105", "cnm_ext_017"): ["bar", "line_chart", "pie"],
    ("cnm_105", "cnm_ext_004"): ["pct_meaning"],
    ("cnm_106", "cnm_ext_017"): ["stat_table"],
    ("cnm_110", "cnm_ext_011"): ["tri_class"],
    ("cnm_120", "cnm_ext_015"): ["translate"],
    ("cnm_131", "cnm_ext_015"): ["reflect"],
    ("cnm_148", "cnm_ext_010"): ["rect_area"],
    ("cnm_150", "cnm_ext_008"): ["factor"],
    ("cnm_171", "cnm_ext_008"): ["factor"],
    ("cnm_200", "cnm_ext_005"): ["direct_prop"],
    ("cnm_211", "cnm_ext_017"): ["mean"],
    ("cnm_212", "cnm_ext_004"): ["pct_meaning"],
    ("cnm_213", "cnm_ext_017"): ["mean"],
    ("cnm_227", "cnm_ext_004"): ["pct_app"],
    ("cnm_237", "cnm_ext_005"): ["inverse_prop"],
    ("cnm_244", "cnm_ext_015"): ["rotate"],
    ("cnm_268", "cnm_ext_005"): ["proportion"],
    ("cnm_284", "cnm_ext_018"): ["chance"],
    ("cnm_285", "cnm_ext_002"): ["frac_meaning"],
    ("cnm_293", "cnm_ext_017"): ["stat_table"],
    ("cnm_295", "cnm_ext_004"): ["pct_meaning"],
    ("cnm_295", "cnm_ext_013"): ["angle_measure"],
    ("cnm_297", "cnm_ext_004"): ["pct_meaning"],
}

ALIASES = [
    ("cnm_ext_001", "整数四则运算与运算律", ["add_col", "mul_1d", "paren", "dist_law"]),
    ("cnm_ext_002", "分数的意义与四则运算", ["frac_meaning", "frac_add", "frac_mul", "frac_div"]),
    ("cnm_ext_003", "小数的意义与四则运算", ["dec_meaning", "dec_add", "dec_mul", "dec_div"]),
    ("cnm_ext_004", "百分数及其应用", ["pct_meaning", "pct_discount", "pct_app"]),
    ("cnm_ext_005", "比与比例（含正比例、反比例）", ["ratio", "proportion", "direct_prop", "inverse_prop"]),
    ("cnm_ext_006", "认识负数", ["neg_know"]),
    ("cnm_ext_007", "用字母表示数与简易方程", ["letter", "eq_solve"]),
    ("cnm_ext_008", "因数、倍数、质数与合数", ["factor", "prime", "lcm"]),
    ("cnm_ext_009", "常见数量关系与单位换算", ["qty_rel", "km", "g_kg", "time_hms"]),
    ("cnm_ext_010", "平面图形的认识及周长面积", ["rect_area", "para_area", "tri_area", "circ_area"]),
    ("cnm_ext_011", "三角形的分类与内角和", ["tri_class", "tri_angle_sum"]),
    ("cnm_ext_012", "立体图形的认识及表面积体积", ["cuboid", "cylinder", "cone"]),
    ("cnm_ext_013", "角的认识与度量", ["angle_measure", "angle_class"]),
    ("cnm_ext_014", "平行与垂直", ["perp", "parallel"]),
    ("cnm_ext_015", "图形的平移、旋转与轴对称", ["translate", "rotate", "reflect"]),
    ("cnm_ext_016", "用数对和方向距离确定位置", ["coord_pair", "dir_dist"]),
    ("cnm_ext_017", "统计表、统计图与平均数", ["stat_table", "line_chart", "pie", "mean"]),
    ("cnm_ext_018", "可能性", ["chance"]),
]


def load(name):
    with open(os.path.join(DATA, name), encoding="utf-8") as f:
        return json.load(f)


def dump(name, obj, indent):
    path = os.path.join(DATA, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=indent)
        f.write("\n")


def is_junior_id(tid):
    return isinstance(tid, str) and tid.startswith("cnm_") and not tid.startswith("cnm_p") and not tid.startswith("cnm_ext_")


def grade_rank(grade, semester):
    return grade * 2 + (1 if semester == "下" else 0)


def chapter_of(t):
    g = ZH[t["grade"] - 1]
    if t["ip"]:
        return "%s年级%s册 综合与实践 %s" % (g, t["semester"], t["uname"])
    if not t["unit"]:
        raise SystemExit("非综合与实践却没有单元号：%s" % t["slug"])
    return "%s年级%s册 第%d单元 %s" % (g, t["semester"], t["unit"], t["uname"])


def standards_of(codes):
    out = []
    for c in codes:
        if isinstance(c, tuple):
            code, note = c
            out.append({"id": "cms-2022:" + code, "confidence": "inferred", "note": note})
        else:
            out.append({"id": "cms-2022:" + c, "confidence": "exact"})
    return out


def primary_reason(child, pre, strength):
    if strength == "soft":
        return "「%s」对学习「%s」有帮助，但不会前者也可以开始学后者。" % (pre["name"], child["name"])
    return "学习「%s」需要先掌握「%s」。" % (child["name"], pre["name"])


def build_question(raw, tid, n):
    q = {
        "id": "%s_q%d" % (tid, n),
        "topicId": tid,
        "difficulty": raw["difficulty"],
        "type": raw["type"],
        "prompt": raw["prompt"],
    }
    ev = VQ.safe_eval(raw["verify"])
    if raw.get("_numchoice"):
        expr = raw["prompt"].split(" 的得数")[0]
        as_dec = ("." in expr) or ("314" in expr)
        correct = fmt_value(eval_zh(expr), as_decimal=as_dec)
        wrongs = []
        for w in raw["wrongs"]:
            text = w
            guard = 0
            while text == correct or text in wrongs:
                guard += 1
                if guard > 5:
                    raise SystemExit("%s 选项撞车无法避开：%s" % (q["id"], raw["prompt"]))
                text = text + str(guard)
            wrongs.append(text)
        shift = int(hashlib.md5(raw["prompt"].encode("utf-8")).hexdigest(), 16) % 4
        opts = wrongs[:]
        opts.insert(shift, correct)
        q["choices"] = [{"key": "ABCD"[i], "text": opts[i]} for i in range(4)]
        q["answer"] = "ABCD"[shift]
    elif raw["type"] == "choice":
        q["choices"] = raw["choices"]
        q["answer"] = solve_question(raw)
    else:
        ans = expected_numeric(raw["prompt"])
        if ans is None:
            raise SystemExit("数值题无法独立求解：%s %s" % (tid, raw["prompt"][:60]))
        q["answer"] = ans
    q["explanation"] = raw["explanation"]
    q["verify"] = raw["verify"]
    if q["type"] == "numeric":
        ok, detail = VQ.compare_numeric(q, ev)
    else:
        ok, detail = VQ.compare_choice(q, ev)
        # 再让独立求解器只看题干，核对选项字母
        if ok and not raw.get("_numchoice"):
            if solve_question(q) != q["answer"]:
                ok, detail = False, "solve_question 与 answer 不一致"
        elif ok and raw.get("_numchoice"):
            solved = solve_question(q)
            if solved != q["answer"]:
                ok, detail = False, "选择题得数对不上，解出 %s 答案 %s" % (solved, q["answer"])
    if not ok:
        raise SystemExit("%s 核验失败：%s\n  %s" % (q["id"], detail, q["prompt"][:80]))
    return q


def reachable(graph, start_topic, skip, hard_only):
    """从 start_topic 沿先修往上走，返回能到达的先修 id（不含自己）。"""
    seen = set()
    stack = []
    for pre, strength in graph.get(start_topic, []):
        if (start_topic, pre) == skip:
            continue
        if hard_only and strength != "hard":
            continue
        stack.append(pre)
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        for pre, strength in graph.get(node, []):
            if hard_only and strength != "hard":
                continue
            if pre not in seen:
                stack.append(pre)
    return seen


def reduce_new(edges, new_keys):
    """只删新边。每条边单独对照「去掉这一条之后的全图」判断。"""
    graph = defaultdict(list)
    for e in edges:
        graph[e["topicId"]].append((e["prerequisiteId"], e["strength"]))
    drop = set()
    for e in edges:
        key = (e["topicId"], e["prerequisiteId"])
        if key not in new_keys:
            continue
        if e["strength"] == "hard":
            hit = reachable(graph, e["topicId"], key, True)
        else:
            hit = reachable(graph, e["topicId"], key, False)
        if e["prerequisiteId"] in hit:
            drop.add(key)
    kept = [e for e in edges if (e["topicId"], e["prerequisiteId"]) not in drop]
    return kept, len(drop)


def main():
    catalog = T12 + T34 + T46 + T56
    by_slug = {}
    for i, t in enumerate(catalog):
        if t["slug"] in by_slug:
            raise SystemExit("slug 重复：" + t["slug"])
        by_slug[t["slug"]] = t
        t["_i"] = i

    topics_raw = load("topics.json")
    deps_raw = load("dependencies.json")
    questions_raw = load("questions.json")
    standards_raw = load("cn-curriculum-standards.json")

    junior_topics = [t for t in topics_raw if is_junior_id(t.get("id"))]
    junior_snap = copy.deepcopy(junior_topics)
    junior_ids = {t["id"] for t in junior_topics}
    if len(junior_topics) != 315:
        raise SystemExit("初中正式知识点应是 315，实际 %d" % len(junior_topics))

    junior_deps = [d for d in deps_raw
                   if is_junior_id(d.get("topicId")) and is_junior_id(d.get("prerequisiteId"))]
    junior_dep_snap = copy.deepcopy(junior_deps)
    # 保护：cnm_221 的边不得改
    cnm_221_before = [(d["prerequisiteId"], d["strength"]) for d in deps_raw if d["topicId"] == "cnm_221"]

    ext_edges = [d for d in deps_raw
                 if str(d.get("topicId", "")).startswith("cnm_ext_") or str(d.get("prerequisiteId", "")).startswith("cnm_ext_")]
    # 首次运行时用原边核对强度；重复运行时这些边已经不在文件里
    if ext_edges:
        seen_retarget = {}
        for d in ext_edges:
            if str(d["topicId"]).startswith("cnm_ext_"):
                continue
            seen_retarget[(d["topicId"], d["prerequisiteId"])] = d["strength"]
        if set(seen_retarget) != set(RETARGET):
            missing = set(seen_retarget) - set(RETARGET)
            extra = set(RETARGET) - set(seen_retarget)
            raise SystemExit("改指向表与现有边不一致 missing=%s extra=%s" % (missing, extra))

    # 原边的理由与强度：优先读文件，否则用上一次编译不了——首次必须能读到
    orig_meta = {}
    if ext_edges:
        for d in ext_edges:
            if is_junior_id(d["topicId"]):
                orig_meta[(d["topicId"], d["prerequisiteId"])] = (d["strength"], d["reason"])
    else:
        # 重复运行：从本脚本无法恢复原文，强度按 RETARGET 注释中的约定不存。
        # 要求调用方保留不了时，拒绝空跑覆盖理由。这里从现有「指向小学」的边无法区分。
        raise SystemExit("dependencies.json 里已经没有 cnm_ext_* 边。请只在含外部节点的原图上编译一次；若要重编，先用 git checkout 恢复 data/dependencies.json 与 data/topics.json。")

    primary_topics = []
    primary_questions = []
    slug_to_id = {}
    for i, t in enumerate(catalog, start=1):
        tid = "cnm_p%03d" % i
        slug_to_id[t["slug"]] = tid
        qs = [build_question(raw, tid, n) for n, raw in enumerate(t["qs"], start=1)]
        q1 = qs[0]
        if q1["type"] == "choice":
            diag_answer = next(c["text"] for c in q1["choices"] if c["key"] == q1["answer"])
        else:
            diag_answer = q1["answer"]
        node = {
            "id": tid,
            "name": t["name"],
            "domain": t["domain"],
            "grade": t["grade"],
            "semester": t["semester"],
            "chapter": chapter_of(t),
            "type": t["type"],
            "description": t["description"],
            "mastery_criteria": list(t["mastery_criteria"]),
            "diagnostic_question": {"question": q1["prompt"], "answer": diag_answer},
            "external": False,
            "standards": standards_of(t["standards"]),
        }
        if t.get("root_reason"):
            node["root_reason"] = t["root_reason"]
        primary_topics.append(node)
        primary_questions.extend(qs)

    id_to_topic = {t["id"]: t for t in primary_topics}
    id_to_topic.update({t["id"]: t for t in junior_topics})

    new_edges = []
    for t in catalog:
        tid = slug_to_id[t["slug"]]
        for pre in t["pre"]:
            if isinstance(pre, tuple):
                slug, strength = pre
            else:
                slug, strength = pre, "hard"
            if slug not in slug_to_id:
                raise SystemExit("%s 的先修 %s 不存在" % (t["slug"], slug))
            pid = slug_to_id[slug]
            if slug_to_id and catalog[by_slug[slug]["_i"]]["_i"] >= t["_i"]:
                raise SystemExit("%s 的先修 %s 不在它前面" % (t["slug"], slug))
            new_edges.append({
                "topicId": tid,
                "prerequisiteId": pid,
                "strength": strength,
                "reason": primary_reason(t, by_slug[slug], strength),
            })

    for (jid, ext), slugs in RETARGET.items():
        strength, reason = orig_meta[(jid, ext)]
        jname = next(t["name"] for t in junior_topics if t["id"] == jid)
        for slug in slugs:
            pid = slug_to_id[slug]
            pname = by_slug[slug]["name"]
            text = reason if reason.endswith("。") else reason + "。"
            new_edges.append({
                "topicId": jid,
                "prerequisiteId": pid,
                "strength": strength,
                "reason": "学习「%s」需要先会小学的「%s」。%s" % (jname, pname, text),
            })

    # 年级单调：先修的年级不晚于知识点
    for e in new_edges + junior_deps:
        a = id_to_topic[e["topicId"]]
        b = id_to_topic[e["prerequisiteId"]]
        if grade_rank(b["grade"], b["semester"]) > grade_rank(a["grade"], a["semester"]):
            raise SystemExit("年级倒退：%s(%s%s) 依赖 %s(%s%s)" % (
                a["id"], a["grade"], a["semester"], b["id"], b["grade"], b["semester"]))

    all_edges = new_edges + junior_deps
    new_keys = {(e["topicId"], e["prerequisiteId"]) for e in new_edges}
    # 重复边
    seen = set()
    for e in all_edges:
        k = (e["topicId"], e["prerequisiteId"])
        if k in seen:
            raise SystemExit("重复边 %s <- %s" % k)
        seen.add(k)
    reduced, n_drop = reduce_new(all_edges, new_keys)

    # 别名
    alias_obj = {
        "description": "方案 b：18 个 cnm_ext_* 已从 topics.json 删除，不再作为节点。诊断或浏览遇到旧 id（例如 ?target=cnm_ext_002）时，按 targets 跳到对应的小学正式知识点。targets 是该外部节点所概括内容里的代表知识点，不是完整清单。",
        "aliases": {},
    }
    for key, name, slugs in ALIASES:
        alias_obj["aliases"][key] = {"name": name, "targets": [slug_to_id[s] for s in slugs]}

    # 课标：小学条目放在第四学段前面。第四学段条目对象不改写。
    stage4 = [it for it in standards_raw["items"] if isinstance(it, dict) and str(it.get("id", "")).startswith("cms-2022:4.")]
    if len(stage4) != 157:
        raise SystemExit("第四学段条目应是 157，实际 %d" % len(stage4))
    stage4_snap = copy.deepcopy(stage4)
    src = standards_raw["source"]
    src["stage"] = "第一至第四学段（1～9年级）"
    src["retrieved"] = "2026-10-17（第四学段）；2026-10-19（第一至三学段）"
    extra = ("第一至三学段条目据公开转写整理（21世纪教育网预览 http://zy.21cnjy.com/20610065 ，检索 2026-10-19），"
             "不是教育部 PDF 的逐页核对，page_or_ref 为「待核」，verbatim 为 false。"
             "第四学段条目正文未改。")
    if extra not in src.get("note", ""):
        src["note"] = src.get("note", "").rstrip() + extra
    standards_raw["items"] = list(PRIMARY_ITEMS) + stage4

    topics_out = primary_topics + junior_topics
    questions_out = primary_questions + [q for q in questions_raw if is_junior_id(q.get("topicId"))]
    if len(questions_out) - len(primary_questions) != 1407:
        raise SystemExit("初中题应保持 1407，实际 %d" % (len(questions_out) - len(primary_questions)))

    # 深比较：初中对象没有被改写
    if junior_topics != junior_snap:
        raise SystemExit("初中知识点对象被改动")
    if junior_deps != junior_dep_snap:
        raise SystemExit("初中之间的先修边被改动")
    if stage4 != stage4_snap:
        raise SystemExit("第四学段课标条目被改动")
    cnm_221_after = [(d["prerequisiteId"], d["strength"]) for d in reduced if d["topicId"] == "cnm_221"]
    if cnm_221_after != cnm_221_before:
        raise SystemExit("cnm_221 的边被改动 %s -> %s" % (cnm_221_before, cnm_221_after))

    dump("topics.json", topics_out, 2)
    dump("dependencies.json", reduced, 2)
    dump("questions.json", questions_out, 1)
    dump("cn-curriculum-standards.json", standards_raw, 2)
    dump("id-aliases.json", alias_obj, 2)

    # 按年级分批，便于核对；合并结果在 questions.json
    os.makedirs(os.path.join(DATA, "_qbatches"), exist_ok=True)
    by_grade = defaultdict(list)
    for q in primary_questions:
        g = id_to_topic[q["topicId"]]["grade"]
        by_grade[g].append(q)
    for g, qs in sorted(by_grade.items()):
        dump("_qbatches/primary_g%d.json" % g, qs, 1)

    # 独立复核记录（不覆盖初中的 second_pass 字段）
    log_path = os.path.join(DATA, "second_pass_log.json")
    with open(log_path, encoding="utf-8") as f:
        log = json.load(f)
    disagree = []
    by_type = Counter()
    for q in primary_questions:
        by_type[q["type"]] += 1
        got = solve_question(q)
        if got != q["answer"]:
            disagree.append({"id": q["id"], "独立答案": got, "题库答案": q["answer"]})
    passes = [p for p in log.get("passes", []) if not str(p.get("name", "")).startswith("C：")]
    passes.append({
        "name": "C：小学题独立复核（primary_recheck，只读题干和选项，不读 answer / verify / explanation）",
        "solver": "scripts/primary_recheck.py",
        "questions": len(primary_questions),
        "by_type": dict(by_type),
        "disagreements": len(disagree),
        "adjudication": "不一致的题必须先改目录再编译；本轮为 0" if not disagree else "见 primary_disagreements",
    })
    log["passes"] = passes
    log["primary_checked"] = len(primary_questions)
    log["primary_disagreements"] = disagree
    log["second_pass_mismatch"] = log.get("second_pass_mismatch") or []
    if disagree:
        log["second_pass_mismatch"] = disagree
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print("小学知识点 %d" % len(primary_topics), Counter(t["grade"] for t in primary_topics))
    print("新边（约简前）%d，删去冗余 %d，写出边 %d（其中初中—初中 %d）" % (
        len(new_edges), n_drop, len(reduced), len(junior_deps)))
    print("小学题 %d" % len(primary_questions), Counter(q["type"] for q in primary_questions),
          Counter(q["difficulty"] for q in primary_questions))
    print("课标 %d（小学 %d + 第四学段 %d）" % (len(standards_raw["items"]), len(PRIMARY_ITEMS), len(stage4)))
    print("复核不一致 %d" % len(disagree))
    if disagree:
        raise SystemExit(disagree[:10])


if __name__ == "__main__":
    main()
