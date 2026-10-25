"""初中物理（人教版 2024/2025 新版）草稿用的小工具：知识点、题目和先修都在 phy_g8a/phy_g8b/phy_g9 里登记。"""
from __future__ import annotations

TOPICS = []          # 按教材目录顺序
_BY_KEY = {}

PHY_DOMAINS = ("物质", "运动和相互作用", "能量", "跨学科实践")
# 物理选择题选项里允许出现的单位（核验时把「数值 + 单位」当成数值比较）
UNITS = ("m/s", "km/h", "kg/m³", "g/cm³", "kg", "g", "t", "mg", "m³", "cm³", "dm³", "mL", "L",
         "m", "cm", "mm", "km", "μm", "nm", "s", "min", "h", "N", "Pa", "kPa", "J", "kJ", "W", "kW",
         "kW·h", "V", "kV", "mV", "A", "mA", "Ω", "kΩ", "℃", "Hz", "dB", "%", "J/(kg·℃)", "J/kg", "N/kg", "m²", "cm²")


def T(key, sec, name, domain, typ, desc, mastery, std, pre=(), math=(), qs=(), root=None, figure_note=None):
    assert key not in _BY_KEY, key
    assert domain in PHY_DOMAINS, (key, domain)
    assert 2 <= len(mastery) <= 3, key
    t = dict(key=key, sec=sec, name=name, domain=domain, type=typ, description=desc, mastery=list(mastery),
             std=list(std), pre=list(pre), math=list(math), qs=list(qs), root=root)
    TOPICS.append(t)
    _BY_KEY[key] = t
    return t


def C(diff, prompt, right, wrongs, expl, verify=None, figure=None, pos=None):
    """选择题：right 是正确选项文字，wrongs 是 2–3 个常见错误。verify 不写时用正确选项文字本身。"""
    return dict(kind="choice", diff=diff, prompt=prompt, right=right, wrongs=list(wrongs), expl=expl,
                verify=verify, figure=figure, pos=pos)


def N(diff, prompt, answer, expl, verify, figure=None, percent=False):
    """数值题：answer 是不带单位的数（单位写在题干里）。verify 是能算出这个数的表达式。"""
    return dict(kind="numeric", diff=diff, prompt=prompt, answer=str(answer), expl=expl, verify=verify, figure=figure,
                percent=percent)
