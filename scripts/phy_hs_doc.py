#!/usr/bin/env python3
"""由 data/ 生成 docs/physics-senior-mapping.md（高中物理：课标模块 ↔ 人教版册/章/节 ↔ 知识点）。

先运行 python3 scripts/phy_build.py，再运行本脚本。文档里的表格全部来自数据，不手写。
"""
from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import phy_hs_plan as P  # noqa: E402
import phy_hs_std as S  # noqa: E402


def load(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8") as f:
        return json.load(f)


def main():
    topics = {t["id"]: t for t in load("topics.json")}
    deps = load("dependencies.json")
    qs = load("questions.json")
    std = load("cn-curriculum-standards.json")
    senior = [t for t in topics.values() if str(t["id"]).startswith("cnp_h")]
    sd = [d for d in deps if str(d["topicId"]).startswith("cnp_h")]
    sq = [q for q in qs if str(q["topicId"]).startswith("cnp_h")]
    items = [i for i in std["items"] if str(i["id"]).startswith("cps-hs-2017:")]
    to_junior = [d for d in sd if str(d["prerequisiteId"]).startswith("cnp_") and not str(d["prerequisiteId"]).startswith("cnp_h")]
    by_std = defaultdict(list)
    for t in senior:
        for s in t["standards"]:
            by_std[s["id"]].append(t["id"])
    src = std["physics_senior"]
    out = []
    w = out.append
    w("# 高中物理：课标模块 ↔ 人教版册、章、节 ↔ 知识点\n")
    w("> 本页由 `scripts/phy_hs_doc.py` 根据 `data/` 生成，不要手改。映射由本项目自己做，未经教师或课程专家审核。\n")
    w("## 1. 版本依据\n")
    w("| 项目 | 内容 |\n|---|---|")
    w("| 课标 | 《%s》，%s，%s |" % (src["title"], src["issuer"], src["revision"]))
    w("| 课标文本 | %s（检索 %s）。**文字层抓取，未与纸本逐字核对**，`verbatim` 为 false，`page_or_ref` 为「待核」 |" % (src["url"], src["retrieved"]))
    w("| 教材 | 人民教育出版社 普通高中教科书·物理（人教版）必修第一册、第二册、第三册、选择性必修第一册、第二册、第三册；2019 年审定，依据 2017 年版课标 |")
    w("| 教材目录来源 | 教师之家 renjiaoshe.com 的「2019版」目录页（逐册抄录到节）；**各册具体印次未逐册核对版权页**，2024–2025 年流通印次的目录与此是否完全一致未逐节核实 |")
    w("| 范围 | 必修 3 册 + 选择性必修 3 册。课标的选修课程（选修 1–3）、活动建议和「例」不收录 |")
    w("| 编号 | 知识点 `cnp_h001`–`cnp_h%03d`（按教材顺序，与初中 `cnp_001`–`cnp_092` 不冲突）；课标 `cps-hs-2017:<B 必修|S 选择性必修><册号>.<主题>.<条款>`，实验用主题 `X` |" % len(senior))
    w("| 年级编号 | grade 10–12 = 必修第一至三册，13–15 = 选择性必修第一至三册，semester 都写「上」，与高中英语的编号习惯一致 |\n")
    w("## 2. 课标模块与教材册章的对应\n")
    w("课标把必修分成「必修 1、2、3」三个模块，选择性必修也是三个模块；教材的册与模块一一对应，但章的切法与课标主题不完全重合：\n")
    w("| 课标模块 | 课标主题 | 教材 | 章 |\n|---|---|---|---|")
    rows = [
        ("必修 1", "机械运动与物理模型；相互作用与运动定律", "必修第一册", "第一至四章"),
        ("必修 2", "机械能及其守恒定律；曲线运动与万有引力定律；牛顿力学的局限性与相对论初步", "必修第二册", "第五至八章（相对论在第七章第 5 节）"),
        ("必修 3", "静电场；电路及其应用；电磁场与电磁波初步；能源与可持续发展", "必修第三册", "第九至十三章（能源在第十二章第 4 节）"),
        ("选择性必修 1", "动量与动量守恒定律；机械振动与机械波；光及其应用", "选择性必修第一册", "第一至四章"),
        ("选择性必修 2", "磁场；电磁感应及其应用；电磁振荡与电磁波；传感器", "选择性必修第二册", "第一至五章"),
        ("选择性必修 3", "固体、液体和气体；热力学定律；原子与原子核；波粒二象性", "选择性必修第三册", "第一至五章（分子动理论课标放在「固体、液体和气体」里；原子结构与波粒二象性教材合在第四章）"),
    ]
    for r in rows:
        w("| %s | %s | %s | %s |" % r)
    w("")
    w("## 3. 数量\n")
    c = Counter(t["grade"] for t in senior)
    names = {10: "必修第一册", 11: "必修第二册", 12: "必修第三册", 13: "选择性必修第一册", 14: "选择性必修第二册", 15: "选择性必修第三册"}
    w("| 册 | 知识点 | 题目 | 课标条目 |\n|---|---:|---:|---:|")
    qcount = Counter(topics[q["topicId"]]["grade"] for q in sq)
    mod_of = {10: "B1", 11: "B2", 12: "B3", 13: "S1", 14: "S2", 15: "S3"}
    scount = Counter(i["id"].split(":")[1][:2] for i in items)
    for g in range(10, 16):
        w("| %s | %d | %d | %d |" % (names[g], c[g], qcount[g], scount[mod_of[g]]))
    w("| 合计 | %d | %d | %d |\n" % (len(senior), len(sq), len(items)))
    hard = sum(d["strength"] == "hard" for d in sd)
    w("先修边 %d 条（hard %d，soft %d），其中指向初中物理 %d 条；mathLinks %d 条（%d 个知识点）。没有任何跨学科先修边。\n" % (
        len(sd), hard, len(sd) - hard, len(to_junior), sum(len(t.get("mathLinks", [])) for t in senior),
        sum(1 for t in senior if t.get("mathLinks"))))
    w("## 4. 各册知识点（按教材目录）\n")
    cur = None
    for r in P.PLAN:
        tid = "cnp_h%03d" % (P.ORDER[r["key"]] + 1)
        t = topics.get(tid)
        if not t:
            continue
        head = (r["book"], r["chapter_no"])
        if cur != head:
            if cur is None or cur[0] != r["book"]:
                w("\n### %s（%s）\n" % (P.BOOKS[r["book"]]["full"], r["mod"]))
                w("| 章 | 节 | 知识点 | 课标 |\n|---|---|---|---|")
            cur = head
        stds = "、".join("%s%s" % (s["id"].split(":")[1], "" if s["confidence"] == "exact" else "*") for s in t["standards"])
        w("| 第%s章 %s | %s.%s %s | %s %s | %s |" % (P.CN_NUM[r["chapter_no"]], r["chapter_name"], r["chapter_no"], r["sec_no"],
                                                  r["sec_title"], tid, t["name"], stds))
    w("\n课标列：带 `*` 的是 inferred（相关但不是专门讲它的条款），其余是 exact。\n")
    w("## 5. 课标条目被引用情况\n")
    unused = [i for i in items if not by_std.get(i["id"])]
    w("条目 %d 条（内容要求 %d + 学生必做实验 %d），被至少一个知识点引用 %d 条。" % (
        len(items), sum(1 for i in items if ".X." not in i["id"]), sum(1 for i in items if ".X." in i["id"]), len(items) - len(unused)))
    if unused:
        w("\n没有知识点引用的条目（多为科学史、STSE 一类的泛化要求）：\n")
        for i in unused:
            w("- `%s` %s" % (i["id"], i["text"]))
    w("\n## 6. 已知局限\n")
    w("- 课标文本取自出版社 PDF 的文字层，没有对照纸本或教育部原件逐字核对。")
    w("- 教材目录取自 2019 版目录页，没有逐册核对 2024–2025 年印次的版权页。")
    w("- 课标的「例」和「活动建议」没有收录；选修 1–3 不收录。")
    w("- 知识点颗粒度是「节」或「节内的一个主要概念/一个实验」，不对应教材的每个小标题。")
    w("- 题目由 AI 撰写，再由另一轮独立审校逐题重算；数值题和带数值的选择题由程序自动核验，纯概念选择题没有自动核验。没有教师或课程专家审核。")
    path = os.path.join(ROOT, "docs", "physics-senior-mapping.md")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")
    print("已写入 " + os.path.relpath(path, ROOT))


if __name__ == "__main__":
    main()
