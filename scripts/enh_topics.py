# -*- coding: utf-8 -*-
"""按教学顺序登记高中英语知识点。顺序就是软先修的主干。"""
from en_lib import TOPICS
import enh_b1
import enh_b2
import enh_b3
import enh_s1
import enh_s2
import enh_s3
import enh_s4
import enh_edges  # noqa: F401

enh_b1.load()
enh_b2.load()
enh_b3.load()
enh_s1.load()
enh_s2.load()
enh_s3.load()
enh_s4.load()

if TOPICS[0]["key"] != "gr_sentmem":
    raise SystemExit("高中英语必须从句子成分 gr_sentmem 开始")
if not (220 <= len(TOPICS) <= 320):
    raise SystemExit("高中英语知识点 %d 不在 220–320" % len(TOPICS))
_keys = [t["key"] for t in TOPICS]
if len(_keys) != len(set(_keys)):
    raise SystemExit("高中英语 key 重复")
if not any(t["name"] == "虚拟语气" for t in TOPICS):
    raise SystemExit("缺少名称为「虚拟语气」的知识点")
