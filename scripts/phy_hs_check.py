#!/usr/bin/env python3
"""检查一份高中物理草稿（scripts/phy_hs_<id>.py）：结构、先修、课标引用、题目核验。

用法：python3 scripts/phy_hs_check.py a01          # 检查 phy_hs_a01.py，只报告错误，不写任何数据文件
      python3 scripts/phy_hs_check.py a01 --show   # 另外打印每个知识点的题目便于人工通读
"""
from __future__ import annotations

import importlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import phy_g8a, phy_g8b, phy_g9  # noqa: E402,F401
import phy_lib  # noqa: E402
import phy_hs_lib as L  # noqa: E402
import phy_hs_plan as P  # noqa: E402
from verify_questions import verify_all  # noqa: E402
import validate as V  # noqa: E402

BAN = re.compile(r"免费|AI\s*初稿|AI初稿")
JUNIOR = {t["key"]: t for t in phy_lib.TOPICS}


def lint_topic(key, t, errs, warns, math_ids):
    plan = P.PLAN_BY_KEY[key]
    where = "%s(%s)" % (key, plan["name"])
    if t["type"] not in V.TYPES:
        errs.append("%s type 非法：%r" % (where, t["type"]))
    if not (30 <= len(t["description"]) <= 260):
        warns.append("%s description 长度 %d，建议 40–200 字" % (where, len(t["description"])))
    if not t["std"]:
        errs.append("%s 没有课标条目" % where)
    if len(t["std"]) > V.MAX_STANDARDS_PER_TOPIC:
        errs.append("%s 课标条目超过 %d 条" % (where, V.MAX_STANDARDS_PER_TOPIC))
    for tail, conf in t["std"]:
        if tail not in L.VALID_STD:
            errs.append("%s 引用了不存在的课标条目 %s" % (where, tail))
        if conf not in V.CONFIDENCES:
            errs.append("%s 课标 confidence 非法：%r" % (where, conf))
    if len({s[0] for s in t["std"]}) != len(t["std"]):
        errs.append("%s 课标条目重复" % where)
    if not t["pre"] and not t["root"]:
        errs.append("%s 没有先修也没有 root" % where)
    if t["root"] is not None and not str(t["root"]).strip():
        errs.append("%s root 为空字符串" % where)
    seen = set()
    for pk, strength in t["pre"]:
        if strength not in V.STRENGTHS:
            errs.append("%s 先修强度非法：%r" % (where, strength))
        if pk in seen:
            errs.append("%s 先修重复：%s" % (where, pk))
        seen.add(pk)
        if pk.startswith("J:"):
            if pk[2:] not in JUNIOR:
                errs.append("%s 的初中先修 %s 不存在（见 phy_g8a/g8b/g9 的 key）" % (where, pk))
        elif pk not in P.PLAN_BY_KEY:
            errs.append("%s 的先修 %s 不在计划里" % (where, pk))
        elif P.ORDER[pk] >= P.ORDER[key]:
            errs.append("%s 的先修 %s 排在它后面或就是它自己" % (where, pk))
    for ml in t["math"]:
        if not (isinstance(ml, (tuple, list)) and len(ml) == 2 and str(ml[1]).strip()):
            errs.append("%s mathLinks 必须是 (id, 说明)" % where)
        elif ml[0] not in math_ids:
            errs.append("%s mathLinks 指向不存在的数学知识点 %s" % (where, ml[0]))
    qs = t["qs"]
    if len(qs) != 4:
        errs.append("%s 题数 %d，必须是 4" % (where, len(qs)))
    diffs = [q["diff"] for q in qs]
    if not {"basic", "standard"} <= set(diffs):
        errs.append("%s 难度需至少含 basic 和 standard：%s" % (where, diffs))
    for q in diffs:
        if q not in V.Q_DIFFICULTIES:
            errs.append("%s 难度非法：%s" % (where, q))
    if qs and qs[0]["diff"] != "basic":
        warns.append("%s 第一题（诊断题）建议是 basic" % where)
    for i, q in enumerate(qs, 1):
        w = "%s_q%d" % (key, i)
        for field in ("prompt", "expl"):
            if BAN.search(q[field]):
                errs.append("%s %s 含禁用文案" % (w, field))
        if q["kind"] == "numeric":
            if "只填数值" not in q["prompt"]:
                warns.append("%s 数值题题干建议以（只填数值）收尾并写明单位" % w)
            if not q["verify"]:
                errs.append("%s 数值题缺 verify" % w)
            if re.search(r"[eE]\d|×10", q["answer"]):
                errs.append("%s numeric answer 必须写成十进制数：%s" % (w, q["answer"]))
        else:
            if not (2 <= len(q["wrongs"]) <= 3):
                errs.append("%s 选择题需要 2–3 个错误选项（推荐 3 个）" % w)
            if len(q["wrongs"]) == 2:
                warns.append("%s 只有 2 个错误选项，建议 3 个" % w)
            for x in [q["right"]] + q["wrongs"]:
                if BAN.search(x):
                    errs.append("%s 选项含禁用文案" % w)
            lens = [len(q["right"])] + [len(x) for x in q["wrongs"]]
            if len(q["right"]) >= 2 * max(len(x) for x in q["wrongs"]) + 6:
                warns.append("%s 正确选项明显比干扰项长，容易被猜中" % w)
        if len(q["expl"]) < 12:
            errs.append("%s 解析太短" % w)


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in P.ASSIGN:
        print("用法：phy_hs_check.py <%s> [--show]" % "|".join(P.ASSIGN))
        return 2
    fid = sys.argv[1]
    show = "--show" in sys.argv
    mod = importlib.import_module("phy_hs_" + fid)  # noqa: F841
    want = P.keys_for(fid)
    got = [k for k in L.HS if k in set(want)]
    extra = [k for k in L.HS if k not in set(want)]
    errs, warns = [], []
    for k in want:
        if k not in L.HS:
            errs.append("缺少知识点 %s（%s）" % (k, P.PLAN_BY_KEY[k]["name"]))
    for k in extra:
        errs.append("登记了不属于 %s 的知识点 %s" % (fid, k))
    with open(os.path.join(ROOT, "data", "topics.json"), encoding="utf-8") as f:
        math_ids = {t["id"] for t in json.load(f) if str(t["id"]).startswith("cnm_")}
    allq = []
    for k in want:
        if k not in L.HS:
            continue
        t = L.HS[k]
        lint_topic(k, t, errs, warns, math_ids)
        allq.extend(L.compile_questions(k, L.tid_of(k), t, errs))
    res = verify_all(allq)
    for m in res["mismatch"]:
        errs.append("核验不通过 %s：%s（answer=%s verify=%s）" % (m["id"], m.get("detail"), m["answer"], m["verify"]))
    unver = [q["id"] for q in allq if q["type"] == "choice" and q["verify"].startswith('"')]
    print("%s：知识点 %d/%d，题目 %d，自动核验 %d，选择题仅文字比对 %d" % (
        fid, len(got), len(want), len(allq), len(res["auto_verified"]), len(unver)))
    if show:
        for k in want:
            if k not in L.HS:
                continue
            t = L.HS[k]
            print("\n## %s %s [%s] pre=%s" % (L.tid_of(k), P.PLAN_BY_KEY[k]["name"], t["domain"], t["pre"]))
            for q in L.compile_questions(k, L.tid_of(k), t, []):
                print("  - [%s] %s" % (q["difficulty"], q["prompt"]))
                if q["type"] == "choice":
                    print("     " + " | ".join("%s.%s" % (c["key"], c["text"]) for c in q["choices"]) + "  → " + q["answer"])
                else:
                    print("     答案 " + q["answer"])
                print("     解析：" + q["explanation"])
    for w in warns:
        print("警告：" + w)
    for e in errs:
        print("错误：" + e)
    print("CHECK %s" % ("FAILED（%d 个错误）" % len(errs) if errs else "PASSED"))
    return 1 if errs else 0


if __name__ == "__main__":
    sys.exit(main())
