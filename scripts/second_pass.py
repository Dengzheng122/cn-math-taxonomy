#!/usr/bin/env python3
"""题库「独立第二遍复核」的辅助脚本（仅标准库）。

流程：
  1) python3 scripts/second_pass.py prepare [--chunk 90] [--prefix b]
       --prefix b：第二轮，只含「没有 verify 核验的题 + 所有 advanced 题」，写 blind_b_NN.json（解题者须附推导）；
       对应 compare --prefix b 读 ans_b_NN.json。
       把 numeric / choice / short 题去掉 answer、explanation、verify、accept，只留题干和选项，
       分块写到 data/_second_pass/blind_NN.json（供“不看答案”的独立解题者使用）。
  2) 解题者把自己的答案写到 data/_second_pass/ans_NN.json：{"题目id": "答案"}。
       numeric：数（整数/小数/分数 a/b/负数），多个答案用「，」；choice：选项字母；short：答案文字。
  3) python3 scripts/second_pass.py compare
       把独立答案与 questions.json 的 answer 对比，不一致的写到 data/_second_pass/mismatches.json
       （含两边的答案和题干，供逐条裁决）。
裁决后把结果记在 data/second_pass_log.json，verify_questions.py 会把它并入 verification_report.json。
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import validate as V  # noqa: E402
from engine_norm import norm_text  # noqa: E402  (见下方同目录小模块)

QPATH = os.path.join(ROOT, "data", "questions.json")
DIR = os.path.join(ROOT, "data", "_second_pass")


def load_questions():
    with open(QPATH, encoding="utf-8") as f:
        return json.load(f)


def is_risky(q):
    """第二轮（更仔细的盲解）的范围：没有 verify 表达式核验的题 + 所有 advanced 题。"""
    return q["type"] in ("numeric", "choice", "short") and (not q.get("verify") or q["difficulty"] == "advanced")


def prepare(chunk, prefix=""):
    os.makedirs(DIR, exist_ok=True)
    qs = [q for q in load_questions() if q["type"] in ("numeric", "choice", "short") and (not prefix or is_risky(q))]
    blind = []
    for q in qs:
        b = {"id": q["id"], "type": q["type"], "prompt": q["prompt"]}
        if q["type"] == "choice":
            b["choices"] = {c["key"]: c["text"] for c in q["choices"]}
        if q["type"] == "numeric" and q.get("unordered"):
            b["note"] = "多个答案，顺序无关"
        blind.append(b)
    n = 0
    for i in range(0, len(blind), chunk):
        n += 1
        path = os.path.join(DIR, "blind_%s%02d.json" % (prefix and prefix + "_", n))
        with open(path, "w", encoding="utf-8") as f:
            json.dump(blind[i:i + chunk], f, ensure_ascii=False, indent=1)
    print("写出 %d 块，共 %d 题 → data/_second_pass/blind_NN.json" % (n, len(blind)))


def same_numeric(q, mine):
    exp = V.parse_numeric_answer(q["answer"])
    got = V.parse_numeric_answer(str(mine))
    if exp is None or got is None or len(exp) != len(got):
        return False
    if q.get("unordered"):
        return sorted(exp) == sorted(got)
    return exp == got


def compare(prefix=""):
    qs = {q["id"]: q for q in load_questions()}
    if prefix:
        qs = {k: v for k, v in qs.items() if is_risky(v)}
    answers = {}
    pat = r"^ans_%s\d+\.json$" % (prefix and prefix + "_")
    for name in sorted(os.listdir(DIR)):
        if re.match(pat, name):
            with open(os.path.join(DIR, name), encoding="utf-8") as f:
                answers.update(json.load(f))
    mism, missing = [], []
    checked = 0
    for qid, q in qs.items():
        if q["type"] not in ("numeric", "choice", "short"):
            continue
        if qid not in answers:
            missing.append(qid)
            continue
        checked += 1
        mine = str(answers[qid]).strip()
        if q["type"] == "choice":
            ok = mine.strip().upper()[:1] == q["answer"]
        elif q["type"] == "numeric":
            ok = same_numeric(q, mine)
        else:
            refs = [q["answer"]] + list(q.get("accept", []))
            ok = norm_text(mine) in {norm_text(r) for r in refs}
        if not ok:
            m = {"id": qid, "type": q["type"], "prompt": q["prompt"], "answer": q["answer"], "independent": mine}
            if q["type"] == "choice":
                m["choices"] = {c["key"]: c["text"] for c in q["choices"]}
            mism.append(m)
    out = os.path.join(DIR, "mismatches%s.json" % (prefix and "_" + prefix))
    with open(out, "w", encoding="utf-8") as f:
        json.dump(mism, f, ensure_ascii=False, indent=1)
    by = {}
    for m in mism:
        by[m["type"]] = by.get(m["type"], 0) + 1
    print("独立答案 %d 道，缺失 %d；不一致 %d（%s）→ %s" % (
        checked, len(missing), len(mism), "，".join("%s %d" % kv for kv in sorted(by.items())) or "无",
        os.path.relpath(out, ROOT)))
    if missing:
        print("缺失：" + "，".join(missing[:30]) + (" ……" if len(missing) > 30 else ""))
    return 0 if not missing else 2


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "prepare":
        size = int(sys.argv[sys.argv.index("--chunk") + 1]) if "--chunk" in sys.argv else 90
        prepare(size, sys.argv[sys.argv.index("--prefix") + 1] if "--prefix" in sys.argv else "")
    elif cmd == "compare":
        sys.exit(compare(sys.argv[sys.argv.index("--prefix") + 1] if "--prefix" in sys.argv else ""))
    else:
        print(__doc__)
        sys.exit(1)
