#!/usr/bin/env python3
"""检查带 figure 的题目：SVG 能解析，不引用外网，图形选项没有把名称写进图里。

用法：python3 scripts/check_figures.py
"""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUESTIONS_PATH = os.path.join(ROOT, "data", "questions.json")

_BAD_TAGS = {"script", "foreignobject", "image", "iframe", "embed", "object", "audio", "video", "link", "use"}
_NS_OK = (
    'xmlns="http://www.w3.org/2000/svg"',
    "xmlns='http://www.w3.org/2000/svg'",
)


def figure_problems(svg, where):
    """返回错误列表。空列表表示这张图可以放进页面。"""
    if not isinstance(svg, str) or not svg.strip():
        return ["%s 的图是空的" % where]
    probe = svg
    for ns in _NS_OK:
        probe = probe.replace(ns, "")
    if re.search(r"https?://", probe, re.I):
        return ["%s 的图引用了外网地址" % where]
    try:
        root = ET.fromstring(svg)
    except ET.ParseError as ex:
        return ["%s 的图不是合法 SVG：%s" % (where, ex)]
    errs = []
    if root.tag.split("}")[-1] != "svg":
        errs.append("%s 的图根节点不是 svg" % where)
    if not (root.attrib.get("viewBox") or "").strip():
        errs.append("%s 的图缺少 viewBox" % where)
    for el in root.iter():
        tag = el.tag.split("}")[-1]
        if tag.lower() in _BAD_TAGS:
            errs.append("%s 的图含有不允许的 <%s>" % (where, tag))
        for key, val in el.attrib.items():
            name = key.split("}")[-1].lower()
            text = str(val)
            if name in ("href", "src") and text and not text.startswith("#"):
                errs.append("%s 的图有外部引用" % where)
            if re.search(r"url\(\s*(?!#)", text, re.I):
                errs.append("%s 的图使用了不是页内片段的 url()" % where)
    return errs


def question_figure_problems(q):
    if not isinstance(q, dict):
        return []
    where = q.get("id") or "题目"
    errs = []
    if "figure" in q:
        errs.extend(figure_problems(q.get("figure"), where))
    choices = q.get("choices") if isinstance(q.get("choices"), list) else []
    if "hideChoiceText" in q:
        if q.get("hideChoiceText") is not True:
            errs.append("%s 的 hideChoiceText 只能是 true" % where)
        elif q.get("type") != "choice":
            errs.append("%s 不是选择题，不能隐藏选项文字" % where)
        elif not choices or not all(
            isinstance(c, dict) and isinstance(c.get("figure"), str) and c.get("figure").strip()
            for c in choices
        ):
            errs.append("%s 隐藏选项文字时，每个选项都要有图" % where)
        else:
            for c in choices:
                if c.get("text") and c["text"] in c["figure"]:
                    errs.append("%s 选项 %s 的图里写出了名称「%s」" % (where, c.get("key"), c["text"]))
    for c in choices:
        if isinstance(c, dict) and "figure" in c:
            errs.extend(figure_problems(c.get("figure"), "%s 选项 %s" % (where, c.get("key"))))
    return errs


def main():
    with open(QUESTIONS_PATH, encoding="utf-8") as f:
        questions = json.load(f)
    errs = []
    n = 0
    for q in questions:
        if not isinstance(q, dict):
            continue
        has = "figure" in q or "hideChoiceText" in q or any(
            isinstance(c, dict) and "figure" in c for c in (q.get("choices") or []) if isinstance(q.get("choices"), list)
        )
        if not has:
            continue
        n += 1
        errs.extend(question_figure_problems(q))
    if errs:
        print("图示检查失败，共 %d 条：" % len(errs))
        for line in errs[:40]:
            print("  " + line)
        if len(errs) > 40:
            print("  ……另有 %d 条" % (len(errs) - 40))
        return 1
    print("图示检查通过：%d 道题带图，SVG 可解析，没有外网引用" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
