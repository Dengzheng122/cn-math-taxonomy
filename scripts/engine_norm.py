"""short 题比较用的最小规范化（与 diagnose/engine.js 的 normalizeText 思路一致，仅用于第二遍复核的粗比较）。"""
import re
import unicodedata


def norm_text(s):
    s = unicodedata.normalize("NFKC", str(s))
    s = s.replace("²", "^2").replace("³", "^3").replace("−", "-")
    s = re.sub(r"\s+", "", s).lower()
    s = re.sub(r"^(答案|答)[:=]", "", s)
    return s.rstrip(".。!")
