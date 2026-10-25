#!/usr/bin/env python3
"""对照《义务教育数学课程标准（2022年版2025年修订）》复核第一至第三学段【内容要求】。

用法：
    python3 scripts/moe2025_check.py --moe /path/to/math-2025.txt

math-2025.txt 是修订版全文的公开转写（见 docs/moe2025-alignment.md 第 1 节）。
脚本只做「解析 → 对齐 → 报告」，**不写文件**；是否改数据由人决定。

输出三块：
  1. 每个（学段, 领域）在修订版文本里的条款数 vs 本仓库条目数；
  2. 相似度低于阈值的配对（>0.995 视为一致，只看差异）；
  3. 修订版多出来的条款（= 本仓库可能漏收）。
仅使用标准库。
"""
import argparse
import difflib
import json
import os
import re
import sys

try:  # Windows 控制台默认 GBK，遇到 ² 之类的字符会直接抛错
    sys.stdout.reconfigure(errors="replace")
except AttributeError:
    pass

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STD_PATH = os.path.join(ROOT, "data", "cn-curriculum-standards.json")

STAGE_RE = re.compile(r"^第([一二三四])学段（(\d)～(\d)年级）$")
CN = {"一": "1", "二": "2", "三": "3", "四": "4"}
DOMAINS = {"（一）数与代数": "NA", "（二）图形与几何": "GG",
           "（三）统计与概率": "SP", "（四）综合与实践": "IP"}
PAIRS = [("1", "NA"), ("2", "NA"), ("3", "NA"),
         ("1", "GG"), ("2", "GG"), ("3", "GG"),
         ("1", "SP"), ("2", "SP"), ("3", "SP")]


def unescape(s):
    for a, b in [("\\#", "#"), ("\\:", "："), ("\\.", "."), ("\\,", "，"), ("\\=", "="),
                 ("\\>", ">"), ("\\<", "<"), ("\\+", "+"), ("\\(", "("), ("\\)", ")"),
                 ("\\%", "%"), ("\\;", "；"), ("\\!", "！"), ("\\?", "？"), ("\\~", "~"),
                 ("\\*", "*"), ("\\[", "["), ("\\]", "]")]:
        s = s.replace(a, b)
    return s


def blocks(lines):
    """切出每个（领域, 学段）的【内容要求】正文行。"""
    out, cur, i = [], None, 0
    while i < len(lines):
        t = unescape(lines[i]).strip()
        if t in DOMAINS:
            cur = DOMAINS[t]
        m = STAGE_RE.match(t)
        if m and cur:
            j = i + 1
            while j < len(lines) and "【内容要求】" not in unescape(lines[j]):
                j += 1
            k = j + 1
            body = []
            while k < len(lines) and "【学业要求】" not in unescape(lines[k]) \
                    and "【教学提示】" not in unescape(lines[k]):
                body.append(lines[k])
                k += 1
            out.append((CN[m.group(1)], cur, j + 1, body))
            i = k
            continue
        i += 1
    return out


def parse(body):
    """把正文行切成条款：小节标题（1.数与运算）+ （n）条款；无编号的整段按一条处理。"""
    items, sub, cur, prose = [], None, None, []
    for raw in body:
        t = unescape(raw).strip()
        if not t or re.match(r"^\[1\]", t):  # 跳过混进正文的脚注
            continue
        m = re.match(r"^(\d+)\\?\.\s*(.+)$", t)
        if m and len(t) <= 20:
            if cur:
                items.append(cur)
                cur = None
            sub = m.group(2).strip()
            continue
        m2 = re.match(r"^（(\d+)）(.+)$", t)
        if m2:
            if cur:
                items.append(cur)
            cur = {"section": sub, "clause": "(" + m2.group(1) + ")", "text": m2.group(2)}
            continue
        if cur:
            cur["text"] += t
        else:
            prose.append(t)
    if cur:
        items.append(cur)
    if not items and prose:
        items = [{"section": sub or "", "clause": "", "text": "".join(prose)}]
    for it in items:
        it["text"] = re.sub(r"\s+", "", it["text"])
    return items


def norm(s):
    s = re.sub(r"（例\s*\d+[^）]*）", "", s)
    return re.sub(r"[^\u4e00-\u9fffA-Za-z0-9]", "", s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--moe", required=True, help="2025 修订版全文（math-2025.txt）")
    ap.add_argument("--std", default=STD_PATH, help="cn-curriculum-standards.json")
    ap.add_argument("--threshold", type=float, default=0.995)
    args = ap.parse_args()

    lines = open(args.moe, encoding="utf-8").read().split("\n")
    new = {}
    for stage, dom, start, body in blocks(lines):
        for it in parse(body):
            it["line"] = start
            new.setdefault((stage, dom), []).append(it)

    std = json.load(open(args.std, encoding="utf-8"))["items"]
    old = {}
    for it in std:
        m = re.match(r"cms-2022:(\d)\.([A-Z]{2})\.(\d+)$", it["id"])
        if m:
            old.setdefault((m.group(1), m.group(2)), []).append((int(m.group(3)), it))
    for k in old:
        old[k].sort()

    print("学段 领域 | 仓库条目 | 修订版条款")
    bad = 0
    for key in PAIRS:
        a, b = old.get(key, []), new.get(key, [])
        print("  %s %s | %d | %d" % (key[0], key[1], len(a), len(b)))
        if len(a) != len(b):
            bad += 1
    print("\n条款数不一致的组：%d" % bad)

    print("\n差异配对（相似度 < %.3f）" % args.threshold)
    n = 0
    for key in PAIRS:
        a = [x[1] for x in old.get(key, [])]
        b = new.get(key, [])
        for x, y in zip(a, b):
            r = difflib.SequenceMatcher(None, norm(x["text"]), norm(y["text"])).ratio()
            if r < args.threshold:
                n += 1
                print("\n  [%.3f] %s  %s:%d" % (r, x["id"], os.path.basename(args.moe), y["line"]))
                print("    仓库  ：", x["text"])
                print("    修订版：", y["text"])
    print("\n差异配对合计：%d" % n)

    print("\n修订版多出的条款（仓库可能漏收）")
    m = 0
    for key in PAIRS:
        b = new.get(key, [])[len(old.get(key, [])):]
        for y in b:
            m += 1
            print("  %s %s %s %s | %s" % (key[0], key[1], y["section"], y["clause"], y["text"]))
    print("合计：%d" % m)
    return 0


if __name__ == "__main__":
    sys.exit(main())
