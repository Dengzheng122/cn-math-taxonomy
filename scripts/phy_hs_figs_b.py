#!/usr/bin/env python3
"""高中物理示意图 B：抛体、圆周、天体、功能、振动与波、光学。"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from phy_fig_lib import Fig, Slope, axes, sample, n
from phy_hs_figs_a import expect, near, incline_base
import fig_draw as D


# ---------------------------------------------------------------- 抛体
def strobe_points():
    k = 200.0
    dxm, dy1, dy2 = 0.30, 0.15, 0.25
    g, T = 10.0, 0.1
    near(dy2 - dy1, g * T * T, 1e-9, "频闪二阶差")
    near(dxm / T, 3.0, 1e-9, "初速度")
    A = (50, 40)
    B = (A[0] + dxm * k, A[1] + dy1 * k)
    C = (B[0] + dxm * k, B[1] + dy2 * k)
    f = Fig(330, 205)
    f.thin((A[0], A[1]), (C[0] + 20, A[1]), 1.3, dash=True)
    f.thin((A[0], B[1]), (C[0] + 20, B[1]), 1.3, dash=True)
    f.thin((A[0], C[1]), (C[0] + 20, C[1]), 1.3, dash=True)
    for p in (A, B, C):
        f.thin((p[0], A[1]), (p[0], 168), 1.3, dash=True)
    pts = []
    for i in range(0, 61):
        s = -0.45 + i * (2.55 + 0.45) / 60
        x = A[0] + s * dxm * k
        y = A[1] + (10 * s * s + 20 * s) * 1.0 + 0.0
        pts.append((x, y))
    # y(s) 的单位是像素：A、B、C 对应 s=0,1,2 → 0,30,80
    f.path(pts, 2.4, dash=True)
    for p, lab in ((A, "A"), (B, "B"), (C, "C")):
        f.dot(p[0], p[1], 4.4)
        f.t(p[0] + 10, p[1] - 8, lab, 15, "start")
    f.dim((A[0], 172), (B[0], 172), "0.30 m", lp=(0, 18))
    f.dim((B[0], 172), (C[0], 172), "0.30 m", lp=(0, 18))
    f.dim((C[0] + 30, A[1]), (C[0] + 30, B[1]), None)
    f.t(C[0] + 38, (A[1] + B[1]) / 2 + 5, "0.15 m", 13, "start")
    f.dim((C[0] + 30, B[1]), (C[0] + 30, C[1]), None)
    f.t(C[0] + 38, (B[1] + C[1]) / 2 + 5, "0.25 m", 13, "start")
    return f.svg()


def balls_AB():
    gy = 190
    f = Fig(300, 215)
    f.ground(14, 286, gy)
    f.ln((16, 48), (110, 48), 2.6)
    top = 40
    xb, xa0 = 46, 90
    for sfrac in (0.5, 0.72, 0.88):
        y = top + (gy - top) * sfrac ** 2
        xa = xa0 + 160 * sfrac
        f.thin((xb, y), (xa, y), 1.2, dash=True)
        f.ring(xb, y, 5, 1.6, op=0.2)
        f.ring(xa, y, 5, 1.6, op=0.2)
    pts = [(xa0 + 160 * s, top + (gy - top) * s * s) for s in [i / 40.0 for i in range(41)]]
    f.path(pts, 2.0, dash=True)
    f.thin((xb, top), (xb, gy), 1.8, dash=True)
    f.ring(xb, top, 8, op=0.25)
    f.ring(xa0, top, 8, op=0.25)
    f.t(xb - 14, top + 5, "B", 15, "end")
    f.t(xa0 + 2, top - 14, "A", 15)
    f.arr((xa0 + 12, top), (xa0 + 56, top), 2.0)
    return f.svg()


def tower_projectile(H, v0, k, vlabel, hlabel, xq=True):
    g = 10.0
    t = math.sqrt(2 * H / g)
    X = v0 * t
    gy = 58 + H * k
    x0 = 112
    W = x0 + X * k + 40
    f = Fig(W, gy + 46)
    f.ground(14, W - 10, gy)
    f.box(60, gy - H * k, 52, H * k, None, op=0.08)
    pts = sample(lambda s: x0 + v0 * s * k, lambda s: (gy - H * k) + 0.5 * g * s * s * k, 0, t, 50)
    near(pts[-1][1], gy, 1e-6, "落地高度")
    f.path(pts, 2.4, dash=True)
    f.ring(x0, gy - H * k, 6, op=0.25)
    f.arr((x0 + 8, gy - H * k - 14), (x0 + 58, gy - H * k - 14), 2.2)
    f.t(x0 + 33, gy - H * k - 24, vlabel, 14)
    f.dim((46, gy - H * k), (46, gy), hlabel, lp=(-26, 5))
    f.dot(pts[-1][0], gy, 3.6)
    if xq:
        f.dim((x0, gy + 22), (pts[-1][0], gy + 22), "水平距离 x", lp=(0, 18))
        f.thin((x0, gy + 6), (x0, gy + 28), 1.2, dash=True)
        f.thin((pts[-1][0], gy + 6), (pts[-1][0], gy + 28), 1.2, dash=True)
    return f.svg()


def slope_throw():
    v0, g = 8.0, 10.0
    tan = 0.75
    t = 2 * v0 * tan / g
    near(t, 1.2, 1e-9, "飞行时间")
    k = 14.0
    T = (50, 40)
    f = Fig(300, 225)
    L = 200
    gy = T[1] + L * tan
    B = (T[0] + L, gy)
    f.poly([T, (T[0], gy), B], 0.08, 2.6)
    f.ground(20, 280, gy, hatch=True)
    pts = sample(lambda s: T[0] + v0 * s * k, lambda s: T[1] + 0.5 * g * s * s * k, 0, t, 40)
    landing = pts[-1]
    near((landing[1] - T[1]) / (landing[0] - T[0]), tan, 1e-9, "落点在斜面上")
    f.path(pts, 2.4, dash=True)
    f.dot(*landing, 4)
    f.ring(T[0], T[1] - 7, 6, op=0.25)
    f.arr((T[0] + 8, T[1] - 14), (T[0] + 62, T[1] - 14), 2.2)
    f.t(T[0] + 36, T[1] - 24, "8 m/s", 14)
    f.angle(T, B, (B[0] - 60, gy), 46, "37°", 14, 14)
    return f.svg()


def oblique(v_label="50 m/s", ang=37, mark_top=True):
    v0, g = 50.0, 10.0
    th = math.radians(ang)
    R = v0 * v0 * math.sin(2 * th) / g
    Hm = (v0 * math.sin(th)) ** 2 / (2 * g)
    k = 1.25
    x0, gy = 34, 110
    f = Fig(x0 + R * k + 36, 175)
    f.ground(14, x0 + R * k + 24, gy)
    pts = sample(lambda s: x0 + v0 * math.cos(th) * s * k, lambda s: gy - (v0 * math.sin(th) * s - 0.5 * g * s * s) * k,
                 0, 2 * v0 * math.sin(th) / g, 60)
    near(pts[-1][1], gy, 1e-6, "落点同高")
    f.path(pts, 2.4, dash=True)
    e = (x0 + 60 * math.cos(th), gy - 60 * math.sin(th))
    f.arr((x0, gy), e, 2.6)
    f.t(e[0] - 6, e[1] - 6, v_label, 14, "end")
    f.angle((x0 + 70, gy), (x0, gy), e, 36, "%d°" % ang, 14, 14)
    if mark_top:
        top = (x0 + R * k / 2, gy - Hm * k)
        f.dot(*top, 4)
        f.t(top[0], top[1] - 12, "最高点", 14)
    f.dim((x0, gy + 24), (x0 + R * k, gy + 24), "射程", lp=(0, 18))
    return f.svg()


def oblique_two_angles():
    L = 300.0
    x0, gy = 30, 150
    R = L * math.sin(math.radians(60))
    near(L * math.sin(math.radians(120)), R, 1e-9, "两个射程相等")
    f = Fig(x0 + R + 40, 180)
    f.ground(14, x0 + R + 30, gy)
    for deg, rr in ((30, 78), (60, 52)):
        th = math.radians(deg)
        pts = []
        for i in range(61):
            x = R * i / 60
            y = x * math.tan(th) - x * x / (2 * L * math.cos(th) ** 2)
            pts.append((x0 + x, gy - y))
        near(pts[-1][1], gy, 1e-6, "落点同高 %d°" % deg)
        f.path(pts, 2.4, dash=(deg == 30))
        e = (x0 + 54 * math.cos(th), gy - 54 * math.sin(th))
        f.angle((x0 + 90, gy), (x0, gy), e, 30 if deg == 60 else 52)
        top = (x0 + R / 2, gy - L * math.sin(th) ** 2 / 2)
        f.t(top[0], top[1] - 8, "%d°" % deg, 14)
    return f.svg()


# ---------------------------------------------------------------- 圆周
def belt(r1, r2, l1, l2, d=150):
    c1, c2 = (80, 90), (80 + d, 90)
    W, H = c2[0] + r2 + 50, 180
    f = Fig(W, H)
    cs = (r1 - r2) / d
    sn = math.sqrt(1 - cs * cs)
    for sgn in (-1, 1):
        nx, ny = cs, sgn * sn
        p1 = (c1[0] + r1 * nx, c1[1] + r1 * ny)
        p2 = (c2[0] + r2 * nx, c2[1] + r2 * ny)
        f.ln(p1, p2, 2.4)
    f.ring(c1[0], c1[1], r1, op=0.1)
    f.ring(c2[0], c2[1], r2, op=0.1)
    f.dot(*c1, 3.4)
    f.dot(*c2, 3.4)
    f.t(c1[0], c1[1] + r1 + 22, l1, 14)
    f.t(c2[0], c1[1] + r1 + 22, l2, 14)
    near(r1 / r2, round(r1 / r2), 1e-9, "半径比为整数")
    return f.svg()


def turntable(dist=False):
    f = Fig(290, 190)
    f.ground(60, 220, 166)
    f.ln((140, 166), (140, 112), 4.0)
    f.box(40, 100, 200, 12, None, op=0.2)
    f.box(188, 76, 26, 24, None, op=0.3)
    f.thin((140, 52), (140, 100), 1.5, dash=True)
    f.raw('<path d="M 98 62 A 42 12 0 0 1 182 62" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" marker-end="url(#%s)"/>' % f._marker())
    f.t(140, 40, "匀速转动", 13)
    if dist:
        f.thin((201, 104), (201, 138), 1.2, dash=True)
        f.thin((140, 118), (140, 138), 1.2, dash=True)
        f.dim((140, 134), (201, 134), "0.5 m", lp=(0, 18))
    return f.svg()


def top_car_curve():
    f = Fig(250, 215)
    O = (100, 106)
    R = 70
    f.raw('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="6 5"/>' % (n(O[0]), n(O[1]), n(R)))
    f.dot(*O, 3.6)
    f.t(O[0] - 8, O[1] + 18, "O", 14, "end")
    f.thin(O, (O[0] + R, O[1]), 1.6)
    f.t(O[0] + R / 2, O[1] - 8, "20 m", 14)
    f.box(O[0] + R - 8, O[1] - 15, 16, 30, None, op=0.3)
    f.arr((O[0] + R + 22, O[1]), (O[0] + R + 22, O[1] - 44), 2.0)
    return f.svg()


def top_ball_string():
    f = Fig(250, 215)
    O = (100, 108)
    R = 70
    f.raw('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="6 5"/>' % (n(O[0]), n(O[1]), n(R)))
    f.dot(*O, 3.6)
    f.t(O[0] - 8, O[1] + 18, "O", 14, "end")
    f.ln(O, (O[0] + R - 9, O[1]), 2.0)
    f.thin((O[0] + R / 2 - 6, O[1] - 7), (O[0] + R / 2 + 6, O[1] + 7), 2.0)
    f.thin((O[0] + R / 2 + 6, O[1] - 7), (O[0] + R / 2 - 6, O[1] + 7), 2.0)
    f.t(O[0] + R / 2, O[1] + 24, "细线", 13)
    f.ring(O[0] + R, O[1], 9, op=0.25)
    f.arr((O[0] + R, O[1] - 14), (O[0] + R, O[1] - 60), 2.4)
    f.t(O[0] + R + 10, O[1] - 38, "v", 15, "start")
    return f.svg()


def bridge(convex, r_label, v_label):
    R = 110
    W = 300
    cx = 150
    if convex:
        cy = 70 + R + 6
        f = Fig(W, cy + 24)
        pts = [(cx + dx, cy - math.sqrt(R * R - dx * dx)) for dx in range(-96, 97, 4)]
        base = cy - 24
        f.fillpath(pts + [(cx + 96, cy + 12), (cx - 96, cy + 12)], 0.1)
        f.path(pts, 2.8)
        top = (cx, cy - R)
        f.box(cx - 20, top[1] - 20, 40, 20, None, op=0.25)
        f.thin(top, (cx, cy), 1.6, dash=True)
        f.dot(cx, cy, 3.6)
        f.t(cx - 8, cy + 18, "O", 14, "end")
        f.t(cx + 8, (top[1] + cy) / 2 + 5, r_label, 14, "start")
        f.arr((cx + 24, top[1] - 10), (cx + 76, top[1] - 10), 2.2)
        f.t(cx + 50, top[1] - 20, v_label, 14)
    else:
        cy = 8
        low = cy + R
        f = Fig(W, low + 50)
        pts = [(cx + dx, cy + math.sqrt(R * R - dx * dx)) for dx in range(-96, 97, 4)]
        f.fillpath(pts + [(cx + 96, low + 30), (cx - 96, low + 30)], 0.1)
        f.path(pts, 2.8)
        f.box(cx - 20, low - 20, 40, 20, None, op=0.25)
        f.thin((cx, low), (cx, cy), 1.6, dash=True)
        f.dot(cx, cy, 3.6)
        f.t(cx - 8, cy + 14, "O", 14, "end")
        f.t(cx - 8, (low + cy) / 2 + 5, r_label, 14, "end")
        f.arr((cx + 24, low - 30), (cx + 76, low - 30), 2.2)
        f.t(cx + 50, low - 40, v_label, 14)
    return f.svg()


def vertical_circle():
    f = Fig(270, 215)
    O = (130, 116)
    R = 80
    f.raw('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="6 5"/>' % (n(O[0]), n(O[1]), n(R)))
    f.ln(O, (O[0], O[1] - R + 9), 2.0)
    f.dot(*O, 3.6)
    f.t(O[0] - 8, O[1] + 18, "O", 14, "end")
    f.ring(O[0], O[1] - R, 9, op=0.25)
    f.arr((O[0] + 16, O[1] - R), (O[0] + 72, O[1] - R), 2.4)
    f.t(O[0] + 50, O[1] - R - 12, "6 m/s", 14)
    f.t(O[0] - 8, O[1] - R / 2 + 5, "0.9 m", 14, "end")
    return f.svg()


# ---------------------------------------------------------------- 天体
def kepler():
    a, b = 118.0, 74.0
    c = math.sqrt(a * a - b * b)
    cx, cy = 170, 100
    f = Fig(340, 180)
    f.raw('<ellipse cx="%s" cy="%s" rx="%s" ry="%s" fill="none" stroke="currentColor" stroke-width="2.2"/>' % (n(cx), n(cy), n(a), n(b)))
    sun = (cx + c, cy)
    f.ring(sun[0], sun[1], 8, op=0.5)
    f.t(sun[0], sun[1] - 14, "太阳", 14)
    f.dot(cx + a, cy, 3.4)
    f.dot(cx - a, cy, 3.4)
    f.t(cx + a + 8, cy + 5, "近日点", 13, "start")
    f.t(cx - a - 8, cy + 5, "远日点", 13, "end")
    ph = math.radians(112)
    P = (cx + a * math.cos(ph), cy - b * math.sin(ph))
    f.ring(P[0], P[1], 6, op=0.4)
    tx, ty = -a * math.sin(ph), -b * math.cos(ph)
    ux, uy = D.unit(tx, ty)
    f.arr((P[0] + ux * 9, P[1] + uy * 9), (P[0] + ux * 52, P[1] + uy * 52), 2.0)
    f.t(P[0] + 8, P[1] - 12, "行星", 13, "start")
    return f.svg()


def earth_two_distances():
    f = Fig(300, 200)
    O = (60, 80)
    R = 44
    f.ring(O[0], O[1], R, op=0.14)
    f.dot(*O, 3.2)
    P1 = (O[0] + R, O[1])
    P2 = (O[0] + 2 * R, O[1])
    f.thin(O, P2, 1.6)
    f.ring(P1[0], P1[1], 5, op=0.5)
    f.ring(P2[0], P2[1], 5, op=0.5)
    f.t(P1[0] - 6, P1[1] - 16, "400 N", 14, "end")
    f.t(P2[0] + 8, P2[1] - 16, "F = ?", 14, "start")
    f.dim((O[0], 150), (P1[0], 150), "R", lp=(0, 17))
    f.dim((O[0], 176), (P2[0], 176), "2R", lp=(0, 17))
    for p in (O, P1, P2):
        f.thin((p[0], O[1] + (R if p is O else 8)), (p[0], 182), 1.2, dash=True)
    return f.svg()


def orbit_2R():
    f = Fig(260, 240)
    O = (90, 84)
    R = 32
    f.ring(O[0], O[1], R, op=0.14)
    f.raw('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="6 5"/>' % (n(O[0]), n(O[1]), n(2 * R)))
    f.dot(*O, 3.2)
    S = (O[0] + 2 * R, O[1])
    f.ring(S[0], S[1], 6, op=0.5)
    f.t(S[0] + 14, S[1] + 5, "卫星", 13, "start")
    f.thin(O, S, 1.4)
    f.dim((O[0], 172), (O[0] + R, 172), "R", lp=(0, 17))
    f.dim((O[0], 206), (S[0], 206), "2R", lp=(0, 17))
    for x in (O[0], O[0] + R, S[0]):
        f.thin((x, O[1] + (R if x == O[0] else 6)), (x, 212 if x != O[0] + R else 178), 1.2, dash=True)
    return f.svg()


def orbit_AB():
    f = Fig(280, 270)
    O = (140, 135)
    rA, rB = 32, 128
    f.ring(O[0], O[1], 12, op=0.4)
    for r in (rA, rB):
        f.raw('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="6 5"/>' % (n(O[0]), n(O[1]), n(r)))
    near(rB / rA, 4.0, 1e-9, "轨道半径比")
    f.thin(O, (O[0] + rB, O[1]), 1.4)
    f.ring(O[0] + rA, O[1], 5, op=0.6)
    f.ring(O[0] + rB, O[1], 5, op=0.6)
    f.t(O[0] + rA + 10, O[1] - 10, "A", 14, "start")
    f.t(O[0] + rB - 10, O[1] - 10, "B", 14, "end")
    f.t(O[0] + (12 + rA) / 2 - 2, O[1] - 8, "r", 13)
    f.t(O[0] + (rA + rB) / 2, O[1] + 34, "4r", 13)
    return f.svg()


# ---------------------------------------------------------------- 功、能
def height_ball(mass, dim_label, ref_text):
    f = Fig(250, 225)
    gy = 200
    k = 24.0
    f.ground(20, 230, gy)
    y = gy - 5 * k
    f.ring(130, y, 14, op=0.2)
    f.t(160, y + 5, mass, 14, "start")
    f.thin((50, y), (116, y), 1.4, dash=True)
    f.dim((50, y), (50, gy), dim_label, lp=(-26, 5))
    f.t(150, gy - 8, "参考平面", 13, "start")
    return f.svg()


def table_ball():
    f = Fig(340, 235)
    gy = 206
    k = 100.0
    ty = gy - 0.8 * k
    f.ground(14, 326, gy)
    f.box(90, ty, 160, 10, None, op=0.2)
    f.ln((104, ty + 10), (104, gy), 2.4)
    f.ln((236, ty + 10), (236, gy), 2.4)
    by = ty - 0.5 * k
    f.ring(170, by, 8, op=0.3)
    f.t(170, by - 16, "1 kg", 13)
    f.thin((170, by), (290, by), 1.3, dash=True)
    f.thin((250, ty), (290, ty), 1.3, dash=True)
    f.dim((290, by), (290, ty), None)
    f.t(298, (by + ty) / 2 + 5, "0.5 m", 13, "start")
    f.dim((64, ty), (64, gy), None)
    f.t(56, (ty + gy) / 2 + 5, "0.8 m", 13, "end")
    return f.svg()


def graph_spring_work():
    f = Fig(270, 190)
    ox, oy = 50, 152
    axes(f, ox, oy, 200, 130, "x/m", "F/N")
    p = (ox + 160, oy - 100)
    f.fillpath([(ox, oy), p, (p[0], oy)], 0.18)
    f.ln((ox, oy), p, 3.0)
    f.thin(p, (p[0], oy), 1.5, dash=True)
    f.thin(p, (ox, p[1]), 1.5, dash=True)
    f.t(p[0], oy + 20, "0.1", 14)
    f.t(ox - 8, p[1] + 5, "20", 14, "end")
    return f.svg()


def ball_spring_floor():
    f = Fig(250, 215)
    gy = 192
    f.ground(60, 190, gy)
    f.spring((125, gy), (125, 112), turns=7, amp=14, lead=8)
    f.ring(125, 52, 15, op=0.2)
    f.t(125, 57, "m", 14)
    f.arr((125, 74), (125, 100), 2.2)
    return f.svg()


def quarter_circle():
    R = 80.0
    O = (190, 56)
    A = (O[0] - R, O[1])
    Bp = (O[0], O[1] + R)
    gy = Bp[1]
    f = Fig(300, 170)
    arc = [(O[0] - R * math.cos(math.radians(a)), O[1] + R * math.sin(math.radians(a))) for a in range(0, 91, 3)]
    f.fillpath(arc + [(A[0], gy)], 0.12)
    f.path(arc, 2.8)
    f.ln((A[0], gy), (A[0], A[1]), 2.4)
    f.ground(A[0], 286, gy)
    f.ring(A[0] + 9, A[1] + 2, 8, op=0.3)
    f.thin(O, A, 1.6)
    f.dot(*O, 3.4)
    f.t(O[0] + 8, O[1] - 6, "O", 14, "start")
    f.t((O[0] + A[0]) / 2 + 12, O[1] - 8, "R = 0.8 m", 13)
    return f.svg()


# ---------------------------------------------------------------- 振动
def oscillator(blk_dx, extremes=False, arrow_left=False, dim_cm=None, k_label=None, m_label=None, dims_both=None):
    W = 340
    xO = 176
    f = Fig(W, 150)
    gy = 112
    f.wall(24, 52, gy, side=-1)
    f.ground(24, 322, gy)
    bw = 44
    bx = xO + blk_dx - bw / 2
    f.spring((24, gy - 23), (bx, gy - 23), turns=7, lead=8)
    f.box(bx, gy - 46, bw, 46, None)
    if m_label:
        f.t(bx + bw + 8, gy - 18, m_label, 13, "start")
    f.thin((xO, 40), (xO, gy + 14), 1.4, dash=True)
    f.t(xO, gy + 30, "O", 14)
    if extremes:
        for s in (-1, 1):
            x = xO + s * 70
            f.thin((x, 54), (x, gy + 14), 1.4, dash=True)
    if arrow_left:
        f.arr((bx + bw / 2, gy - 58), (bx + bw / 2 - 40, gy - 58), 2.2)
    if dim_cm:
        f.dim((xO, 38), (xO + blk_dx, 38), dim_cm, lp=(0, -9))
    if dims_both:
        k = dims_both[0]
        for s in (-1, 1):
            f.dim((xO, 38), (xO + s * k, 38), None)
        f.t(xO + k / 2, 30, dims_both[1], 13)
        f.t(xO - k / 2, 30, dims_both[1], 13)
    if k_label:
        f.t((24 + bx) / 2, gy - 38, k_label, 13)
    return f.svg()


def osc_vertical():
    f = Fig(280, 180)
    f.ceiling(70, 170, 16)
    f.spring((120, 16), (120, 96), turns=7, lead=8)
    f.box(95, 96, 50, 36, "0.5 kg", 13)
    f.t(138, 60, "k = 100 N/m", 13, "start")
    f.arr((200, 114), (200, 80), 2.0)
    f.arr((200, 114), (200, 148), 2.0)
    f.t(212, 118, "上下振动", 13, "start")
    return f.svg()


def sine_plot_q2():
    f = Fig(280, 170)
    ox, oy = 44, 86
    axes(f, ox, oy, 222, 70, "t/s", "x/cm")
    k_t, k_x = 200.0, 10.0
    pts = [(ox + k_t * t, oy - 5 * k_x * math.sin(4 * math.pi * t + math.pi / 2)) for t in [i * 0.75 / 120 for i in range(121)]]
    near(pts[0][1], oy - 50, 1e-6, "t=0 时在正向最大位移")
    f.path(pts, 2.8)
    f.thin((ox + 100, oy - 6), (ox + 100, oy + 6), 1.6)
    f.t(ox + 100, oy + 22, "0.5", 13)
    f.thin((ox - 4, oy - 50), (ox + 4, oy - 50), 1.6)
    f.t(ox - 8, oy - 45, "5", 13, "end")
    f.thin((ox - 4, oy + 50), (ox + 4, oy + 50), 1.6)
    f.t(ox - 8, oy + 55, "-5", 13, "end")
    return f.svg()


def sine_plot_q3():
    f = Fig(290, 175)
    ox, oy = 44, 88
    axes(f, ox, oy, 236, 76, "t/s", "x/cm")
    k_t, k_x = 100.0, 7.0
    fx = lambda t: 8 * math.sin(math.pi * t + math.pi / 6)
    pts = [(ox + k_t * t, oy - k_x * fx(t)) for t in [i * 2.2 / 120 for i in range(121)]]
    f.path(pts, 2.8)
    f.thin((ox + k_t, oy - 6), (ox + k_t, oy + 6), 1.6)
    f.t(ox + k_t, oy - 12, "1", 13)
    f.thin((ox + k_t, oy), (ox + k_t, oy - k_x * fx(1.0)), 1.4, dash=True)
    f.dot(ox + k_t, oy - k_x * fx(1.0), 4)
    for v in (8, -8):
        f.thin((ox - 4, oy - k_x * v), (ox + 4, oy - k_x * v), 1.6)
        f.t(ox - 8, oy - k_x * v + 5, str(v), 13, "end")
    return f.svg()


def pendulum():
    f = Fig(250, 190)
    P = (110, 16)
    f.ceiling(60, 170, P[1])
    th = math.radians(10)
    L = 130
    B = (P[0] + L * math.sin(th), P[1] + L * math.cos(th))
    f.thin(P, (P[0], P[1] + L + 28), 1.4, dash=True)
    f.ln(P, B, 2.2)
    f.ring(B[0], B[1], 10, op=0.3)
    f.angle((P[0], P[1] + 90), P, B, 50, "θ", 14, 12)
    f.t(P[0] - 14, P[1] + L / 2 + 5, "摆长 1.00 m", 13, "end")
    return f.svg()


# ---------------------------------------------------------------- 波
def wave_profile(lam_label, amp_label=None, crest_dim=None):
    f = Fig(370, 140)
    oy = 74
    lam, A = 100.0, 32.0
    x0 = 30
    pts = [(x0 + i * 3, oy - A * math.sin(2 * math.pi * (i * 3) / lam)) for i in range(0, 110)]
    f.thin((x0 - 6, oy), (x0 + 330, oy), 1.3, dash=True)
    f.path(pts, 2.8)
    c1 = (x0 + lam / 4, oy - A)
    c2 = (x0 + lam * 5 / 4, oy - A)
    if crest_dim:
        f.dot(*c1, 3.8)
        f.dot(*c2, 3.8)
        f.dim((c1[0], c1[1] - 16), (c2[0], c2[1] - 16), crest_dim, lp=(0, -9))
        f.thin(c1, (c1[0], c1[1] - 20), 1.2, dash=True)
        f.thin(c2, (c2[0], c2[1] - 20), 1.2, dash=True)
    else:
        f.dim((c1[0], c1[1] - 16), (c2[0], c2[1] - 16), lam_label, lp=(0, -9))
        f.thin(c1, (c1[0], c1[1] - 20), 1.2, dash=True)
        f.thin(c2, (c2[0], c2[1] - 20), 1.2, dash=True)
        f.dim((c2[0] + 40, oy), (c2[0] + 40, c2[1]), amp_label, lp=(14, 5))
        f.thin(c2, (c2[0] + 46, c2[1]), 1.2, dash=True)
    return f.svg()


def wave_P():
    f = Fig(340, 180)
    ox, oy = 40, 78
    axes(f, ox, oy, 280, 70, "x", "y")
    lam, A = 140.0, 44.0
    pts = [(ox + i * 2.5, oy - A * math.sin(2 * math.pi * (i * 2.5) / lam)) for i in range(0, 106)]
    f.path(pts, 2.8)
    P = (ox + lam / 8, oy - A * math.sin(math.pi / 4))
    f.dot(*P, 4.4)
    f.t(P[0] + 6, P[1] - 10, "P", 15, "start")
    f.thin((ox + lam / 8, oy), P, 1.3, dash=True)
    f.t(ox + lam / 8 + 2, oy + 20, "λ/8", 13)
    f.thin((ox + lam, oy - 5), (ox + lam, oy + 5), 1.6)
    f.t(ox + lam, oy + 20, "λ", 14)
    f.arr((120, 160), (190, 160), 2.2)
    f.t(205, 165, "传播方向", 13, "start")
    return f.svg()


def wave_and_vibration(kind):
    f = Fig(430, 150)
    oy = 72
    # 左：波形
    ox = 36
    axes(f, ox, oy, 190, 56, "x/m", "y", o_label=True)
    A = 38.0
    if kind == "q3":
        kx = 28.0
        pts = [(ox + kx * x, oy + A * math.cos(2 * math.pi * (x - 1) / 4.0)) for x in [i * 6.2 / 100 for i in range(101)]]
        # 波谷在 x=1、5：y=-A（图中向下）
        near(pts[int(round(1 / 6.2 * 100))][1], oy + A, 1.5, "x=1 处是波谷")
        f.path(pts, 2.6)
        for xm in (1, 5):
            f.dot(ox + kx * xm, oy + A, 3.6)
            f.thin((ox + kx * xm, oy + A), (ox + kx * xm, oy - 4), 1.2, dash=True)
            f.t(ox + kx * xm, oy - 9, str(xm), 13)
    else:
        kx = 36.0
        pts = [(ox + kx * x, oy - A * math.sin(math.pi * x / 2)) for x in [i * 4.5 / 100 for i in range(101)]]
        f.path(pts, 2.6)
        Q = (ox + 2 * kx, oy)
        f.dot(*Q, 4.2)
        f.t(Q[0] + 2, Q[1] - 10, "Q", 15, "start")
        f.t(Q[0], oy + 30, "2", 13)
        f.thin((Q[0], oy + 4), (Q[0], oy + 16), 1.2)
        f.thin((ox + 4 * kx, oy - 5), (ox + 4 * kx, oy + 5), 1.6)
        f.t(ox + 4 * kx, oy + 30, "4", 13)
    # 右：振动图像
    ox2 = 272
    axes(f, ox2, oy, 138, 56, "t/s", "y")
    if kind == "q3":
        kt = 54.0
        Tm = 2.0
        pts = [(ox2 + kt * t, oy - A * math.sin(2 * math.pi * t / Tm)) for t in [i * 2.0 / 100 for i in range(101)]]
        f.path(pts, 2.6)
        f.thin((ox2 + kt * 2, oy - 5), (ox2 + kt * 2, oy + 5), 1.6)
        f.t(ox2 + kt * 2, oy + 20, "2", 13)
    else:
        kt = 250.0
        Tm = 0.4
        pts = [(ox2 + kt * t, oy - A * math.sin(2 * math.pi * t / Tm)) for t in [i * 0.5 / 100 for i in range(101)]]
        near(pts[1][1] - pts[0][1], pts[1][1] - oy, 1e-9, "t=0 在平衡位置")
        expect(pts[1][1] < oy, "Q 起始向 y 正方向（图中向上）运动")
        f.path(pts, 2.6)
        f.thin((ox2 + kt * 0.4, oy - 5), (ox2 + kt * 0.4, oy + 5), 1.6)
        f.t(ox2 + kt * 0.4, oy + 30, "0.4", 13)
    f.t(ox + 80, 140, "波的图像（t = 0）", 13)
    f.t(ox2 + 62, 140, "质点的振动图像" if kind == "q3" else "质点 Q 的振动图像", 13)
    return f.svg()


# ---------------------------------------------------------------- 光学
def refraction_30():
    f = Fig(290, 190)
    y0 = 96
    f.fillpath([(20, y0), (270, y0), (270, 176), (20, 176)], 0.08)
    f.ln((20, y0), (270, y0), 2.4)
    O = (150, y0)
    f.thin((150, 14), (150, 180), 1.4, dash=True)
    f.t(150, 10, "法线", 13)
    f.t(34, 34, "空气", 14, "start")
    f.t(34, 168, "介质", 14, "start")
    i_deg, r_deg = 60, 30
    A = (O[0] - 100 * math.sin(math.radians(i_deg)), O[1] - 100 * math.cos(math.radians(i_deg)))
    Bp = (O[0] + 86 * math.sin(math.radians(r_deg)), O[1] + 86 * math.cos(math.radians(r_deg)))
    f.arr(A, O, 2.4)
    f.ln(O, Bp, 2.4)
    near(D.angle_deg(A, O, (20, y0)), 30, 0.1, "入射光线与界面夹角")
    near(D.angle_deg(Bp, O, (150, 180)), 30, 0.1, "折射角")
    near(math.sin(math.radians(i_deg)) / math.sin(math.radians(r_deg)), math.sqrt(3), 1e-9, "折射率")
    f.angle(A, O, (20, y0), 40, "30°", 13, 16)
    f.angle(Bp, O, (150, 180), 44, "30°", 13, 16)
    return f.svg()


def snell_slab(i_deg, n_idx, y_top, thick):
    i = math.radians(i_deg)
    r = math.asin(math.sin(i) / n_idx)
    return i, r


def pins_slab():
    n_idx = 1.5
    i, r = snell_slab(50, n_idx, 0, 0)
    top, bot = 100, 150
    O = (150, top)
    E = (O[0] + (bot - top) * math.tan(r), bot)
    u_in = (-math.sin(i), -math.cos(i))
    u_out = (math.sin(i), math.cos(i))
    P2 = (O[0] + 36 * u_in[0], O[1] + 36 * u_in[1])
    P1 = (O[0] + 84 * u_in[0], O[1] + 84 * u_in[1])
    P3 = (E[0] + 36 * u_out[0], E[1] + 36 * u_out[1])
    P4 = (E[0] + 84 * u_out[0], E[1] + 84 * u_out[1])
    f = Fig(330, 240)
    f.box(30, top, 270, bot - top, None, op=0.1)
    f.t(312 - 10, top - 6, "aa′", 14, "end")
    f.t(312 - 10, bot + 16, "bb′", 14, "end")
    f.ln(P1, O, 1.8)
    f.ln(O, E, 1.8)
    f.ln(E, P4, 1.8)
    for p, lab, dx in ((P1, "P₁", -10), (P2, "P₂", -10), (P3, "P₃", 10), (P4, "P₄", 10)):
        f.ring(p[0], p[1], 4.4, 1.8, op=0.5)
        f.t(p[0] + dx, p[1] + 4, lab, 14, "end" if dx < 0 else "start")
    near(D.angle_deg(P1, O, (O[0], top - 40)), 50, 0.1, "入射角")
    return f.svg()


def circle_method():
    R = 80.0
    O = (150, 104)
    f = Fig(330, 225)
    f.fillpath([(24, O[1]), (276, O[1]), (276, 212), (24, 212)], 0.08)
    f.ln((24, O[1]), (276, O[1]), 2.4)
    f.thin((O[0], 14), (O[0], 208), 1.4, dash=True)
    f.raw('<circle cx="%s" cy="%s" r="%s" fill="none" stroke="currentColor" stroke-width="1.5"/>' % (n(O[0]), n(O[1]), n(R)))
    dA, dB = 3.6 / 4.0 * R, 2.4 / 4.0 * R
    A = (O[0] - dA, O[1] - math.sqrt(R * R - dA * dA))
    B = (O[0] + dB, O[1] + math.sqrt(R * R - dB * dB))
    near(math.hypot(A[0] - O[0], A[1] - O[1]), R, 1e-6, "A 在圆上")
    near(math.hypot(B[0] - O[0], B[1] - O[1]), R, 1e-6, "B 在圆上")
    near((dA / R) / (dB / R), 1.5, 1e-9, "折射率")
    f.arr(A, O, 2.4)
    f.ln(O, B, 2.4)
    f.thin(A, (O[0], A[1]), 1.5, dash=True)
    f.thin(B, (O[0], B[1]), 1.5, dash=True)
    f.dot(*A, 3.8)
    f.dot(*B, 3.8)
    f.t(A[0] - 8, A[1] - 6, "A", 15, "end")
    f.t(B[0] + 8, B[1] + 14, "B", 15, "start")
    f.t(O[0] - 10, O[1] + 18, "O", 14, "end")
    f.t((A[0] + O[0]) / 2, A[1] - 8, "3.6 cm", 13)
    f.thin((B[0], B[1]), (B[0], 190), 1.2, dash=True)
    f.thin((O[0], B[1]), (O[0], 190), 1.2, dash=True)
    f.dim((O[0], 190), (B[0], 190), "2.4 cm", lp=(0, 17))
    f.t(236, 36, "R = 4.0 cm", 13, "start")
    f.t(34, 34, "空气", 13, "start")
    f.t(34, 170, "玻璃", 13, "start")
    return f.svg()


def slab_bb_far():
    n_idx, i_deg = 1.5, 50
    i, r = snell_slab(i_deg, n_idx, 0, 0)
    top, bot, drawn = 56, 116, 148
    O = (120, top)
    E = (O[0] + (bot - top) * math.tan(r), bot)
    Ep = (E[0] + (drawn - bot) * math.tan(i), drawn)
    r_meas = math.atan2(Ep[0] - O[0], drawn - top)
    expect(r_meas > r, "所画折射角应大于真实折射角")
    expect(math.sin(i) / math.sin(r_meas) < n_idx, "测得折射率应偏小")
    u_in = (-math.sin(i), -math.cos(i))
    P0 = (O[0] + 66 * u_in[0], O[1] + 66 * u_in[1])
    end = (E[0] + 100 * math.sin(i), E[1] + 100 * math.cos(i))
    f = Fig(330, 215)
    f.box(30, top, 270, bot - top, None, op=0.1)
    f.thin((30, bot), (300, bot), 1.4, dash=True)
    f.ln((30, drawn), (300, drawn), 2.0)
    f.t(298, top - 6, "aa′", 14, "end")
    f.t(298, drawn + 17, "bb′（所画）", 13, "end")
    f.t(36, bot + 16, "实际下界面", 13, "start")
    f.arr(P0, O, 2.2)
    f.ln(O, E, 1.6)
    f.ln(E, end, 2.2)
    f.thin(O, Ep, 2.0, dash=True)
    f.dot(*Ep, 3.8)
    f.t(Ep[0] - 8, Ep[1] + 17, "E′", 14, "end")
    f.t(O[0] - 8, O[1] - 6, "O", 14, "end")
    return f.svg()


def liquid_cone():
    k = 90.0
    depth, n_idx = 1.6, 5.0 / 3.0
    C = math.asin(1 / n_idx)
    rr = depth * math.tan(C)
    near(rr, 1.2, 1e-9, "圆的半径应为 1.2 m")
    y0 = 40
    S = (170, y0 + depth * k)
    f = Fig(340, 220)
    f.fillpath([(20, y0), (320 - 30, y0), (320 - 30, 212), (20, 212)], 0.08)
    f.ln((20, y0), (290, y0), 2.4)
    L = (S[0] - rr * k, y0)
    Rr = (S[0] + rr * k, y0)
    f.ln(S, L, 1.8)
    f.ln(S, Rr, 1.8)
    f.thin(S, (S[0], y0), 1.4, dash=True)
    f.dot(*S, 4.4)
    f.t(S[0] - 8, S[1] + 18, "点光源", 13, "end")
    f.t(S[0] + 12, S[1] + 18, "n = 5/3", 13, "start")
    f.dim((S[0], y0 - 14), (Rr[0], y0 - 14), "r = ?", lp=(0, -8))
    f.thin((Rr[0], y0), (Rr[0], y0 - 20), 1.2, dash=True)
    f.dim((310, y0), (310, S[1]), None)
    f.t(302, (y0 + S[1]) / 2 + 5, "1.6 m", 13, "end")
    f.t(34, 62, "液体", 14, "start")
    f.t(34, 28, "空气", 14, "start")
    return f.svg()


def optical_fiber():
    f = Fig(380, 150)
    x1, x2 = 20, 330
    f.box(x1, 40, x2 - x1, 80, None, op=0.06, sw=2.2)
    f.box(x1, 62, x2 - x1, 36, None, op=0.16, sw=2.2)
    tan30 = math.tan(math.radians(30))
    yt, yb = 62, 98
    pts = [(x1, 80)]
    x, y, dirn = x1, 80, 1
    while True:
        ty = yb if dirn > 0 else yt
        dx = abs(ty - y) / tan30
        if x + dx >= x2:
            pts.append((x2, y + dirn * (x2 - x) * tan30))
            break
        x += dx
        y = ty
        pts.append((x, y))
        dirn = -dirn
    f.path(pts, 2.2)
    f.t(x2 + 10, 54, "外套", 14, "start")
    f.t(x2 + 10, 84, "内芯", 14, "start")
    return f.svg()
