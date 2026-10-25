# -*- coding: utf-8 -*-
"""小学英语知识点的薄封装。各册脚本只负责内容。"""
from en_lib import vocab, sound, four, C, N

_CRIT = {
    "语音": ["能根据字母或读音选出正确的一项", "能把字母、发音和例词对上"],
    "词汇": ["能选出单词的中文意思", "能根据中文选出英文单词"],
    "语法": ["能选出语法正确的词或句子", "能在句子里用对这个句型"],
    "日常表达": ["能选出符合情境的英文句子", "能读懂这个功能句在问什么或在说什么"],
    "读写": ["能根据短文选出与文字一致的信息", "能选出和短文意思一致的句子"],
}


def V(key, name, g, s, u, desc, words, std=None):
    if std is None:
        std = "vocab34" if g <= 4 else "vocab56"
    vocab(key, name, g, s, u, desc, _CRIT["词汇"], words, std)


def S(key, name, g, s, u, desc, sound_name, goods, bads, std, mode="vowel"):
    sound(key, name, g, s, u, desc, _CRIT["语音"], std, sound_name, goods, bads, mode)


def X(key, name, domain, g, s, u, typ, desc, std, qs, conf="inferred", note=None):
    items = []
    for q in qs:
        if q[0] == "n":
            items.append(N(q[1], q[2], q[3]))
        else:
            items.append(C(q[1], q[2], q[3], q[4]))
    four(key, name, domain, g, s, u, typ, desc, _CRIT[domain], std, items, conf, note)


def P(key, name, g, s, u, desc, std, qs, conf="exact"):
    X(key, name, "语音", g, s, u, "procedural", desc, std, qs, conf)


def G(key, name, g, s, u, desc, std, qs):
    X(key, name, "语法", g, s, u, "procedural", desc, std, qs, "exact")


def F(key, name, g, s, u, desc, std, qs):
    X(key, name, "日常表达", g, s, u, "application", desc, std, qs)


def R(key, name, g, s, u, desc, std, qs):
    X(key, name, "读写", g, s, u, "application", desc, std, qs)
