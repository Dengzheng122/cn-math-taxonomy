# -*- coding: utf-8 -*-
"""小学题生成。题干里的算式会由 primary_recheck 再算一遍，这里不把答案写死进题干以外的隐藏字段。"""
from fractions import Fraction


def ask(prompt, py, diff, expl):
    """题干用独立复核能识别的问法，verify 用等价的 Python 表达式。"""
    return {"difficulty": diff, "type": "numeric", "prompt": prompt, "verify": py, "explanation": expl}


def calc(py, zh, diff, expl, decimal=False):
    prompt = "计算：%s＝？" % zh
    if decimal:
        prompt += "（用小数作答）"
    return {"difficulty": diff, "type": "numeric", "prompt": prompt, "verify": py, "explanation": expl}


def story(prefix, py, zh, diff, expl, decimal=False):
    prompt = prefix + "计算：%s＝？" % zh
    if decimal:
        prompt += "（用小数作答）"
    return {"difficulty": diff, "type": "numeric", "prompt": prompt, "verify": py, "explanation": expl}


def rem(a, b, diff, expl, prefix=""):
    prompt = prefix + "先写商，再写余数。商和余数：%d÷%d" % (a, b)
    return {"difficulty": diff, "type": "numeric", "prompt": prompt,
            "verify": "(%d//%d, %d%%%d)" % (a, b, a, b), "explanation": expl}


def choice_num(zh, py, wrongs, diff, expl):
    """选项是得数。wrongs 是字符串，不能和正确得数相同。"""
    return {"difficulty": diff, "type": "choice",
            "prompt": "%s 的得数是哪一个？" % zh,
            "wrongs": list(wrongs), "verify": py, "explanation": expl, "_numchoice": True}


def fact(prompt, options, correct, expl, diff="basic"):
    if correct not in options:
        raise ValueError("正确项不在选项里：%s" % prompt)
    if len(options) not in (3, 4) or len(set(options)) != len(options):
        raise ValueError("选项不合法：%s" % prompt)
    keys = "ABCD"
    return {"difficulty": diff, "type": "choice", "prompt": prompt,
            "choices": [{"key": keys[i], "text": t} for i, t in enumerate(options)],
            "verify": repr(correct), "explanation": expl}


def add4(pairs, thing="苹果", unit="个"):
    """pairs 四个 (a,b)，都是非负整数，和不超过题目要求的范围。"""
    (a, b), (c, d), (e, f), (g, h) = pairs
    return [
        calc("%d+%d" % (a, b), "%d＋%d" % (a, b), "basic", "%d＋%d＝%d。" % (a, b, a + b)),
        calc("%d+%d" % (c, d), "%d＋%d" % (c, d), "basic", "%d＋%d＝%d。" % (c, d, c + d)),
        story("有 %d %s%s，又放进来 %d %s。一共有多少%s？" % (e, unit, thing, f, unit, unit),
              "%d+%d" % (e, f), "%d＋%d" % (e, f), "standard",
              "把两部分合起来，%d＋%d＝%d。" % (e, f, e + f)),
        choice_num("%d＋%d" % (g, h), "%d+%d" % (g, h),
                   [str(g + h + 1), str(max(g + h - 1, 0)), str(g + h + 2)],
                   "standard", "%d＋%d＝%d。" % (g, h, g + h)),
    ]


def sub4(pairs, thing="苹果", unit="个"):
    (a, b), (c, d), (e, f), (g, h) = pairs
    for x, y in pairs:
        if x < y:
            raise ValueError("减法被减数不能更小：%s-%s" % (x, y))
    return [
        calc("%d-%d" % (a, b), "%d－%d" % (a, b), "basic", "%d－%d＝%d。" % (a, b, a - b)),
        calc("%d-%d" % (c, d), "%d－%d" % (c, d), "basic", "%d－%d＝%d。" % (c, d, c - d)),
        story("有 %d %s%s，拿走 %d %s。还剩多少%s？" % (e, unit, thing, f, unit, unit),
              "%d-%d" % (e, f), "%d－%d" % (e, f), "standard",
              "从总数里去掉一部分，%d－%d＝%d。" % (e, f, e - f)),
        choice_num("%d－%d" % (g, h), "%d-%d" % (g, h),
                   [str(g - h + 1), str(g - h + 2), str(abs(g - h - 1))],
                   "standard", "%d－%d＝%d。" % (g, h, g - h)),
    ]


def mul4(pairs, thing="铅笔", unit="支"):
    (a, b), (c, d), (e, f), (g, h) = pairs
    return [
        calc("%d*%d" % (a, b), "%d×%d" % (a, b), "basic", "%d×%d＝%d。" % (a, b, a * b)),
        calc("%d*%d" % (c, d), "%d×%d" % (c, d), "basic", "%d×%d＝%d。" % (c, d, c * d)),
        story("每盒有 %d %s%s，一共 %d 盒。一共有多少%s？" % (e, unit, thing, f, unit),
              "%d*%d" % (e, f), "%d×%d" % (e, f), "standard",
              "求 %d 个 %d 的和，用乘法，%d×%d＝%d。" % (f, e, e, f, e * f)),
        choice_num("%d×%d" % (g, h), "%d*%d" % (g, h),
                   [str(g * h + g), str(g * h + 1), str(g + h)],
                   "standard", "%d×%d＝%d。" % (g, h, g * h)),
    ]


def div4(pairs, thing="糖", unit="颗"):
    (a, b), (c, d), (e, f), (g, h) = pairs
    for x, y in pairs:
        if y == 0 or x % y:
            raise ValueError("除法要整除：%s/%s" % (x, y))
    return [
        calc("%d/%d" % (a, b), "%d÷%d" % (a, b), "basic", "%d÷%d＝%d。" % (a, b, a // b)),
        calc("%d/%d" % (c, d), "%d÷%d" % (c, d), "basic", "%d÷%d＝%d。" % (c, d, c // d)),
        story("%d %s%s，平均分成 %d 份。每份有多少%s？" % (e, unit, thing, f, unit),
              "%d/%d" % (e, f), "%d÷%d" % (e, f), "standard",
              "%d÷%d＝%d。" % (e, f, e // f)),
        choice_num("%d÷%d" % (g, h), "%d/%d" % (g, h),
                   [str(g // h + 1), str(g // h + 2), str(max(g // h - 1, 0))],
                   "standard", "%d÷%d＝%d。" % (g, h, g // h)),
    ]


def expr4(items):
    """items: 4 个 (py, zh, diff, expl, prefix可选, decimal可选)。diff 必须两道 basic、两道 standard，且第一道 basic。"""
    out = []
    for it in items:
        py, zh, diff, expl = it[:4]
        prefix = it[4] if len(it) > 4 else ""
        decimal = it[5] if len(it) > 5 else False
        if prefix:
            out.append(story(prefix, py, zh, diff, expl, decimal))
        else:
            out.append(calc(py, zh, diff, expl, decimal))
    return out


def mix_basic_fact(calc_q, fact_q, std1, std2):
    """q1 数值 basic，q2 选择 basic，q3 q4 standard 数值。"""
    calc_q = dict(calc_q, difficulty="basic")
    fact_q = dict(fact_q, difficulty="basic")
    std1 = dict(std1, difficulty="standard")
    std2 = dict(std2, difficulty="standard")
    return [calc_q, fact_q, std1, std2]
