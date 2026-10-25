#!/usr/bin/env python3
"""给高中物理（topicId 以 cnp_h 开头）的看图题写入内联 SVG。

只改下面登记的题（写入前这些题都没有 figure）。可重复运行。
  python3 scripts/phy_hs_figures.py                    写入 data/questions.json
  python3 scripts/phy_hs_figures.py --preview out.html 只生成预览页，不写数据
自检：图里出现的数字必须能在题干或选项里找到，场景函数里还有几何/物理关系的断言。
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import phy_hs_figs_a as A  # noqa: E402
import phy_hs_figs_b as B  # noqa: E402
from phy_fig_lib import svg_texts  # noqa: E402
from check_figures import figure_problems  # noqa: E402

ROOT = os.path.dirname(HERE)
QUESTIONS = os.path.join(ROOT, "data", "questions.json")


def ids(*pairs):
    out = []
    for p in pairs:
        h, qs = p
        for q in qs:
            out.append("cnp_h%03d_q%d" % (h, q))
    return out


def catalog():
    c = []

    def add(idlist, svg, extra=()):
        if isinstance(idlist, str):
            idlist = [idlist]
        for i in idlist:
            c.append((i, svg, set(extra)))

    # 必修一 运动学
    add(ids((1, [3])), A.trains())
    add(ids((2, [2])), A.walk_triangle())
    add(ids((2, [3])), A.numline_path())
    add(ids((3, [2])), A.two_points_axis())
    add(ids((3, [3])), A.half_half())
    add(ids((3, [4])), A.glider_gate())
    add(ids((4, [3])), A.ball_wall())
    add(ids((4, [4])), A.v_a_opposite())
    add(ids((5, [3])), A.tape_c())
    add(ids((5, [4])), A.tape_six())
    add(ids((6, [2])), A.vt_origin())
    add(ids((7, [2])), A.vt_area())
    add(ids((9, [1])), A.drop_height())
    add(ids((9, [3])), A.roof_stone())
    add(ids((9, [4])), A.water_drops(), extra={"4"})
    # 弹簧、摩擦、力
    add(ids((11, [1])), A.spring_stretch())
    add(ids((11, [3])), A.spring_hang())
    add(ids((11, [4])), A.spring_two_pulls())
    add(ids((12, [2])), A.graph_Fx())
    add(ids((12, [3])), A.graph_Fl())
    add(ids((12, [4])), A.graph_data())
    add(ids((13, [1])), A.pull_box("20 kg", "50 N", 0))
    add(ids((13, [2])), A.conveyor_incline())
    add(ids((13, [3])), A.pull_box("重 40 N", "15 N", 0))
    add(ids((14, [3])), A.pull_box("22 kg", "100 N", 37))
    add(ids((14, [4])), A.conveyor_flat())
    add(ids((15, [3])), A.stack_AB())
    add(ids((16, [1])), A.perp_forces())
    add(ids((16, [3])), A.two_forces_120())
    add(ids((17, [3])), A.parallelogram_FFp())
    add(ids((17, [4])), A.forces_345())
    add(ids((18, [1])), A.force_components())
    add(ids((18, [2])), A.incline_mg())
    add(ids((18, [3])), A.incline_G(37, "5 kg"))
    add(ids((18, [4])), A.force_resolve_10N())
    add(ids((19, [2])), A.two_ropes_60())
    add(ids((19, [3])), A.incline_push_up())
    add(ids((19, [4])), A.ball_pulled())
    # 牛顿定律
    add(ids((22, [3])), A.graph_aF_bend())
    add(ids((22, [4])), A.tape_four())
    add(ids((23, [2])), A.block_two_forces())
    add(ids((23, [3])), A.spring_string_AB())
    add(ids((23, [4])), A.top_view_forces())
    add(ids((25, [2])), A.incline_smooth())
    add(ids((25, [3])), A.incline_mu(37, "m"))
    add(ids((25, [4])), A.incline_mu(37, "m", v0=True))
    add(ids((26, [1, 2])), A.two_blocks_rope())
    add(ids((26, [3])), A.table_pulley())
    add(ids((26, [4])), A.plank_AB())
    add(ids((27, [2])), A.elevator_scale())
    add(ids((27, [4])), A.elevator_spring())
    # 曲线运动
    add(ids((28, [4])), A.compass_curve())
    add(ids((29, [2])), A.river_cross())
    add(ids((29, [4])), A.river_upstream())
    add(ids((30, [3])), B.strobe_points())
    add(ids((30, [4])), B.balls_AB())
    add(ids((31, [2])), B.tower_projectile(45, 10, 3.2, "10 m/s", "45 m"))
    add(ids((31, [3])), B.tower_projectile(45, 40, 1.4, "40 m/s", "45 m", xq=False))
    add(ids((31, [4])), B.slope_throw())
    add(ids((32, [2, 3])), B.oblique())
    add(ids((32, [4])), B.oblique_two_angles())
    add(ids((33, [4])), B.belt(44, 22, "主动轮", "从动轮"))
    add(ids((34, [3])), B.turntable())
    add(ids((35, [3])), B.belt(54, 18, "左塔轮", "右塔轮"))
    add(ids((36, [3])), B.belt(54, 18, "A 轮", "B 轮"))
    add(ids((37, [1])), B.bridge(True, "r", "v"))
    add(ids((37, [2])), B.bridge(False, "50 m", "10 m/s"))
    add(ids((37, [3])), B.top_car_curve())
    add(ids((37, [4])), B.vertical_circle())
    add(ids((38, [2])), B.top_ball_string())
    add(ids((38, [4])), B.turntable(dist=True))
    # 万有引力
    add(ids((39, [2])), B.kepler())
    add(ids((40, [3])), B.earth_two_distances())
    add(ids((43, [2])), B.orbit_2R())
    add(ids((43, [3])), B.orbit_AB())
    # 功和能
    add(ids((45, [1])), A.pull_box("木箱", "10 N", 60, "4 m"))
    add(ids((45, [3])), A.incline_slide_5m())
    add(ids((45, [4])), A.pull_box("10 kg", "50 N", 37, "2 m"))
    add(ids((47, [1])), B.height_ball("2 kg", "5 m", ""))
    add(ids((47, [3])), B.table_ball())
    add(ids((48, [3])), B.graph_spring_work())
    add(ids((51, [3])), B.ball_spring_floor())
    add(ids((51, [4])), B.quarter_circle())
    add(ids((52, [3])), A.tape_abc())
    add(ids((52, [4])), A.tape_op())
    # 振动
    add(ids((98, [1])), B.oscillator(54))
    add(ids((98, [2])), B.oscillator(70, extremes=True))
    add(ids((98, [3])), B.oscillator(34, extremes=True, arrow_left=True))
    add(ids((98, [4])), B.osc_vertical())
    add(ids((99, [3])), B.sine_plot_q3())
    add(ids((100, [2])), B.oscillator(30, dim_cm="3 cm", k_label="k = 200 N/m"))
    add(ids((100, [4])), B.oscillator(0, dims_both=(60, "5 cm"), k_label="k = 40 N/m", m_label="0.1 kg"))
    add(ids((101, [1])), B.pendulum())
    # 波
    add(ids((105, [2])), B.wave_profile("λ", "A"))
    add(ids((105, [3])), B.wave_profile(None, crest_dim="1.5 m"))
    add(ids((106, [2])), B.wave_P())
    add(ids((106, [3])), B.wave_and_vibration("q3"))
    add(ids((106, [4])), B.wave_and_vibration("q4"))
    # 光
    add(ids((110, [3])), B.refraction_30())
    add(ids((111, [1])), B.pins_slab())
    add(ids((111, [3])), B.circle_method())
    add(ids((111, [4])), B.slab_bb_far())
    add(ids((112, [3])), B.liquid_cone())
    add(ids((112, [4])), B.optical_fiber())
    return c


def number_problems(qid, svg, text_blob, extra):
    bad = []
    blob = set(re.findall(r"\d+(?:\.\d+)?", text_blob))
    for s in svg_texts(svg):
        for tok in re.findall(r"\d+(?:\.\d+)?", s):
            if tok not in blob and tok not in extra and tok != "0":
                bad.append("%s 的图里有数字 %s，题干和选项里没有（文字：%s）" % (qid, tok, s))
    return bad


def write_preview(items, path, byid):
    parts = ['<!DOCTYPE html><meta charset="utf-8"><title>物理图示预览</title>',
             '<style>body{margin:0;font-family:"Noto Sans CJK SC","PingFang SC",sans-serif;background:#fff;color:#162033}',
             '.row{display:flex;gap:10px;flex-wrap:wrap}.card{width:430px;padding:6px;box-sizing:border-box;border:1px solid #ddd}',
             'svg{width:100%;height:auto;display:block}h2{font-size:12px;margin:4px 0}p{font-size:12px;margin:2px 0 6px;color:#555}</style><div class="row">']
    for qid, svg, _ in items:
        q = byid.get(qid, {})
        parts.append('<div class="card"><h2>%s</h2><p>%s</p>%s</div>' % (qid, q.get("prompt", "")[:90], svg))
    parts.append("</div>")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(parts))
    print("预览", path, "共", len(items), "题")


def main():
    items = catalog()
    seen = set()
    for qid, _, _ in items:
        if qid in seen:
            raise SystemExit("重复登记：" + qid)
        seen.add(qid)
    with open(QUESTIONS, encoding="utf-8") as f:
        questions = json.load(f)
    byid = {q["id"]: q for q in questions if isinstance(q, dict) and "id" in q}
    problems = []
    for qid, svg, extra in items:
        q = byid.get(qid)
        if not q:
            problems.append("找不到题目 " + qid)
            continue
        if not str(q.get("topicId", "")).startswith("cnp_h"):
            problems.append("%s 不是高中物理题" % qid)
        blob = q.get("prompt", "") + " " + " ".join(c.get("text", "") for c in (q.get("choices") or []))
        problems += number_problems(qid, svg, blob, extra)
        problems += figure_problems(svg, qid)
        if re.search(r"AI\s*初稿|免费", svg):
            problems.append(qid + " 图里有不允许的文案")
    if problems:
        print("图示自检失败：")
        for p in problems:
            print("  " + p)
        return 1
    if len(sys.argv) >= 3 and sys.argv[1] == "--preview":
        write_preview(items, sys.argv[2], byid)
        return 0
    added = 0
    for qid, svg, _ in items:
        q = byid[qid]
        if q.get("figure") != svg:
            q["figure"] = svg
            added += 1
    with open(QUESTIONS, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("高中物理带图题：%d（本次新写入或更新 %d）" % (len(items), added))
    return 0


if __name__ == "__main__":
    sys.exit(main())
