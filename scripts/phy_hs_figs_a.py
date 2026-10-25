#!/usr/bin/env python3
"""高中物理示意图 A：必修一（运动、力、牛顿定律）。每个函数返回 SVG 字符串。"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phy_fig_lib import Fig, Slope, axes, sample, n
import fig_draw as D


def expect(cond, msg):
    if not cond:
        raise SystemExit("图和题目不一致：" + msg)


def near(got, want, eps, msg):
    expect(abs(got - want) <= eps, "%s：得到 %.3f，应为 %.3f" % (msg, got, want))


# ---------------------------------------------------------------- 运动学
def trains():
    f = Fig(360, 120)
    f.ground(10, 350, 88)
    f.box(30, 54, 50, 34, "甲", 14)
    f.box(84, 54, 50, 34)
    f.box(226, 54, 50, 34, "乙", 14)
    f.box(280, 54, 50, 34)
    s = 2.0
    f.arr((36, 38), (36 + 30 * s, 38))
    f.t(36 + 15 * s, 28, "30 m/s", 14)
    f.arr((324, 38), (324 - 20 * s, 38))
    f.t(324 - 10 * s, 28, "20 m/s", 14)
    f.t(180, 112, "相向而行", 14)
    return f.svg()


def walk_triangle():
    f = Fig(300, 205)
    k = 3.0
    A = (50, 175)
    C = (A[0] + 30 * k, 175)
    B = (C[0], 175 - 40 * k)
    f.arr(A, C)
    f.arr(C, B)
    f.thin(A, B, 1.8, dash=True)
    f.right(C, A, B)
    f.dot(*A)
    f.dot(*B)
    f.t(A[0] - 6, A[1] + 18, "A", 16, "end")
    f.t(B[0] + 10, B[1] - 4, "B", 16, "start")
    f.t((A[0] + C[0]) / 2, A[1] + 22, "30 m", 14)
    f.t(C[0] + 10, (C[1] + B[1]) / 2 + 5, "40 m", 14, "start")
    f.arr((230, 150), (230, 112), 1.8)
    f.t(230, 104, "北", 14)
    f.arr((230, 150), (268, 150), 1.8)
    f.t(280, 155, "东", 14)
    return f.svg()


def numline_path():
    f = Fig(300, 140)
    s, ox, y = 22.0, 120, 66
    f.arr((14, y), (284, y), 2.0)
    for m in range(-4, 7):
        f.thin((ox + s * m, y - 4), (ox + s * m, y + 4), 1.6)
    f.t(ox, y + 20, "0", 14)
    f.t(280, y + 18, "x", 14, "end")
    f.t(296, y + 36, "向东为正", 13, "end")
    f.dot(ox, y)
    f.curve_arr((ox, y - 4), (ox + 3 * s, y - 60), (ox + 6 * s, y - 4), 2.0)
    f.t(ox + 3 * s, y - 40, "向东 6 m", 14)
    f.curve_arr((ox + 6 * s, y + 4), (ox + s, y + 60), (ox - 4 * s, y + 4), 2.0)
    f.t(ox + s, y + 56, "向西 10 m", 14)
    return f.svg()


def two_points_axis():
    f = Fig(330, 112)
    s, ox, y = 24.0, 190, 66
    f.arr((16, y), (316, y), 2.0)
    for m in range(-6, 5):
        f.thin((ox + s * m, y - 4), (ox + s * m, y + 4), 1.6)
    for m, lab in ((-5, "-5"), (0, "0"), (3, "3")):
        f.t(ox + s * m, y + 22, lab, 14)
    f.t(312, y + 20, "x/m", 14, "end")
    for m, lab in ((3, "t = 2 s"), (-5, "t = 6 s")):
        f.dot(ox + s * m, y, 4)
        f.t(ox + s * m, y - 14, lab, 14)
    return f.svg()


def half_half():
    f = Fig(360, 120)
    y = 62
    f.ln((30, y), (330, y), 2.4)
    for x in (30, 180, 330):
        f.dot(x, y, 4)
    f.thin((180, y - 8), (180, y + 8), 1.8)
    f.dim((30, 38), (180, 38), "30 m/s", lp=(0, -9))
    f.dim((180, 38), (330, 38), "60 m/s", lp=(0, -9))
    f.t(105, y + 28, "前一半位移", 14)
    f.t(255, y + 28, "后一半位移", 14)
    return f.svg()


def glider_gate():
    f = Fig(360, 130)
    f.ground(10, 350, 102)
    f.box(50, 82, 100, 20, None)
    f.box(94, 46, 12, 36, None, op=0.3)
    f.thin((94, 38), (106, 38), 1.7)
    for x in (94, 106):
        f.thin((x, 33), (x, 43), 1.7)
    f.t(100, 24, "d = 3.0 cm", 14)
    f.t(86, 62, "遮光片", 13, "end")
    f.ln((240, 34), (272, 34), 2.4)
    f.ln((240, 34), (240, 72), 2.4)
    f.ln((272, 34), (272, 72), 2.4)
    f.t(256, 22, "光电门", 14)
    f.arr((160, 92), (212, 92), 2.0)
    return f.svg()


def ball_wall():
    f = Fig(330, 150)
    f.wall(300, 14, 140, side=1)
    k = 10.0
    f.ring(112, 44, 11, op=0.15)
    f.arr((128, 44), (128 + 8 * k, 44))
    f.t(128 + 4 * k, 30, "8 m/s", 14)
    f.t(34, 49, "碰前", 14)
    f.ring(212, 112, 11, op=0.15)
    f.arr((196, 112), (196 - 6 * k, 112))
    f.t(196 - 3 * k, 98, "6 m/s", 14)
    f.t(34, 117, "碰后", 14)
    return f.svg()


def v_a_opposite():
    f = Fig(360, 130)
    f.ground(20, 340, 90)
    f.box(165, 64, 40, 26, None)
    k = 20.0
    f.arr((205, 52), (205 + 5 * k, 52))
    f.t(205 + 2.5 * k, 38, "v = 5 m/s", 14)
    f.arr((165, 52), (165 - 2 * k, 52))
    f.t(165 - 2 * k, 38, "a = 2 m/s²", 14, "end")
    f.t(30, 118, "西", 14)
    f.arr((52, 114), (310, 114), 1.6)
    f.t(330, 118, "东", 14)
    return f.svg()


def tape(labels, segs, scale, fmt, stagger=False, caption=None, total=None, first=30):
    xs = [first]
    for s in segs:
        xs.append(xs[-1] + s * scale)
    W = xs[-1] + first
    y = 78 if not stagger else 92
    H = y + (60 if caption else 44)
    f = Fig(W, H)
    f.box(xs[0] - 14, y - 11, xs[-1] - xs[0] + 28, 22, None, op=0.07, sw=1.8)
    for i, x in enumerate(xs):
        f.dot(x, y, 3.4)
        f.t(x, y + 30, labels[i], 15)
    for i, s in enumerate(segs):
        f.dim((xs[i], y - 16), (xs[i + 1], y - 16), None, tl=4, sw=1.4)
        f.t((xs[i] + xs[i + 1]) / 2, y - 24 - (0 if (not stagger or i % 2 == 0) else 17), fmt(s), 12)
    if total:
        i, j, lab = total
        f.dim((xs[i], 20), (xs[j], 20), lab, size=14, lp=(0, -9))
    if caption:
        f.t(W / 2, H - 8, caption, 13)
    return f.svg()


def tape_c():
    return tape("ABCDE", [3.00, 4.60, 6.20, 7.80], 12, lambda v: "%.2f" % v, caption="单位：cm，相邻计数点间 T = 0.1 s")


def tape_six():
    return tape("OABCDEF"[:7], [1.40, 3.40, 5.40, 7.40, 9.40, 11.40], 11, lambda v: "%.2f" % v, stagger=True,
                caption="单位：cm，相邻计数点间 T = 0.1 s")


def tape_four():
    return tape("OABCD"[:5], [3.00, 3.38, 3.82, 4.20], 13, lambda v: "%.2f" % v, caption="单位：cm，相邻计数点间 T = 0.10 s")


def tape_abc():
    return tape("ABC", [3.4, 3.8], 14, lambda v: "", total=(0, 2, "AC = 7.2 cm"), caption="相邻两点间隔 0.02 s")


def tape_op():
    f = Fig(240, 190)
    f.ground(20, 220, 176)
    f.dot(110, 24, 4)
    f.t(124, 29, "O", 15, "start")
    f.dot(110, 144, 4)
    f.t(124, 149, "P", 15, "start")
    f.dim((70, 24), (70, 144), "0.5 m", lp=(-28, 5))
    f.thin((70, 24), (110, 24), 1.4, dash=True)
    f.thin((70, 144), (110, 144), 1.4, dash=True)
    f.ring(110, 144, 9, op=0.15)
    f.t(168, 100, "重物下落", 13)
    f.arr((168, 108), (168, 136), 1.8)
    return f.svg()


def vt_origin():
    f = Fig(280, 170)
    ox, oy = 50, 140
    axes(f, ox, oy, 200, 120, "t", "v")
    f.ln((ox, oy), (ox + 170, oy - 95), 3.0)
    return f.svg()


def vt_area():
    f = Fig(280, 170)
    ox, oy = 50, 140
    axes(f, ox, oy, 200, 120, "t", "v")
    p0 = (ox, oy - 40)
    p1 = (ox + 160, oy - 98)
    f.fillpath([(ox, oy), p0, p1, (p1[0], oy)], 0.16)
    f.ln(p0, p1, 3.0)
    f.thin(p1, (p1[0], oy), 1.6, dash=True)
    return f.svg()


def drop_height():
    f = Fig(210, 225)
    gy, top = 200, 40
    f.ground(20, 190, gy)
    f.ring(120, top, 10, op=0.15)
    f.arr((120, top + 14), (120, top + 62), 2.0)
    f.thin((46, top), (112, top), 1.4, dash=True)
    f.dim((46, top), (46, gy), "20 m", lp=(-26, 5))
    f.t(150, top + 44, "静止释放", 13, "start")
    return f.svg()


def roof_stone():
    g, t = 10.0, 3.0
    H = 0.5 * g * t * t
    last = H - 0.5 * g * (t - 1) ** 2
    near(last, 25, 1e-6, "最后 1 s 下落")
    k = 3.0
    gy = 185
    top = gy - H * k
    yl = gy - last * k
    f = Fig(280, 210)
    f.ground(20, 260, gy)
    f.box(50, top, 54, gy - top, None, op=0.08)
    f.t(77, top + 28, "屋顶", 13)
    f.ring(122, top - 8, 8, op=0.15)
    f.thin((104, top), (150, top), 1.4, dash=True)
    f.dot(150, yl, 3.4)
    f.thin((122, top), (122, yl), 1.4, dash=True)
    f.thin((104, yl), (150, yl), 1.4, dash=True)
    f.dim((196, yl), (196, gy), "25 m", lp=(28, 5))
    f.thin((150, yl), (196, yl), 1.4, dash=True)
    f.t(190, yl - 14, "最后 1 s", 13, "end")
    f.dim((30, top), (30, gy), "H", lp=(-12, 5))
    return f.svg()


def water_drops():
    g, T = 10.0, 0.2
    H = 0.5 * g * (4 * T) ** 2
    near(H, 3.2, 1e-9, "屋檐高度")
    k = 50.0
    top, gy = 26, 26 + H * k
    f = Fig(250, gy + 48)
    f.ground(20, 230, gy)
    f.ceiling(70, 130, top)
    f.wall(70, top, top + 24, side=-1)
    f.dim((52, top), (52, gy), "3.2 m", lp=(-26, 5))
    ys = []
    for i in range(1, 6):
        fall = 0.5 * g * ((5 - i) * T) ** 2
        y = top + fall * k
        ys.append(y)
        f.ring(150, y - (4.6 if i == 1 else 0), 4.6, op=0.4)
        f.t(164, y + 5 - (4.6 if i == 1 else 0), str(i), 13, "start")
    near((ys[1] - ys[2]) / k, 1.0, 1e-9, "第2、3滴间距")
    f.t(190, gy + 36, "数字表示第几滴", 12, "end")
    return f.svg()


# ---------------------------------------------------------------- 弹簧
def spring_stretch():
    f = Fig(240, 165)
    f.wall(30, 24, 134, side=-1)
    f.spring((30, 52), (90, 52), turns=5, lead=8)
    f.dot(90, 52, 3.2)
    f.t(60, 34, "原长", 14)
    f.spring((30, 112), (120, 112), turns=6, lead=8)
    f.dot(120, 112, 3.2)
    f.arr((120, 112), (176, 112), 2.2)
    f.t(190, 117, "F", 15, "start")
    f.thin((90, 52), (90, 140), 1.4, dash=True)
    f.thin((120, 112), (120, 140), 1.4, dash=True)
    near(120 - 90, 30, 1e-6, "伸长量")
    f.dim((90, 140), (120, 140), "5 cm", lp=(0, 18))
    return f.svg()


def spring_hang():
    f = Fig(300, 190)
    f.ceiling(40, 270, 22)
    k = 8.0
    f.spring((100, 22), (100, 22 + 10 * k), turns=6, lead=8)
    f.dim((70, 22), (70, 22 + 10 * k), "10 cm", lp=(-26, 5))
    f.t(100, 22 + 10 * k + 30, "不挂物体", 14)
    L2 = 14 * k
    f.spring((220, 22), (220, 22 + L2), turns=7, lead=8)
    f.box(195, 22 + L2, 50, 36, "2 kg", 14)
    f.dim((188, 22), (188, 22 + L2), "14 cm", lp=(-26, 5))
    return f.svg()


def spring_two_pulls():
    f = Fig(280, 170)
    f.wall(30, 14, 150, side=-1)
    k = 8.0
    for y, cm, N in ((44, 12, 4), (118, 14, 8)):
        x1 = 30 + cm * k
        f.spring((30, y), (x1, y), turns=6, lead=8)
        f.arr((x1, y), (x1 + N * 10, y), 2.2)
        f.t(x1 + N * 5, y - 12, "%d N" % N, 14)
        f.dim((30, y + 18), (x1, y + 18), "%d cm" % cm, lp=(0, 17))
    return f.svg()


def graph_Fx():
    f = Fig(250, 185)
    ox, oy = 50, 150
    axes(f, ox, oy, 190, 130, "x/cm", "F/N")
    kx, kf = 30.0, 40.0
    px, py = ox + 4.0 * kx, oy - 2.0 * kf
    near((oy - py) / (px - ox), 2.0 / 4.0 * kf / kx, 1e-9, "斜率")
    f.ln((ox, oy), (ox + 6 * kx, oy - 3 * kf), 3.0)
    f.thin((ox, py), (px, py), 1.5, dash=True)
    f.thin((px, py), (px, oy), 1.5, dash=True)
    f.dot(px, py, 4)
    f.t(px, oy + 20, "4.0", 14)
    f.t(ox - 8, py + 5, "2.0", 14, "end")
    return f.svg()


def graph_Fl():
    f = Fig(270, 190)
    ox, oy = 40, 150
    axes(f, ox, oy, 215, 130, "l/cm", "F/N")
    k = 12.0
    x8 = ox + 8 * k
    f.ln((x8, oy), (x8 + 6 * k, oy - 100), 3.0)
    f.dot(x8, oy, 4)
    f.t(x8, oy + 20, "8", 14)
    return f.svg()


def graph_data():
    f = Fig(300, 232)
    ox, oy = 62, 186
    axes(f, ox, oy, 215, 170, None, None, o_label=False)
    f.t(ox - 10, oy - 170 - 2, "l/cm", 14, "end")
    f.t(ox + 215, oy + 36, "钩码个数", 14, "end")
    kx, ky = 40.0, 9.0
    ls = [15.0, 17.5, 20.0, 22.5, 25.0, 29.0]
    pts = [(ox + i * kx, oy - (l - 13.0) * ky) for i, l in enumerate(ls)]
    f.thin(pts[0], (ox + 5 * kx, oy - (27.5 - 13.0) * ky), 1.5, dash=True)
    for i, p in enumerate(pts):
        f.dot(p[0], p[1], 4.2)
        f.t(p[0], oy + 18, str(i), 14)
    for l in (15.0, 25.0, 29.0):
        y = oy - (l - 13.0) * ky
        f.thin((ox - 4, y), (ox + 4, y), 1.5)
        f.t(ox - 10, y + 5, "%.1f" % l, 13, "end")
    f.t(pts[5][0] - 10, pts[5][1] - 4, "超过弹性限度", 13, "end")
    return f.svg()


# ---------------------------------------------------------------- 受力
def pull_box(box_label, F_label, ang, s_label=None, push=False):
    W = 340
    f = Fig(W, 150)
    gy = 112
    f.ground(14, W - 14, gy)
    bx, bw, bh = 110, 70, 42
    f.box(bx, gy - bh, bw, bh, box_label, 13)
    cy = gy - bh / 2
    if ang == 0:
        f.arr((bx - 66, cy), (bx, cy), 2.4)
        f.t(bx - 33, cy - 12, F_label, 14)
    else:
        a = (bx + bw, cy)
        r = math.radians(ang)
        e = (a[0] + 88 * math.cos(r), a[1] - 88 * math.sin(r))
        f.arr(a, e, 2.4)
        f.thin(a, (a[0] + 56, a[1]), 1.4, dash=True)
        f.angle((a[0] + 56, a[1]), a, e, 34, "%d°" % ang, 14, 14)
        near(D.angle_deg((a[0] + 56, a[1]), a, e), ang, 0.2, "拉力角")
        f.t(e[0] + 6, e[1] - 4, F_label, 14, "start")
    if s_label:
        sh = 140
        f.path([(bx + sh, gy), (bx + sh, gy - bh), (bx + sh + bw, gy - bh), (bx + sh + bw, gy)], 1.6, dash=True)
        f.dim((bx + bw / 2, gy + 24), (bx + sh + bw / 2, gy + 24), s_label, lp=(0, 17))
        f.thin((bx + bw / 2, gy + 6), (bx + bw / 2, gy + 30), 1.2, dash=True)
        f.thin((bx + sh + bw / 2, gy + 6), (bx + sh + bw / 2, gy + 30), 1.2, dash=True)
        f.h = 160
    return f.svg()


def conveyor_flat():
    f = Fig(330, 150)
    f.ring(70, 100, 16, op=0.1)
    f.ring(250, 100, 16, op=0.1)
    f.ln((70, 84), (250, 84), 2.6)
    f.ln((70, 116), (250, 116), 2.6)
    f.box(84, 56, 30, 28, None, op=0.2)
    f.arr((150, 58), (226, 58), 2.2)
    f.t(190, 46, "传送带速度", 14)
    return f.svg()


def conveyor_incline():
    f = Fig(330, 215)
    S = Slope((34, 176), 28)
    L = 262
    c1, c2 = S.P(14, -14), S.P(L - 14, -14)
    f.ring(c1[0], c1[1], 14, op=0.1)
    f.ring(c2[0], c2[1], 14, op=0.1)
    f.ln(S.P(14, 0), S.P(L - 14, 0), 2.6)
    f.ln(S.P(14, -28), S.P(L - 14, -28), 2.6)
    S.block(f, 110, 150, 30)
    f.arr(S.P(168, 22), S.P(236, 22), 2.2)
    f.t(S.P(202, 22)[0] - 8, S.P(202, 22)[1] - 18, "向上匀速", 14)
    return f.svg()


def stack_AB():
    f = Fig(290, 150)
    f.ground(20, 270, 124)
    f.box(60, 80, 170, 44, "B  5 kg", 14)
    f.box(104, 38, 82, 42, "A  3 kg", 14)
    return f.svg()


def perp_forces():
    f = Fig(210, 130)
    O = (60, 100)
    f.arr(O, (O[0] + 80, O[1]), 2.6)
    f.arr(O, (O[0], O[1] - 60), 2.6)
    f.right(O, (O[0] + 80, O[1]), (O[0], O[1] - 60))
    f.dot(*O, 4)
    f.t(O[0] + 40, O[1] + 20, "4 N", 14)
    f.t(O[0] - 10, O[1] - 30, "3 N", 14, "end")
    return f.svg()


def two_forces_120():
    f = Fig(290, 130)
    O = (145, 110)
    ends = []
    for deg in (30, 150):
        r = math.radians(deg)
        e = (O[0] + 100 * math.cos(r), O[1] - 100 * math.sin(r))
        ends.append(e)
        f.arr(O, e, 2.6)
    near(D.angle_deg(ends[0], O, ends[1]), 120, 0.1, "夹角")
    f.angle(ends[0], O, ends[1], 28, "120°", 14, 18)
    f.dot(*O, 4)
    f.t(ends[0][0] + 6, ends[0][1] + 4, "10 N", 14, "start")
    f.t(ends[1][0] - 6, ends[1][1] + 4, "10 N", 14, "end")
    return f.svg()


def parallelogram_FFp():
    s = 0.8
    O = (80, 172)
    a1, l1 = math.radians(20), 120 * s
    a2, l2 = math.radians(70), 100 * s
    F1 = (O[0] + l1 * math.cos(a1), O[1] - l1 * math.sin(a1))
    F2 = (O[0] + l2 * math.cos(a2), O[1] - l2 * math.sin(a2))
    F = (F1[0] + F2[0] - O[0], F1[1] + F2[1] - O[1])
    dx, dy = F[0] - O[0], O[1] - F[1]
    aF = math.atan2(dy, dx)
    Lf = math.hypot(dx, dy)
    ap = aF + math.radians(11)
    Fp = (O[0] + Lf * 1.02 * math.cos(ap), O[1] - Lf * 1.02 * math.sin(ap))
    f = Fig(310, 240)
    f.thin(F1, F, 1.4, dash=True)
    f.thin(F2, F, 1.4, dash=True)
    f.arr(O, F1, 2.4)
    f.arr(O, F2, 2.4)
    f.arr(O, F, 2.6)
    f.arr(O, Fp, 2.2)
    G = (O[0] - 70 * math.cos(ap), O[1] + 70 * math.sin(ap))
    f.ln(G, O, 1.8)
    f.ring(G[0], G[1], 5, op=0.3)
    f.dot(*O, 4)
    f.t((G[0] + O[0]) / 2 - 12, (G[1] + O[1]) / 2 + 8, "橡皮条", 13, "end")
    f.t(F1[0] + 8, F1[1] + 6, "F₁", 15, "start")
    f.t(F2[0] - 8, F2[1] - 4, "F₂", 15, "end")
    f.t(F[0] + 10, F[1] + 20, "F", 15, "start")
    f.t(Fp[0] + 8, Fp[1] - 6, "F′", 15, "start")
    expect(abs(math.degrees(ap) - math.degrees(aF)) > 3, "F′ 应略偏离 F")
    return f.svg()


def forces_345():
    f = Fig(340, 200)
    O = (50, 170)
    k = 20.0
    F1 = (O[0], O[1] - 3 * k)
    F2 = (O[0] + 4 * k, O[1])
    F = (O[0] + 4 * k, O[1] - 3 * k)
    near(math.hypot(F[0] - O[0], F[1] - O[1]) / k, 5.0, 1e-9, "合力")
    f.thin(F1, F, 1.4, dash=True)
    f.thin(F2, F, 1.4, dash=True)
    f.arr(O, F1, 2.4)
    f.arr(O, F2, 2.4)
    f.arr(O, F, 2.6)
    ap = math.atan2(3, 4) + math.radians(4)
    Fp = (O[0] + 5.2 * k * math.cos(ap), O[1] - 5.2 * k * math.sin(ap))
    f.arr(O, Fp, 2.0)
    f.dot(*O, 4)
    f.t(O[0] - 8, O[1] - 30, "3.0 N", 14, "end")
    f.t(O[0] + 40, O[1] + 20, "4.0 N", 14)
    f.t(F[0] + 8, F[1] + 18, "5.0 N（作图）", 13, "start")
    f.t(Fp[0] + 8, Fp[1] - 8, "5.2 N（单个测力计）", 13, "start")
    return f.svg()


def force_components():
    f = Fig(260, 175)
    O = (46, 140)
    r = math.radians(37)
    e = (O[0] + 120 * math.cos(r), O[1] - 120 * math.sin(r))
    f.arr(O, e, 2.8)
    f.thin(O, (e[0], O[1]), 1.6, dash=True)
    f.thin(e, (e[0], O[1]), 1.6, dash=True)
    f.angle((O[0] + 70, O[1]), O, e, 44, "37°", 14, 16)
    f.t(e[0] + 8, e[1] + 2, "100 N", 14, "start")
    f.t((O[0] + e[0]) / 2, O[1] + 20, "水平分力", 13)
    f.t(e[0] + 8, (e[1] + O[1]) / 2 + 20, "竖直分力", 13, "start")
    return f.svg()


def incline_base(deg, L=230, x0=34, y0=172):
    S = Slope((x0, y0), deg)
    C = S.P(L)
    B = (C[0], y0)
    return S, C, B


def incline_mg():
    f = Fig(280, 190)
    S, C, B = incline_base(30)
    f.poly([S.base, C, B], 0.08, 2.6)
    pts = S.block(f, 90, 144, 36)
    c = S.P(117, 18)
    f.arr(c, (c[0], c[1] + 66), 2.6)
    f.t(c[0] + 8, c[1] + 74, "mg", 14, "start")
    d = (S.d[0] * -1, S.d[1] * -1)
    f.thin(c, (c[0] + d[0] * 33, c[1] + d[1] * 33), 1.6, dash=True)
    f.thin(c, (c[0] - S.nv[0] * 57, c[1] - S.nv[1] * 57), 1.6, dash=True)
    f.angle(C, S.base, B, 40, "θ", 15, 16)
    return f.svg()


def incline_block(deg, label, extra=None, label_frac=0.5):
    f = Fig(280, 195)
    S, C, B = incline_base(deg)
    f.poly([S.base, C, B], 0.08, 2.6)
    S.block(f, 92, 144, 34, label, 13, label_frac)
    f.angle(C, S.base, B, 44, "%d°" % deg, 14, 14)
    if extra:
        extra(f, S)
    return f.svg()


def incline_G(deg, label):
    def ex(f, S):
        c = S.P(118, 10)
        f.arr(c, (c[0], c[1] + 56), 2.4)
        f.t(c[0] + 8, c[1] + 62, "G", 14, "start")
    return incline_block(deg, label, ex, 0.74)


def force_resolve_10N():
    f = Fig(250, 150)
    O = (50, 120)
    f.arr(O, (O[0] + 130, O[1]), 2.8)
    r = math.radians(30)
    e = (O[0] + 170 * math.cos(r), O[1] - 170 * math.sin(r))
    f.thin(O, e, 1.8, dash=True)
    f.angle((O[0] + 80, O[1]), O, e, 50, "30°", 14, 16)
    f.t(O[0] + 66, O[1] + 20, "F = 10 N", 14)
    f.t(e[0] - 8, e[1] - 6, "F₁ 的方向", 13, "end")
    f.dot(*O, 4)
    return f.svg()


def two_ropes_60():
    f = Fig(300, 200)
    O = (150, 104)
    L = 110
    A = (O[0] - L * math.sin(math.radians(60)), O[1] - L * math.cos(math.radians(60)))
    B = (O[0] + L * math.sin(math.radians(60)), A[1])
    V = (O[0], A[1])
    f.ceiling(A[0] - 30, B[0] + 30, A[1])
    f.ln(A, O, 2.4)
    f.ln(B, O, 2.4)
    f.thin(O, V, 1.5, dash=True)
    near(D.angle_deg(A, O, V), 60, 0.1, "左绳夹角")
    near(D.angle_deg(B, O, V), 60, 0.1, "右绳夹角")
    f.angle(A, O, V, 30, "60°", 14, 16)
    f.angle(V, O, B, 30, "60°", 14, 16)
    f.ln(O, (O[0], O[1] + 34), 2.4)
    f.box(O[0] - 26, O[1] + 34, 52, 36, "100 N", 14)
    f.dot(*O, 3.6)
    return f.svg()


def incline_push_up():
    def ex(f, S):
        a = S.P(144, 17)
        f.arr(a, S.P(206, 17), 2.6)
        f.t(S.P(206, 17)[0] + 6, S.P(206, 17)[1] - 6, "F", 15, "start")
    return incline_block(37, "4 kg", ex)


def ball_pulled():
    f = Fig(290, 165)
    P = (100, 18)
    f.ceiling(60, 150, P[1])
    th = math.radians(35)
    L = 118
    B = (P[0] + L * math.sin(th), P[1] + L * math.cos(th))
    f.thin(P, (P[0], P[1] + 134), 1.5, dash=True)
    f.ln(P, B, 2.2)
    f.ring(B[0], B[1], 11, op=0.2)
    f.t(B[0] - 16, B[1] + 5, "m", 14, "end")
    f.arr((B[0] + 11, B[1]), (B[0] + 78, B[1]), 2.6)
    f.t(B[0] + 46, B[1] - 12, "F", 15)
    f.angle((P[0], P[1] + 80), P, B, 56, "θ", 15, 14)
    return f.svg()


def graph_aF_bend():
    f = Fig(270, 200)
    ox, oy = 50, 170
    axes(f, ox, oy, 205, 150, "F", "a")
    f.thin((ox, oy), (ox + 180, oy - 126), 1.6, dash=True)
    pts = []
    for i in range(0, 141):
        x = i * 1.25 + 0.0
        if x <= 100:
            y = 0.7 * x
        else:
            y = 70 + 0.7 * (x - 100) - 0.004 * (x - 100) ** 2
        pts.append((ox + x, oy - y))
    f.path(pts, 3.0)
    return f.svg()


def block_two_forces():
    f = Fig(340, 130)
    f.ground(14, 326, 104)
    f.box(140, 62, 80, 42, "4 kg", 14)
    f.arr((220, 83), (300, 83), 2.6)
    f.t(262, 68, "F = 20 N", 14)
    f.arr((140, 83), (108, 83), 2.6)
    f.t(112, 66, "摩擦力 8 N", 13, "end")
    return f.svg()


def spring_string_AB():
    f = Fig(250, 222)
    f.ceiling(70, 170, 16)
    f.spring((120, 16), (120, 86), turns=6, lead=8)
    f.ring(120, 102, 15, op=0.18)
    f.t(120, 107, "A", 15)
    f.ln((120, 117), (120, 167), 2.0)
    f.ring(120, 182, 15, op=0.18)
    f.t(120, 187, "B", 15)
    f.t(142, 54, "轻质弹簧", 13, "start")
    f.t(142, 134, "细线", 13, "start")
    f.thin((113, 143), (127, 157), 2.0)
    f.thin((127, 143), (113, 157), 2.0)
    f.t(142, 156, "剪断", 13, "start")
    return f.svg()


def top_view_forces():
    f = Fig(270, 175)
    O = (80, 134)
    k = 10.0
    f.box(O[0] - 14, O[1] - 14, 28, 28, None, op=0.15)
    f.arr(O, (O[0] + 6 * k, O[1]), 2.6)
    f.arr(O, (O[0], O[1] - 8 * k), 2.6)
    f.t(O[0] + 6 * k + 8, O[1] + 5, "F₁ = 6 N（向东）", 13, "start")
    f.t(O[0] + 10, O[1] - 8 * k - 4, "F₂ = 8 N（向北）", 13, "start")
    f.t(O[0] - 20, O[1] + 34, "5 kg", 13, "end")
    f.arr((234, 60), (234, 24), 1.6)
    f.t(234, 16, "北", 13)
    f.arr((220, 60), (254, 60), 1.6)
    f.t(264, 64, "东", 13)
    return f.svg()


def incline_smooth():
    def ex(f, S):
        a = S.P(92 + 26, 50)
        f.arr(a, (a[0] - S.d[0] * 52, a[1] - S.d[1] * 52), 2.2)
        f.t(S.P(176, -30)[0], S.P(176, -30)[1], "光滑", 14)
    return incline_block(30, "m", ex)


def incline_mu(deg, label, mu_only=True, v0=False):
    def ex(f, S):
        p = S.P(156, -30)
        f.t(p[0], p[1], "μ = 0.5", 14)
        if v0:
            a = S.P(150, 17)
            b = S.P(210, 17)
            f.arr(a, b, 2.4)
            f.t(S.P(180, 17)[0] - 10, S.P(180, 17)[1] - 24, "初速度 10 m/s", 13, "end")
    return incline_block(deg, label, ex)


def two_blocks_rope():
    f = Fig(340, 140)
    f.ground(14, 326, 104)
    f.t(36, 128, "光滑", 13, "start")
    f.box(40, 56, 70, 48, None)
    f.t(75, 76, "m₁", 14)
    f.t(75, 94, "3 kg", 13)
    f.ln((110, 80), (160, 80), 2.0)
    f.box(160, 56, 70, 48, None)
    f.t(195, 76, "m₂", 14)
    f.t(195, 94, "2 kg", 13)
    f.arr((230, 80), (310, 80), 2.6)
    f.t(270, 66, "F = 20 N", 14)
    return f.svg()


def table_pulley():
    f = Fig(300, 200)
    f.box(20, 72, 192, 70, "光滑桌面", 14, op=0.07)
    f.box(78, 38, 64, 34, None)
    f.t(110, 53, "m₁", 13)
    f.t(110, 68, "4 kg", 12)
    f.ln((142, 55), (230, 55), 1.8)
    f.ring(230, 66, 11, op=0.1)
    f.ln((212, 72), (219, 66), 2.0)
    f.raw('<path d="M 230 55 A 11 11 0 0 1 241 66" fill="none" stroke="currentColor" stroke-width="1.8"/>')
    f.ln((241, 66), (241, 126), 1.8)
    f.box(214, 126, 54, 44, None)
    f.t(241, 145, "m₂", 13)
    f.t(241, 162, "1 kg", 12)
    return f.svg()


def plank_AB():
    f = Fig(350, 168)
    f.ground(14, 336, 124)
    f.t(180, 152, "光滑水平面", 13)
    f.box(40, 92, 220, 32, "B  2 kg", 14)
    f.box(96, 56, 66, 36, "A  1 kg", 14)
    f.t(210, 86, "μ = 0.2", 14)
    f.arr((260, 108), (322, 108), 2.6)
    f.t(300, 96, "F", 15)
    return f.svg()


def elevator_scale():
    f = Fig(310, 195)
    f.ln((120, 4), (120, 28), 2.4)
    f.box(54, 28, 132, 132, None, op=0.06)
    f.ring(112, 64, 9)
    f.ln((112, 73), (112, 112), 2.4)
    f.ln((112, 84), (98, 100), 2.0)
    f.ln((112, 84), (126, 100), 2.0)
    f.ln((112, 112), (102, 138), 2.4)
    f.ln((112, 112), (122, 138), 2.4)
    f.box(88, 138, 50, 12, None, op=0.3)
    f.t(146, 70, "60 kg", 13, "start")
    f.t(142, 148, "体重计", 12, "start")
    f.arr((218, 134), (218, 74), 2.4)
    f.t(228, 100, "a = 2 m/s²", 14, "start")
    f.t(228, 120, "（向上）", 13, "start")
    return f.svg()


def elevator_spring():
    f = Fig(300, 195)
    f.ln((100, 4), (100, 28), 2.4)
    f.box(36, 28, 200, 140, None, op=0.06)
    f.ln((100, 28), (100, 44), 2.0)
    f.box(88, 44, 24, 48, None, op=0.15)
    f.ln((100, 92), (100, 108), 2.0)
    f.box(82, 108, 36, 34, "2 kg", 12)
    f.t(122, 72, "示数 16 N", 13, "start")
    return f.svg()


def compass_curve():
    f = Fig(330, 195)
    P = (150, 140)
    pts = []
    for i in range(0, 41):
        x = 40 + i * 5.5
        pts.append((x, P[1] - 100 * ((x - P[0]) / 110.0) ** 2))
    f.path(pts, 2.8)
    f.dot(*P, 4.2)
    f.t(P[0], P[1] + 22, "P", 15)
    f.t(pts[0][0] - 4, pts[0][1] - 8, "M", 15, "end")
    f.t(pts[-1][0] + 6, pts[-1][1] - 8, "N", 15, "start")
    f.arr(P, (P[0] + 64, P[1]), 2.6)
    f.t(P[0] + 36, P[1] + 22, "v", 15)
    f.arr((270, 182), (270, 138), 1.8)
    f.t(270, 130, "北", 14)
    f.arr((270, 182), (310, 182), 1.8)
    f.t(322, 187, "东", 14)
    return f.svg()


def river_cross():
    f = Fig(330, 205)
    f.ceiling(14, 316, 28)
    f.ground(14, 316, 176)
    for x in (200, 250):
        f.arr((x, 92), (x + 34, 92), 1.6)
    f.t(236, 112, "水流", 13)
    k = 20.0
    S = (90, 146)
    f.arr(S, (S[0], S[1] - 4 * k), 2.6)
    f.t(S[0] - 8, S[1] - 2 * k, "4 m/s", 14, "end")
    f.thin((S[0], S[1] - 4 * k), (S[0] + 3 * k, S[1] - 4 * k), 1.4, dash=True)
    f.thin((S[0] + 3 * k, S[1] - 4 * k), (S[0] + 3 * k, S[1]), 1.4, dash=True)
    f.arr(S, (S[0] + 3 * k, S[1]), 2.0)
    f.t(S[0] + 1.5 * k, S[1] + 17, "水速 3 m/s", 13)
    f.arr(S, (S[0] + 3 * k, S[1] - 4 * k), 2.0, dash=True)
    f.dot(*S, 3.6)
    return f.svg()


def river_upstream():
    f = Fig(330, 190)
    f.ceiling(14, 316, 22)
    f.ground(14, 316, 160)
    f.dim((52, 22), (52, 160), "200 m", lp=(-27, 5))
    k = 20.0
    S = (150, 150)
    tip = (S[0] - 3 * k, S[1] - 4 * k)
    near(math.hypot(S[0] - tip[0], S[1] - tip[1]) / k, 5.0, 1e-9, "船速")
    f.arr(S, tip, 2.6)
    f.arr(tip, (tip[0] + 3 * k, tip[1]), 2.2)
    f.arr(S, (S[0], S[1] - 4 * k), 2.2, dash=True)
    f.t((S[0] + tip[0]) / 2 - 8, (S[1] + tip[1]) / 2 + 6, "5 m/s", 14, "end")
    f.t(tip[0] + 1.5 * k, tip[1] - 10, "水速 3 m/s", 13)
    f.dot(*S, 3.6)
    return f.svg()


def incline_slide_5m():
    f = Fig(290, 200)
    S, C, B = incline_base(30, L=240)
    f.poly([S.base, C, B], 0.08, 2.6)
    top_u, low_u, hgt = 190, 80, 30
    pts0 = [S.P(top_u, 0), S.P(top_u + 44, 0), S.P(top_u + 44, hgt), S.P(top_u, hgt)]
    f.path(pts0, 1.6, dash=True, close=True)
    S.block(f, low_u, low_u + 44, hgt, "2 kg", 12)
    a, b = S.P(top_u + 22, hgt + 22), S.P(low_u + 22, hgt + 22)
    f.arr(a, b, 1.8)
    near(math.hypot(a[0] - b[0], a[1] - b[1]), (top_u - low_u), 1e-6, "位移沿斜面")
    mid = ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)
    f.t(mid[0] + S.nv[0] * 16, mid[1] + S.nv[1] * 16 + 4, "5 m", 14)
    f.angle(C, S.base, B, 44, "30°", 14, 14)
    return f.svg()
