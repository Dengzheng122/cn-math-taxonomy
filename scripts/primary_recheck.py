# -*- coding: utf-8 -*-
"""小学题独立复核：只读题干和选项，不读 answer / verify / explanation。

数值题一律在题干里带「计算：……＝？」，这里用自己的分数递归下降解析器重算。
选择题能从题干算出得数的，按得数对选项；其余靠下面的事实规则（与出题脚本分开写）。
"""
import re
from fractions import Fraction


class ParseError(Exception):
    pass


def eval_zh(src):
    s = (src.replace("＋", "+").replace("－", "-").replace("−", "-")
           .replace("×", "*").replace("÷", "/").replace("（", "(").replace("）", ")")
           .replace(" ", ""))
    p = _P(s)
    v = p.expr()
    if p.i != len(p.s):
        raise ParseError("未能吃完：%s" % src)
    return v


class _P:
    def __init__(self, s):
        self.s = s
        self.i = 0

    def peek(self):
        return self.s[self.i] if self.i < len(self.s) else ""

    def eat(self, c):
        if self.peek() != c:
            raise ParseError("期望 %s，得到 %s" % (c, self.peek()))
        self.i += 1

    def expr(self):
        v = self.term()
        while self.peek() in ("+", "-"):
            op = self.peek()
            self.i += 1
            r = self.term()
            v = v + r if op == "+" else v - r
        return v

    def term(self):
        v = self.unary()
        while self.peek() in ("*", "/"):
            op = self.peek()
            self.i += 1
            r = self.unary()
            if op == "/" and r == 0:
                raise ParseError("除以 0")
            v = v * r if op == "*" else v / r
        return v

    def unary(self):
        if self.peek() == "-":
            self.i += 1
            return -self.unary()
        if self.peek() == "+":
            self.i += 1
            return self.unary()
        return self.primary()

    def primary(self):
        if self.peek() == "(":
            self.eat("(")
            v = self.expr()
            self.eat(")")
            return v
        return self.number()

    def number(self):
        start = self.i
        if self.peek() == ".":
            raise ParseError("小数点开头")
        while self.peek().isdigit():
            self.i += 1
        if self.peek() == ".":
            self.i += 1
            if not self.peek().isdigit():
                raise ParseError("小数点后没有数字")
            while self.peek().isdigit():
                self.i += 1
        if self.i == start:
            raise ParseError("不是数字：%s" % self.peek())
        return Fraction(self.s[start:self.i])


_CALC = re.compile(r"计算：(.+?)＝？")


def _nums_in_calc(prompt):
    m = _CALC.search(prompt)
    if not m:
        return None
    expr = m.group(1)
    # 多个算式用顿号或分号隔开时，逐个算
    parts = re.split(r"[、；]", expr)
    vals = [eval_zh(p) for p in parts if p.strip()]
    return vals[0] if len(vals) == 1 else vals


def _fmt_one(v, as_decimal=False):
    if isinstance(v, float):
        v = Fraction(v).limit_denominator(10 ** 9)
    if not isinstance(v, Fraction):
        v = Fraction(v)
    if v.denominator == 1:
        return str(v.numerator)
    if as_decimal:
        sign = "-" if v < 0 else ""
        v = abs(v)
        for k in range(1, 7):
            scaled = v * (10 ** k)
            if scaled.denominator == 1:
                digits = scaled.numerator
                whole = digits // (10 ** k)
                rest = digits % (10 ** k)
                frac = str(rest).zfill(k).rstrip("0")
                return sign + str(whole) + "." + frac
        raise ParseError("不是有限小数：%s" % v)
    return "%d/%d" % (v.numerator, v.denominator)


def fmt_value(v, as_decimal=False):
    if isinstance(v, (list, tuple)):
        return "，".join(_fmt_one(x, as_decimal) for x in v)
    return _fmt_one(v, as_decimal)


def _I(m, i):
    return int(m.group(i))


# 题干本身不把得数写出来。顺序：先特殊问法，再「商和余数」，再「计算：」。
_SPECIAL = [
    (r"(\d+) 的后面一个数是几？", lambda m: _I(m, 1) + 1),
    (r"(\d+) 的前面一个数是几？", lambda m: _I(m, 1) - 1),
    (r"十位上是 (\d+)、个位上是 (\d+)，这个两位数是多少？", lambda m: _I(m, 1) * 10 + _I(m, 2)),
    (r"(\d+) 的个位是几？", lambda m: _I(m, 1) % 10),
    (r"(\d+) 的十位是几？", lambda m: _I(m, 1) // 10 % 10),
    (r"(\d+) 的百位是几？", lambda m: _I(m, 1) // 100 % 10),
    (r"(\d+) 的千位是几？", lambda m: _I(m, 1) // 1000 % 10),
    (r"(\d+) 里面有几个十？", lambda m: _I(m, 1) // 10),
    (r"(\d+) 里面有几个百？", lambda m: _I(m, 1) // 100),
    (r"(\d+) 里面有几个千？", lambda m: _I(m, 1) // 1000),
    (r"(\d+) 米是多少厘米？", lambda m: _I(m, 1) * 100),
    (r"(\d+) 厘米是多少毫米？", lambda m: _I(m, 1) * 10),
    (r"(\d+) 分米是多少厘米？", lambda m: _I(m, 1) * 10),
    (r"(\d+) 千米是多少米？", lambda m: _I(m, 1) * 1000),
    (r"(\d+) 千克是多少克？", lambda m: _I(m, 1) * 1000),
    (r"(\d+) 吨是多少千克？", lambda m: _I(m, 1) * 1000),
    (r"(\d+) 时是多少分？", lambda m: _I(m, 1) * 60),
    (r"(\d+) 分是多少秒？", lambda m: _I(m, 1) * 60),
    (r"(\d+) 元是多少角？", lambda m: _I(m, 1) * 10),
    (r"(\d+) 角是多少分？", lambda m: _I(m, 1) * 10),
    (r"(\d+) 平方米是多少平方分米？", lambda m: _I(m, 1) * 100),
    (r"(\d+) 公顷是多少平方米？", lambda m: _I(m, 1) * 10000),
    (r"长 (\d+) 厘米、宽 (\d+) 厘米的长方形，周长是多少厘米？", lambda m: 2 * (_I(m, 1) + _I(m, 2))),
    (r"长 (\d+) 厘米、宽 (\d+) 厘米的长方形，面积是多少平方厘米？", lambda m: _I(m, 1) * _I(m, 2)),
    (r"边长 (\d+) 厘米的正方形，周长是多少厘米？", lambda m: 4 * _I(m, 1)),
    (r"边长 (\d+) 厘米的正方形，面积是多少平方厘米？", lambda m: _I(m, 1) ** 2),
    (r"底 (\d+) 厘米、高 (\d+) 厘米的平行四边形，面积是多少平方厘米？", lambda m: _I(m, 1) * _I(m, 2)),
    (r"底 (\d+) 厘米、高 (\d+) 厘米的三角形，面积是多少平方厘米？", lambda m: Fraction(_I(m, 1) * _I(m, 2), 2)),
    (r"上底 (\d+) 厘米、下底 (\d+) 厘米、高 (\d+) 厘米的梯形，面积是多少平方厘米？",
     lambda m: Fraction((_I(m, 1) + _I(m, 2)) * _I(m, 3), 2)),
    (r"长 (\d+) 厘米、宽 (\d+) 厘米、高 (\d+) 厘米的长方体，体积是多少立方厘米？",
     lambda m: _I(m, 1) * _I(m, 2) * _I(m, 3)),
    (r"棱长 (\d+) 厘米的正方体，体积是多少立方厘米？", lambda m: _I(m, 1) ** 3),
    (r"半径 (\d+) 厘米的圆，周长是多少厘米？圆周率按 314/100。", lambda m: Fraction(2 * 314 * _I(m, 1), 100)),
    (r"半径 (\d+) 厘米的圆，面积是多少平方厘米？圆周率按 314/100。", lambda m: Fraction(314 * _I(m, 1) * _I(m, 1), 100)),
    (r"底面半径 (\d+) 厘米、高 (\d+) 厘米的圆柱，体积是多少立方厘米？圆周率按 314/100。",
     lambda m: Fraction(314 * _I(m, 1) * _I(m, 1) * _I(m, 2), 100)),
    (r"一组数 (\d+)、(\d+)、(\d+) 的平均数是多少？", lambda m: Fraction(_I(m, 1) + _I(m, 2) + _I(m, 3), 3)),
    (r"原价 (\d+) 元，打 (\d+) 折后是多少元？", lambda m: Fraction(_I(m, 1) * _I(m, 2), 10)),
    (r"(\d+) 的 (\d+)% 是多少？", lambda m: Fraction(_I(m, 1) * _I(m, 2), 100)),
    (r"比 (\d+)：(\d+) 化成最简整数比后，前项是多少？", lambda m: _I(m, 1) // math_gcd(_I(m, 1), _I(m, 2))),
    (r"(\d+)：(\d+) 的比值是多少？", lambda m: Fraction(_I(m, 1), _I(m, 2))),
]


def math_gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def expected_numeric(prompt):
    """返回与题库 answer 同格式的字符串；解不了则返回 None。"""
    for cre, fn in _SPECIAL:
        m = re.search(cre, prompt)
        if m:
            v = fn(m)
            as_dec = ("用小数作答" in prompt) or (isinstance(v, Fraction) and v.denominator not in (1,) and "." in prompt and "314/100" in prompt)
            if "314/100" in prompt:
                as_dec = True
            if "平均数" in prompt and isinstance(v, Fraction) and v.denominator != 1:
                as_dec = False
            return fmt_value(v, as_decimal=as_dec)
    m = re.search(r"商和余数：(\d+)÷(\d+)", prompt)
    if m:
        a, b = int(m.group(1)), int(m.group(2))
        if b == 0:
            raise ParseError("除数是 0")
        return "%d，%d" % (a // b, a % b)
    v = _nums_in_calc(prompt)
    if v is None:
        return None
    return fmt_value(v, as_decimal=("用小数作答" in prompt) or _expr_has_dot(prompt))


def _expr_has_dot(prompt):
    m = _CALC.search(prompt)
    return bool(m and "." in m.group(1))


# 选择题：返回应当选中的选项文字。规则按数学事实写，不读取答案字段。
def expected_choice_text(prompt, texts):
    m = re.search(r"计算：(.+?)＝？", prompt)
    if m:
        val = fmt_value(eval_zh(m.group(1)))
        hits = [t for t in texts if _same_num(t, val)]
        if len(hits) == 1:
            return hits[0]
    m = re.match(r"^(.+?) 的得数是哪一个？$", prompt)
    if m:
        val = fmt_value(eval_zh(m.group(1)))
        hits = [t for t in texts if _same_num(t, val)]
        if len(hits) == 1:
            return hits[0]
    for pred, text in _FACTS:
        if pred(prompt):
            if text not in texts:
                raise ParseError("事实规则给出的文字不在选项里：%s / %s" % (text, texts))
            return text
    return None


def _same_num(text, val):
    t = text.strip().replace(" ", "")
    if not re.match(r"^-?\d+(?:\.\d+)?(?:/\d+)?$", t):
        return False
    return Fraction(t) == Fraction(val)


def _has(s):
    return lambda p, s=s: s in p


# (谓词, 正确选项的全文)。选项文字必须和出题时一致。
_FACTS = [
    (_has("0 是哪种数"), "既不是正数，也不是负数"),
    (_has("下面哪一个是长方体"), "长方体"),
    (_has("下面哪一个是圆柱"), "圆柱"),
    (_has("球滚起来最容易"), "球"),
    (_has("下面哪一个是正方形"), "正方形"),
    (_has("下面哪一个是三角形"), "三角形"),
    (_has("长方形有几条边"), "4条"),
    (_has("正方形的四条边"), "四条边都相等"),
    (_has("加法是把两部分"), "把两部分合起来"),
    (_has("减法是求"), "从总数里去掉一部分，求剩下的"),
    (_has("乘法表示的是"), "求几个相同加数的和"),
    (_has("除法表示的是"), "把总数平均分成几份，求每一份"),
    (_has("有余数的除法里，余数和除数"), "余数比除数小"),
    (_has("小括号要"), "先算小括号里面的"),
    (_has("先乘除、后加减"), "先算乘除，再算加减"),
    (_has("1 厘米大约有多长"), "指甲盖的宽度大约是 1 厘米"),
    (_has("1 米等于多少厘米"), "100厘米"),
    (_has("人民币 1 元等于"), "10角"),
    (_has("钟面上分针走一圈是"), "60分"),
    (_has("1 时等于多少分"), "60分"),
    (_has("平年的 2 月有几天"), "28天"),
    (_has("闰年的 2 月有几天"), "29天"),
    (_has("一年有几个月"), "12个月"),
    (_has("东和西是"), "相反的方向"),
    (_has("地图上通常是"), "上北下南，左西右东"),
    (_has("直角比锐角"), "直角比锐角大"),
    (_has("钝角比直角"), "钝角比直角大"),
    (_has("同一平面内，不相交的两条直线"), "互相平行"),
    (_has("两条直线相交成直角"), "互相垂直"),
    (_has("三角形内角和是"), "180度"),
    (_has("任意两边之和"), "大于第三边"),
    (_has("长方形的对边"), "对边相等"),
    (_has("平行四边形的对边"), "对边平行且相等"),
    (_has("梯形只有"), "一组对边平行"),
    (_has("轴对称图形有"), "对称轴"),
    (_has("平移之后，图形的大小"), "大小和形状都不变"),
    (_has("旋转之后，图形的大小"), "大小和形状都不变"),
    (_has("质数的因数"), "只有 1 和它本身"),
    (_has("1 是质数还是合数"), "1 既不是质数也不是合数"),
    (_has("偶数的个位"), "0、2、4、6 或 8"),
    (_has("一个数的个位是 0 或 5"), "是 5 的倍数"),
    (_has("分数的分母表示"), "把整体平均分成了几份"),
    (_has("分子比分母小的分数"), "真分数"),
    (_has("百分数表示"), "一个数是另一个数的百分之几"),
    (_has("比的前项除以后项"), "比值"),
    (_has("比例的两项外项之积"), "等于两项内项之积"),
    (_has("成正比例的两种量"), "比值一定"),
    (_has("成反比例的两种量"), "乘积一定"),
    (_has("负数表示的是"), "与正数意义相反的量"),
    (_has("温度零下用"), "负数表示"),
    (_has("条形统计图适合看"), "数量的多少"),
    (_has("折线统计图适合看"), "数量的变化"),
    (_has("扇形统计图适合看"), "各部分占总数的多少"),
    (_has("平均数表示的是"), "一组数的平均水平"),
    (_has("可能性相等时"), "每种结果的机会一样大"),
    (_has("一定发生的事情"), "可能性是确定的，一定会发生"),
    (_has("不可能发生的事情"), "不会发生"),
    (_has("圆上的点到圆心"), "距离都等于半径"),
    (_has("圆周率大约是"), "3.14"),
    (_has("长方体有几个面"), "6个"),
    (_has("正方体的每条棱"), "一样长"),
    (_has("圆柱的两个底面"), "是完全相同的圆"),
    (_has("圆锥的底面"), "是一个圆"),
    (_has("从正面、侧面、上面看"), "看到的形状可能不一样"),
    (_has("有序数对先写"), "先写列，再写行"),
    (_has("折扣里的八折是"), "原价的 80%"),
    (_has("方程两边同时加上"), "相等关系不变"),
    (_has("用字母表示数时，字母表示"), "一个可以变化的数"),
    (_has("分类要先定"), "分类标准"),
    (_has("第几是看"), "顺序，从 1 开始数"),
    (_has("0 表示一个也没有"), "一个也没有"),
    (_has("凑十法是先"), "先把一个数凑成 10"),
    (_has("破十法是先"), "先把十几分成 10 和几"),
    (_has("个位满十要"), "向十位进 1"),
    (_has("退位减法要向"), "向十位借 1 当 10"),
    (_has("估算是为了"), "很快知道大约是多少"),
    (_has("验算加法可以用"), "用减法把和减去一个加数"),
    (_has("面积要用"), "面积单位"),
    (_has("周长是"), "图形一周边线的长度"),
    (_has("体积要用"), "体积单位"),
    (_has("1 千米等于"), "1000米"),
    (_has("1 千克等于"), "1000克"),
    (_has("1 吨等于"), "1000千克"),
    (_has("公顷是"), "面积单位"),
    (_has("比例尺是"), "图上距离与实际距离的比"),
    (_has("集合图里两边都有的"), "两个圈重叠的部分"),
    (_has("鸡兔同笼用的是"), "假设全部是鸡，再调整"),
    (_has("植树问题要先分清"), "两端都种、还是只种一端"),
    (_has("找次品时每次要"), "把物品分成三份来称"),
    (_has("鸽巢问题是说"), "物体数比抽屉数多，必有一个抽屉至少放两个"),
    (_has("数字编码是为了"), "用数字表示事物，方便区分"),
    (_has("优化问题要"), "把几件事安排得更节省"),
    (_has("搭配时交换顺序"), "如果顺序不同算不同，就要分开数"),
]


def solve_question(q):
    """返回 (kind, value)。kind 为 'numeric' 或 'choice'。解不了抛错。"""
    if q["type"] == "numeric":
        got = expected_numeric(q["prompt"])
        if got is None:
            raise ParseError("数值题里没有可计算的「计算：」：" + q["prompt"][:80])
        return got
    if q["type"] == "choice":
        texts = [c["text"].strip() for c in q["choices"]]
        text = expected_choice_text(q["prompt"], texts)
        if text is None:
            raise ParseError("选择题无法独立求解：" + q["prompt"][:80])
        for c in q["choices"]:
            if c["text"].strip() == text:
                return c["key"]
        raise ParseError("选项缺失")
    raise ParseError("不支持的题型 " + q.get("type", ""))
