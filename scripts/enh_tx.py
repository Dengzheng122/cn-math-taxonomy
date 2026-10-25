# -*- coding: utf-8 -*-
"""高中英语知识点登记。各册脚本只负责内容，编译由 enh_build.py 完成。"""
from en_lib import vocab, four, C

_CRIT = {
    "语音": ["能根据重音、语调或音变选出正确的一项", "能说明这个朗读规则用在什么地方"],
    "词汇": ["能选出单词或短语的中文意思", "能根据中文选出英文单词或短语"],
    "语法": ["能选出语法正确的词或句子", "能说明这个结构在句中做什么"],
    "日常表达": ["能选出符合情境的英文句子", "能读懂这个功能句在问什么或在说什么"],
    "读写": ["能根据短文选出与文字一致的信息", "能选出和写作要点一致的句子"],
}


def q(prompt, answer, w1, w2, w3, expl):
    return (prompt, answer, [w1, w2, w3], expl)


def V(key, name, grade, unit, desc, words, std):
    vocab(
        key, name, grade, "上", unit, desc, _CRIT["词汇"], words, std,
    )


def X(key, name, domain, grade, unit, typ, desc, std, rows, conf):
    if len(rows) != 4:
        raise SystemExit("%s 需要恰好 4 题，现在 %d" % (key, len(rows)))
    items = [C(r[0], r[1], r[2], r[3]) for r in rows]
    four(key, name, domain, grade, "上", unit, typ, desc, _CRIT[domain], std, items, conf)


def P(key, name, grade, unit, desc, std, rows):
    X(key, name, "语音", grade, unit, "procedural", desc, std, rows, "inferred")


def G(key, name, grade, unit, desc, std, rows, conf="exact"):
    X(key, name, "语法", grade, unit, "procedural", desc, std, rows, conf)


def F(key, name, grade, unit, desc, std, rows):
    X(key, name, "日常表达", grade, unit, "application", desc, std, rows, "inferred")


def R(key, name, grade, unit, desc, std, rows):
    X(key, name, "读写", grade, unit, "application", desc, std, rows, "inferred")
