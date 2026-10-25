#!/usr/bin/env python3
"""题库答案自动核验（仅标准库）。

用法：
  python3 scripts/verify_questions.py                       # 核验 data/questions.json，写 data/verification_report.json
  python3 scripts/verify_questions.py --file data/_qbatches/01.json   # 只核验某个批次文件（顺带做格式检查），不写报告
  python3 scripts/verify_questions.py --report out.json     # 指定报告路径

题目的 verify 字段是一个 Python 表达式字符串，在受限环境中求值（AST 白名单：四则、**、//、%、比较、
推导式、元组/列表、下标；没有属性访问、没有 import、没有赋值）。可用名字：
  Fraction sqrt pi e sin cos tan asin acos atan atan2 radians degrees log log10 log2 exp
  factorial comb perm gcd lcm abs round sum min max len sorted range floor ceil isqrt int float
  mean median pvariance variance mode
  solve2(a1,b1,c1,a2,b2,c2) -> (x, y)    解 a1x+b1y=c1, a2x+b2y=c2（精确 Fraction）
  roots2(a,b,c) -> 升序实根列表          判别式是完全平方（有理）时为 Fraction，否则为 float

比较规则：
  numeric：表达式结果（数，或多个答案时为列表/元组）与 answer 比较。结果是 int/Fraction 时精确比较；
           结果是 float 时容差 1e-9（相对/绝对取大者）。answer 多个值时按 unordered 决定是否顺序无关。
  choice ：表达式结果与「正确选项的内容」比较：选项文字可解析为数时按数值比较（同上规则），否则要求
           str(结果) 与选项文字完全相同。另外检查没有第二个选项与它数值相同（避免双解）。
没有 verify 的题计入 unverifiable（由第二遍独立复核覆盖）。
"""
import argparse
import ast
import json
import math
import os
import re
import signal
import statistics
import sys
from collections import Counter
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import validate as V  # noqa: E402

QUESTIONS_PATH = os.path.join(ROOT, "data", "questions.json")
REPORT_PATH = os.path.join(ROOT, "data", "verification_report.json")
SECOND_PASS_LOG = os.path.join(ROOT, "data", "second_pass_log.json")
TOL = 1e-9


# ------------------------------------------------------------ 受限求值

def solve2(a1, b1, c1, a2, b2, c2):
    a1, b1, c1, a2, b2, c2 = [Fraction(v) for v in (a1, b1, c1, a2, b2, c2)]
    det = a1 * b2 - a2 * b1
    if det == 0:
        raise ValueError("方程组无唯一解")
    return ((c1 * b2 - c2 * b1) / det, (a1 * c2 - a2 * c1) / det)


def _rat_sqrt(fr):
    if fr < 0:
        return None
    n, d = fr.numerator, fr.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    return Fraction(rn, rd) if rn * rn == n and rd * rd == d else None


def roots2(a, b, c):
    a, b, c = Fraction(a), Fraction(b), Fraction(c)
    if a == 0:
        raise ValueError("a 不能为 0")
    disc = b * b - 4 * a * c
    if disc < 0:
        return []
    r = _rat_sqrt(disc)
    if r is not None:
        xs = sorted({(-b - r) / (2 * a), (-b + r) / (2 * a)})
        return xs
    s = math.sqrt(float(disc))
    return sorted([(-float(b) - s) / (2 * float(a)), (-float(b) + s) / (2 * float(a))])


def _mode(xs):
    return statistics.mode(xs)


NAMES = {
    "Fraction": Fraction, "sqrt": math.sqrt, "pi": math.pi, "e": math.e,
    "sin": math.sin, "cos": math.cos, "tan": math.tan, "asin": math.asin, "acos": math.acos,
    "atan": math.atan, "atan2": math.atan2, "radians": math.radians, "degrees": math.degrees,
    "log": math.log, "log10": math.log10, "log2": math.log2, "exp": math.exp,
    "factorial": math.factorial, "comb": math.comb, "perm": math.perm, "gcd": math.gcd, "lcm": math.lcm,
    "abs": abs, "round": round, "sum": sum, "min": min, "max": max, "len": len, "sorted": sorted,
    "range": range, "floor": math.floor, "ceil": math.ceil, "isqrt": math.isqrt, "int": int, "float": float,
    "mean": statistics.mean, "median": statistics.median, "pvariance": statistics.pvariance,
    "variance": statistics.variance, "mode": _mode, "solve2": solve2, "roots2": roots2,
}

ALLOWED_NODES = (
    ast.Expression, ast.BinOp, ast.UnaryOp, ast.BoolOp, ast.Compare, ast.IfExp, ast.Call, ast.Name,
    ast.Load, ast.Store, ast.Constant, ast.Tuple, ast.List, ast.Subscript, ast.Slice,
    ast.ListComp, ast.GeneratorExp, ast.comprehension,
    ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod, ast.Pow, ast.USub, ast.UAdd,
    ast.And, ast.Or, ast.Not, ast.Eq, ast.NotEq, ast.Lt, ast.LtE, ast.Gt, ast.GtE,
)


class UnsafeExpression(Exception):
    pass


def _check_ast(tree):
    bound = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.comprehension):
            for n in ast.walk(node.target):
                if isinstance(n, ast.Name):
                    bound.add(n.id)
    for node in ast.walk(tree):
        if not isinstance(node, ALLOWED_NODES):
            raise UnsafeExpression("不允许的语法：%s" % type(node).__name__)
        if isinstance(node, ast.Name) and node.id not in NAMES and node.id not in bound:
            raise UnsafeExpression("不允许的名字：%s" % node.id)
        if isinstance(node, ast.Call) and not isinstance(node.func, ast.Name):
            raise UnsafeExpression("只能直接调用白名单函数")
        if isinstance(node, ast.Call) and node.keywords:
            raise UnsafeExpression("不允许关键字参数")
        if isinstance(node, ast.Constant) and not isinstance(node.value, (int, float, str, bool, type(None))):
            raise UnsafeExpression("不允许的常量")
        if isinstance(node, ast.Constant) and isinstance(node.value, int) and abs(node.value) > 10 ** 12:
            raise UnsafeExpression("整数常量过大")
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Pow):
            r = node.right
            if isinstance(r, ast.Constant) and isinstance(r.value, (int, float)) and abs(r.value) > 400:
                raise UnsafeExpression("指数过大")


class _Timeout(Exception):
    pass


def _alarm(signum, frame):
    raise _Timeout()


def safe_eval(expr):
    if not isinstance(expr, str) or len(expr) > 600:
        raise UnsafeExpression("表达式为空或过长")
    tree = ast.parse(expr.strip(), mode="eval")
    _check_ast(tree)
    code = compile(tree, "<verify>", "eval")
    old = None
    try:
        old = signal.signal(signal.SIGALRM, _alarm)
        signal.alarm(2)
    except (ValueError, AttributeError):
        old = None
    try:
        env = {"__builtins__": {}}
        env.update(NAMES)  # 必须放在 globals：推导式内部作用域看不到 locals
        return eval(code, env)
    finally:
        if old is not None:
            signal.alarm(0)
            signal.signal(signal.SIGALRM, old)


# ------------------------------------------------------------ 比较

def num_equal(expected, got):
    """expected 来自 answer（Fraction），got 来自表达式（int/Fraction/float/bool）。"""
    if isinstance(got, bool):
        return False
    if isinstance(got, (int, Fraction)):
        return Fraction(got) == expected
    if isinstance(got, float):
        if math.isnan(got) or math.isinf(got):
            return False
        return abs(float(expected) - got) <= TOL * max(1.0, abs(got))
    return False


def flatten_result(res):
    if isinstance(res, (list, tuple)):
        return list(res)
    return [res]


def compare_numeric(q, res):
    exp = V.parse_numeric_answer(q["answer"])
    got = flatten_result(res)
    if exp is None:
        return False, "answer 无法解析"
    if len(exp) != len(got):
        return False, "答案个数不同：answer %d 个，verify %d 个" % (len(exp), len(got))
    if q.get("unordered") is True:
        left = list(got)
        for e in exp:
            hit = next((i for i, g in enumerate(left) if num_equal(e, g)), None)
            if hit is None:
                return False, "answer 中的 %s 在 verify 结果里找不到" % e
            left.pop(hit)
        return True, ""
    for e, g in zip(exp, got):
        if not num_equal(e, g):
            return False, "按顺序比较：answer %s ≠ verify %s" % (e, g)
    return True, ""


def choice_text_value(text):
    t = text.strip().replace(" ", "").replace("−", "-")
    return V.parse_numeric_answer(t) if V.NUM_RE.match(t) else None


# 物理选项常写成「数值 + 单位」（如 20 m/s、2.7 g/cm³）。只对 cnp_ 题拆出数值比较，单位必须是下面这些之一；
# 判断双解时数值相同且单位也相同才算重复（2.7 g/cm³ 与 2.7 kg/m³ 是不同选项）。
PHY_UNITS = ("J/(kg·℃)", "kg/m³", "g/cm³", "kW·h", "m/s", "km/h", "N/kg", "J/kg", "kPa", "kW", "kJ", "kV", "kΩ",
             "mV", "mA", "mL", "mg", "mm", "cm³", "dm³", "m³", "cm²", "m²", "cm", "km", "μm", "nm", "min", "Hz", "dB",
             "Pa", "kg", "℃", "Ω", "%", "m", "g", "t", "L", "s", "h", "N", "J", "W", "V", "A", "个", "倍",
             # 高中物理
             "m/s²", "cm/s", "rad/s", "r/min", "r/s", "rad", "°", "N·s", "kg·m/s", "N·m", "N/m", "V/m", "N/C", "C", "μC", "nC",
             "pF", "μF", "mF", "F", "mT", "μT", "T", "Wb", "Ω·m", "mH", "μH", "H", "MHz", "kHz", "GHz", "eV", "keV", "MeV",
             "K", "mol", "J/K", "ms", "μs", "ns", "MW", "MJ", "mW", "kN", "cm/s²", "atm", "mmHg", "MPa", "J/mol", "m/s³",
             "kg·m²", "W/m²", "天", "年", "圈", "次", "匝", "u", "个/s")
_PHY_RE = re.compile(r"^(-?\d+(?:\.\d+)?)\s*(" + "|".join(re.escape(u) for u in PHY_UNITS) + r")$")


def phy_choice_value(text):
    """返回 (Fraction, 单位) 或 None。"""
    m = _PHY_RE.match(text.strip())
    if not m:
        return None
    return Fraction(m.group(1)), m.group(2)


def compare_phy_choice(q, res):
    texts = {c["key"]: c["text"].strip() for c in q["choices"]}
    right = texts[q["answer"]]
    rv = phy_choice_value(right)
    if rv is None or isinstance(res, (str, bool)) or not isinstance(res, (int, float, Fraction)):
        return None
    if not num_equal(rv[0], res):
        return False, "verify 得 %s，但正确选项 %s 的值是 %s" % (res, q["answer"], right)
    dup = [k for k, t in texts.items() if k != q["answer"] and phy_choice_value(t) is not None
           and phy_choice_value(t)[1] == rv[1] and num_equal(phy_choice_value(t)[0], res)]
    if dup:
        return False, "选项 %s 与正确选项数值和单位都相同（双解）" % "、".join(dup)
    return True, ""


def compare_choice(q, res):
    if str(q.get("id", "")).startswith("cnp_"):
        out = compare_phy_choice(q, res)
        if out is not None:
            return out
    texts = {c["key"]: c["text"].strip() for c in q["choices"]}
    right = texts[q["answer"]]
    rv = choice_text_value(right)
    if rv is not None and len(rv) == 1 and isinstance(res, (int, float, Fraction)) and not isinstance(res, bool):
        if not num_equal(rv[0], res):
            return False, "verify 得 %s，但正确选项 %s 的值是 %s" % (res, q["answer"], rv[0])
        dup = [k for k, t in texts.items() if k != q["answer"] and choice_text_value(t) is not None
               and len(choice_text_value(t)) == 1 and num_equal(choice_text_value(t)[0], res)]
        if dup:
            return False, "选项 %s 与正确选项数值相同（双解）" % "、".join(dup)
        return True, ""
    if str(res).strip() == right:
        dup = [k for k, t in texts.items() if k != q["answer"] and t == right]
        return (False, "选项文字重复") if dup else (True, "")
    return False, "verify 得 %r，但正确选项 %s 的文字是 %r" % (res, q["answer"], right)


# ------------------------------------------------------------ 主流程

def verify_all(questions):
    r = {"auto_verified": [], "mismatch": [], "unverifiable": [], "expression_errors": []}
    for q in questions:
        typ = q.get("type")
        expr = q.get("verify")
        if typ not in ("numeric", "choice") or not expr:
            r["unverifiable"].append(q["id"])
            continue
        try:
            res = safe_eval(expr)
        except Exception as ex:  # noqa: BLE001
            r["expression_errors"].append({"id": q["id"], "verify": expr, "error": "%s: %s" % (type(ex).__name__, ex)})
            r["mismatch"].append({"id": q["id"], "type": typ, "answer": q["answer"], "verify": expr,
                                  "detail": "verify 表达式无法求值：%s: %s" % (type(ex).__name__, ex)})
            continue
        ok, detail = compare_numeric(q, res) if typ == "numeric" else compare_choice(q, res)
        if ok:
            r["auto_verified"].append(q["id"])
        else:
            r["mismatch"].append({"id": q["id"], "type": typ, "answer": q["answer"], "verify": expr,
                                  "verify_result": repr(res), "detail": detail})
    return r


def load_second_pass_log():
    if not os.path.exists(SECOND_PASS_LOG):
        return None
    with open(SECOND_PASS_LOG, encoding="utf-8") as f:
        return json.load(f)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", help="只核验这个题库/批次文件")
    ap.add_argument("--report", help="报告输出路径（默认 data/verification_report.json；--file 时默认不写）")
    args = ap.parse_args()

    path = args.file or QUESTIONS_PATH
    with open(path, encoding="utf-8") as f:
        questions = json.load(f)
    with open(os.path.join(ROOT, "data", "topics.json"), encoding="utf-8") as f:
        topics = {t["id"]: t for t in json.load(f)}

    errs, stats = V.question_errors(questions, topics, require_coverage=not args.file)
    if errs:
        print("格式错误 %d 处：" % len(errs))
        for e in errs[:80]:
            print("  - " + e)
        if len(errs) > 80:
            print("  ……另有 %d 处" % (len(errs) - 80))
    questions_ok = [q for q in questions if isinstance(q, dict) and isinstance(q.get("id"), str)
                    and q.get("type") in V.Q_TYPES]
    # 结构有问题的 choice 题（缺 choices / answer 不在选项里）不进入表达式比较，格式错误里已经报了
    safe = [q for q in questions_ok if not (q["type"] == "choice" and not (
        isinstance(q.get("choices"), list) and all(isinstance(c, dict) and "key" in c and "text" in c for c in q["choices"])
        and q.get("answer") in [c["key"] for c in q["choices"]]))
        and not (q["type"] == "numeric" and V.parse_numeric_answer(q.get("answer")) is None)]
    res = verify_all(safe)
    bad_ids = {q["id"] for q in questions_ok} - {q["id"] for q in safe}
    for qid in sorted(bad_ids):
        res["unverifiable"].append(qid)

    n_eligible = sum(1 for q in questions_ok if q["type"] in ("numeric", "choice"))
    unver_by_type = Counter(q["type"] for q in questions_ok if q["id"] in set(res["unverifiable"]))
    report = {
        "generated_at": __import__("datetime").datetime.now().isoformat(timespec="seconds"),
        "source": os.path.relpath(path, ROOT),
        "total_questions": len(questions),
        "by_type": dict(Counter(q.get("type") for q in questions)),
        "format_errors": errs,
        "auto_verified": len(res["auto_verified"]),
        "mismatch": len(res["mismatch"]),
        "unverifiable": len(res["unverifiable"]),
        "unverifiable_by_type": dict(unver_by_type),
        "numeric_choice_total": n_eligible,
        "numeric_choice_auto_verified_share": round(len(res["auto_verified"]) / float(n_eligible), 4) if n_eligible else None,
        "mismatches": res["mismatch"],
        "unverifiable_ids": sorted(res["unverifiable"]),
    }
    sp = load_second_pass_log() if not args.file else None
    if sp is not None:
        report["second_pass"] = dict(sp)
        report["second_pass"].setdefault("second_pass_mismatch", [])
    out = args.report or (None if args.file else REPORT_PATH)
    if out:
        with open(out, "w", encoding="utf-8") as f:
            json.dump(report, f, ensure_ascii=False, indent=2)
            f.write("\n")

    print("题目 %d 道；numeric+choice %d 道" % (len(questions), n_eligible))
    print("auto_verified %d　mismatch %d　unverifiable %d（%s）" % (
        report["auto_verified"], report["mismatch"], report["unverifiable"],
        "，".join("%s %d" % kv for kv in sorted(unver_by_type.items())) or "无"))
    for m in res["mismatch"][:60]:
        print("  MISMATCH %s answer=%r verify=%r → %s" % (m["id"], m["answer"], m["verify"], m["detail"]))
    if len(res["mismatch"]) > 60:
        print("  ……另有 %d 处" % (len(res["mismatch"]) - 60))
    if out:
        print("报告：" + os.path.relpath(out, ROOT))
    if res["mismatch"] or errs:
        print("VERIFICATION FAILED")
        return 1
    sp_bad = (report.get("second_pass") or {}).get("second_pass_mismatch")
    if sp_bad:
        print("VERIFICATION FAILED（第二遍复核仍有 %d 处未解决）" % len(sp_bad))
        return 1
    print("VERIFICATION PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
