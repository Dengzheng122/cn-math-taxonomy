"""高中物理草稿用的登记函数。章节、名称、年级册次全部来自 phy_hs_plan.py；草稿里只写内容。

T(key, domain, typ, desc, mastery, std, pre=(), math=(), qs=(), root=None)
  key    phy_hs_plan.py 里登记的知识点 key
  std    [("B1.1.3", "exact"), ...]  课标条目的 id 尾部（cps-hs-2017: 后面的部分），最多 3 条
  pre    [("velocity", "hard"), ("J:ohm", "soft")]  先修：高中 key 必须排在本知识点之前；"J:" 开头是初中物理 key（phy_g8a/g8b/g9 里的 key）
  math   [("cnm_h012", "一句话说明为什么要用到这个数学点")]  只写 mathLinks，不连先修边
  qs     恰好 4 道题，用 C（选择题）和 N（数值题）
C、N 与初中物理共用（见 phy_lib.py）。
"""
from __future__ import annotations

import hashlib
import json

from phy_lib import C, N, PHY_DOMAINS  # noqa: F401
from phy_hs_plan import PLAN, PLAN_BY_KEY, ORDER, BOOKS  # noqa: F401
import phy_hs_std as S

HS = {}     # key -> 草稿
VALID_STD = {c[0] for c in S.CLAUSES} | {e[0] for e in S.EXPERIMENTS}


def T(key, domain, typ, desc, mastery, std, pre=(), math=(), qs=(), root=None):
    assert key in PLAN_BY_KEY, "phy_hs_plan.py 里没有这个 key：%s" % key
    assert key not in HS, "重复登记：%s" % key
    assert domain in PHY_DOMAINS, (key, domain)
    assert 2 <= len(mastery) <= 3, key
    HS[key] = dict(key=key, domain=domain, type=typ, description=desc, mastery=list(mastery), std=list(std),
                   pre=list(pre), math=list(math), qs=list(qs), root=root)
    return HS[key]


def std_id(tail):
    return "cps-hs-2017:" + tail


def tid_of(key):
    return "cnp_h%03d" % (ORDER[key] + 1)


def _slot(key, i):
    return int(hashlib.md5(("%s#%d" % (key, i)).encode()).hexdigest(), 16) % 4


def compile_questions(key, tid, t, errs):
    out = []
    if len(t["qs"]) != 4:
        errs.append("%s 题数不是 4" % key)
    for i, q in enumerate(t["qs"], 1):
        qid = "%s_q%d" % (tid, i)
        if q["kind"] == "numeric":
            obj = {"id": qid, "topicId": tid, "difficulty": q["diff"], "type": "numeric", "prompt": q["prompt"],
                   "answer": q["answer"], "explanation": q["expl"], "verify": q["verify"]}
            if q.get("percent"):
                obj["percent"] = True
        else:
            texts = list(q["wrongs"])
            if len(set(texts + [q["right"]])) != len(texts) + 1:
                errs.append("%s 选项重复" % qid)
            pos = q["pos"] if q["pos"] is not None else _slot(key, i) % (len(texts) + 1)
            texts.insert(pos, q["right"])
            keys = "ABCD"
            obj = {"id": qid, "topicId": tid, "difficulty": q["diff"], "type": "choice", "prompt": q["prompt"],
                   "choices": [{"key": keys[j], "text": x} for j, x in enumerate(texts)],
                   "answer": keys[pos], "explanation": q["expl"],
                   "verify": q["verify"] if q["verify"] else json.dumps(q["right"], ensure_ascii=False)}
        if q.get("figure"):
            obj["figure"] = q["figure"]
        out.append(obj)
    return out
