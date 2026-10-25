#!/usr/bin/env python3
"""物理示意图的小工具：在 fig_draw 的图元风格之上，加箭头、弹簧、斜面、坐标轴等。
坐标系与 SVG 相同：x 向右，y 向下。只用 currentColor。"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fig_draw as D

n = D.n


class Fig:
    def __init__(self, w, h):
        self.w, self.h = w, h
        self.b = []
        self._defs = None
        self._mid = None

    def _marker(self):
        if self._mid is None:
            self._defs, self._mid = D.defs_arrow()
        return self._mid

    def raw(self, s):
        self.b.append(s)

    # ---- 线
    def ln(self, a, b, sw=2.4, dash=False):
        self.b.append(D.line(a, b, D.hidden(sw) if dash else D.edge(sw)))

    def thin(self, a, b, sw=1.5, dash=False):
        if dash:
            self.b.append(D.line(a, b, 'fill="none" stroke="currentColor" stroke-width="%s" stroke-dasharray="5 4" stroke-linecap="round"' % n(sw)))
        else:
            self.b.append(D.line(a, b, D.thin(sw)))

    def arr(self, a, b, sw=2.2, dash=False):
        mid = self._marker()
        extra = ' stroke-dasharray="6 4"' if dash else ""
        self.b.append('<line x1="%s" y1="%s" x2="%s" y2="%s" fill="none" stroke="currentColor" stroke-width="%s"%s marker-end="url(#%s)"/>' % (
            n(a[0]), n(a[1]), n(b[0]), n(b[1]), n(sw), extra, mid))

    def curve_arr(self, a, c, b, sw=2.2):
        mid = self._marker()
        self.b.append('<path d="M %s %s Q %s %s %s %s" fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round" marker-end="url(#%s)"/>' % (
            n(a[0]), n(a[1]), n(c[0]), n(c[1]), n(b[0]), n(b[1]), n(sw), mid))

    def path(self, pts, sw=2.4, dash=False, close=False):
        d = "M " + " L ".join("%s %s" % (n(x), n(y)) for x, y in pts) + (" Z" if close else "")
        extra = ' stroke-dasharray="6 5"' if dash else ""
        self.b.append('<path d="%s" fill="none" stroke="currentColor" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"%s/>' % (d, n(sw), extra))

    def fillpath(self, pts, op=0.12):
        d = "M " + " L ".join("%s %s" % (n(x), n(y)) for x, y in pts) + " Z"
        self.b.append('<path d="%s" %s/>' % (d, D.face(op)))

    # ---- 文字、点
    def t(self, x, y, s, size=15, anchor="middle"):
        self.b.append(D.text(x, y, s, size, anchor))

    def dot(self, x, y, r=3.2):
        self.b.append(D.circ(x, y, r, 'fill="currentColor"'))

    def ring(self, x, y, r, sw=2.2, op=None):
        if op:
            self.b.append(D.circ(x, y, r, D.face(op)))
        self.b.append(D.circ(x, y, r, D.edge(sw)))

    def box(self, x, y, w, h, label=None, size=14, op=0.12, sw=2.4):
        self.b.append('<rect x="%s" y="%s" width="%s" height="%s" %s/>' % (n(x), n(y), n(w), n(h), D.face(op)))
        self.b.append('<rect x="%s" y="%s" width="%s" height="%s" %s/>' % (n(x), n(y), n(w), n(h), D.edge(sw)))
        if label:
            self.t(x + w / 2, y + h / 2 + size * 0.35, label, size)

    def poly(self, pts, op=0.12, sw=2.4):
        self.b.append(D.poly(pts, D.face(op)))
        self.b.append(D.poly(pts, D.edge(sw)))

    # ---- 地面、墙
    def ground(self, x1, x2, y, hatch=True, sw=2.6):
        self.ln((x1, y), (x2, y), sw)
        if hatch:
            x = x1 + 4
            while x < x2 - 2:
                self.thin((x + 8, y), (x, y + 9), 1.4)
                x += 11

    def wall(self, x, y1, y2, side=-1, sw=2.6):
        """side=-1 表示阴影在左侧。"""
        self.ln((x, y1), (x, y2), sw)
        y = y1 + 4
        while y < y2 - 2:
            self.thin((x, y + 8), (x + side * 9, y), 1.4)
            y += 11

    def ceiling(self, x1, x2, y, sw=2.6):
        self.ln((x1, y), (x2, y), sw)
        x = x1 + 4
        while x < x2 - 2:
            self.thin((x + 8, y), (x, y - 9), 1.4)
            x += 11

    # ---- 标注
    def dim(self, a, b, label=None, size=14, lp=None, tl=6, sw=1.7):
        """尺寸线：两端有短竖线，label 放在中点附近。lp 是相对中点的偏移。"""
        ux, uy = D.unit(b[0] - a[0], b[1] - a[1])
        px, py = -uy, ux
        self.thin(a, b, sw)
        for p in (a, b):
            self.thin((p[0] - px * tl, p[1] - py * tl), (p[0] + px * tl, p[1] + py * tl), sw)
        if label:
            mx, my = (a[0] + b[0]) / 2, (a[1] + b[1]) / 2
            if lp is None:
                lp = (px * -16, py * -16 + size * 0.35) if abs(px) < 0.5 else (-16 if px > 0 else 16, size * 0.35)
            self.t(mx + lp[0], my + lp[1], label, size, "middle")

    def spring(self, a, b, turns=7, amp=7, lead=10, sw=2.2):
        ux, uy = D.unit(b[0] - a[0], b[1] - a[1])
        px, py = -uy, ux
        L = math.hypot(b[0] - a[0], b[1] - a[1])
        s0, s1 = lead, L - lead
        pts = [a, (a[0] + ux * s0, a[1] + uy * s0)]
        m = turns * 2
        for i in range(m):
            s = s0 + (s1 - s0) * (i + 0.5) / m
            sign = 1 if i % 2 == 0 else -1
            pts.append((a[0] + ux * s + px * amp * sign, a[1] + uy * s + py * amp * sign))
        pts.append((a[0] + ux * s1, a[1] + uy * s1))
        pts.append(b)
        self.path(pts, sw)

    def angle(self, a, o, c, r=24, label=None, size=14, extra=14):
        self.b.append(D.angle_arc(a, o, c, r, label, sw=1.8, size=size, extra=extra))

    def right(self, v, p, q, s=11):
        self.b.append(D.right_mark(v, p, q, s, 1.8))

    def svg(self, minw=330):
        body = "".join(self.b)
        w = self.w
        if w < minw:
            body = '<g transform="translate(%s 0)">%s</g>' % (n((minw - w) / 2.0), body)
            w = minw
        return D.svg(w, self.h, (self._defs or "") + body)


class Slope:
    """向右上倾斜的斜面坐标：u 沿斜面向上，v 垂直斜面向外（左上侧）。"""

    def __init__(self, base, deg):
        self.base = base
        self.th = math.radians(deg)
        self.d = (math.cos(self.th), -math.sin(self.th))
        self.nv = (-math.sin(self.th), -math.cos(self.th))

    def P(self, u, v=0.0):
        return (self.base[0] + u * self.d[0] + v * self.nv[0], self.base[1] + u * self.d[1] + v * self.nv[1])

    def block(self, f, u0, u1, hgt, label=None, size=13, label_frac=0.5):
        pts = [self.P(u0, 0), self.P(u1, 0), self.P(u1, hgt), self.P(u0, hgt)]
        f.poly(pts, 0.14, 2.4)
        if label:
            c = self.P((u0 + u1) / 2, hgt * label_frac)
            f.t(c[0], c[1] + size * 0.35, label, size)
        return pts


def sample(fx, fy, t0, t1, k=48):
    return [(fx(t0 + (t1 - t0) * i / k), fy(t0 + (t1 - t0) * i / k)) for i in range(k + 1)]


def axes(f, ox, oy, w, h, xl=None, yl=None, o_label=True):
    f.arr((ox - 4, oy), (ox + w, oy), 2.0)
    f.arr((ox, oy + 4), (ox, oy - h), 2.0)
    if xl:
        f.t(ox + w + 4, oy + 18, xl, 14, "end")
    if yl:
        f.t(ox - 8, oy - h + 6, yl, 14, "end")
    if o_label:
        f.t(ox - 8, oy + 16, "O", 14, "end")


def svg_texts(svg):
    import re
    return re.findall(r">([^<]+)</text>", svg)
