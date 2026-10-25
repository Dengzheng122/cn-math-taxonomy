#!/usr/bin/env python3
"""内联 SVG 图元。只使用 currentColor，不引用外网，虚线表示看不见的棱。"""
import math

FONT = 'fill="currentColor" font-family="Noto Sans CJK SC, Noto Sans SC, sans-serif" font-weight="650"'


def n(x):
    v = round(float(x) + 0.0, 1)
    if abs(v - round(v)) < 1e-9:
        return str(int(round(v)))
    return ("%.1f" % v).rstrip("0").rstrip(".")


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def svg(w, h, body):
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %s %s">%s</svg>' % (n(w), n(h), body)


def edge(sw=2.6):
    return 'fill="none" stroke="currentColor" stroke-width="%s" stroke-linejoin="round" stroke-linecap="round"' % n(sw)


def hidden(sw=2.3):
    return 'fill="none" stroke="currentColor" stroke-width="%s" stroke-dasharray="7 5" stroke-linejoin="round" stroke-linecap="round"' % n(sw)


def thin(sw=1.5):
    return 'fill="none" stroke="currentColor" stroke-width="%s" stroke-linecap="round"' % n(sw)


def face(op):
    return 'fill="currentColor" fill-opacity="%s" stroke="none"' % op


def line(a, b, attrs):
    return '<line x1="%s" y1="%s" x2="%s" y2="%s" %s/>' % (n(a[0]), n(a[1]), n(b[0]), n(b[1]), attrs)


def poly(pts, attrs):
    return '<polygon points="%s" %s/>' % (" ".join("%s,%s" % (n(x), n(y)) for x, y in pts), attrs)


def circ(cx, cy, r, attrs):
    return '<circle cx="%s" cy="%s" r="%s" %s/>' % (n(cx), n(cy), n(r), attrs)


def text(x, y, s, size=18, anchor="middle"):
    return '<text x="%s" y="%s" %s font-size="%s" text-anchor="%s">%s</text>' % (
        n(x), n(y), FONT, n(size), anchor, esc(s))


_ids = 0


def _next_id(prefix):
    global _ids
    _ids += 1
    return "%s%d" % (prefix, _ids)


def defs_arrow():
    """返回 (defs 标记, 标记 id)。每张图用不同 id，避免同一页里箭头串台。"""
    mid = _next_id("ah")
    defs = ('<defs><marker id="%s" markerWidth="8" markerHeight="8" refX="7" refY="3.2" orient="auto">'
            '<path d="M0,0.4 L7,3.2 L0,6 Z" fill="currentColor"/></marker></defs>' % mid)
    return defs, mid


def unit(dx, dy):
    L = math.hypot(dx, dy) or 1.0
    return dx / L, dy / L


def tick(a, b, sw=2.4, length=8, shift=0):
    dx, dy = b[0] - a[0], b[1] - a[1]
    ux, uy = unit(dx, dy)
    px, py = -uy, ux
    mx, my = (a[0] + b[0]) / 2 + ux * shift, (a[1] + b[1]) / 2 + uy * shift
    return line((mx - px * length, my - py * length), (mx + px * length, my + py * length), edge(sw))


def right_mark(v, p, q, s=13, sw=2.2):
    ux, uy = unit(p[0] - v[0], p[1] - v[1])
    vx, vy = unit(q[0] - v[0], q[1] - v[1])
    a = (v[0] + ux * s, v[1] + uy * s)
    c = (v[0] + vx * s, v[1] + vy * s)
    b = (a[0] + vx * s, a[1] + vy * s)
    return line(a, b, edge(sw)) + line(b, c, edge(sw))


def angle_deg(a, b, c):
    v1 = (a[0] - b[0], a[1] - b[1])
    v2 = (c[0] - b[0], c[1] - b[1])
    dot = v1[0] * v2[0] + v1[1] * v2[1]
    den = math.hypot(*v1) * math.hypot(*v2)
    cos = max(-1.0, min(1.0, dot / den))
    return math.degrees(math.acos(cos))


def angle_arc(a, b, c, r=24, label=None, sw=2.2, size=16, extra=16):
    """画小于或等于 180° 的那一侧。"""
    a1 = math.atan2(a[1] - b[1], a[0] - b[0])
    a2 = math.atan2(c[1] - b[1], c[0] - b[0])
    d = (a2 - a1) % (2 * math.pi)
    if d > math.pi:
        a1, a2 = a2, a1
        d = (a2 - a1) % (2 * math.pi)
    p1 = (b[0] + r * math.cos(a1), b[1] + r * math.sin(a1))
    p2 = (b[0] + r * math.cos(a1 + d), b[1] + r * math.sin(a1 + d))
    large = 1 if d > math.pi + 1e-4 else 0
    body = '<path d="M %s %s A %s %s 0 %d 1 %s %s" %s/>' % (
        n(p1[0]), n(p1[1]), n(r), n(r), large, n(p2[0]), n(p2[1]), edge(sw))
    if label:
        mid = a1 + d / 2.0
        lx = b[0] + (r + extra) * math.cos(mid)
        ly = b[1] + (r + extra) * math.sin(mid) + size * 0.35
        body += text(lx, ly, label, size)
    return body


# ---------------------------------------------------------------- 立体
def cuboid(L, H, D, lab_l=None, lab_h=None, lab_d=None, ticks=False, sw=2.6, margin=28, bold=None,
           letters=False, mid=None, foot=None, tags=None, face_note=None):
    """斜二测：看得见正面、顶面、右侧。看不见的三条棱用虚线。L 长、H 高、D 深，单位是像素。

    顶点：A 前下左，B 前下右，C 前上右，D 前上左，E 后下左，F 后下右，G 后上右，H 后上左。
    bold / tags 用这些字母。mid 是要标中点 M 的一条棱。虚线表示看不见的棱。
    """
    dx, dy = D * 0.52, -D * 0.40
    left = 10
    if lab_h:
        left = 76
    if letters:
        left = max(left, 26)
    ax = margin + left
    ay = margin + H - dy + (12 if letters else 4)
    A = (ax, ay)
    B = (ax + L, ay)
    C = (ax + L, ay - H)
    Dp = (ax, ay - H)
    E = (ax + dx, ay + dy)
    F = (ax + L + dx, ay + dy)
    G = (ax + L + dx, ay - H + dy)
    Hp = (ax + dx, ay - H + dy)
    names = {"A": A, "B": B, "C": C, "D": Dp, "E": E, "F": F, "G": G, "H": Hp}
    e, hd = edge(sw), hidden(sw)
    body = []
    body.append(poly([A, B, C, Dp], face("0.10")))
    body.append(poly([Dp, C, G, Hp], face("0.20")))
    body.append(poly([B, F, G, C], face("0.15")))
    for a, b_ in ((A, E), (E, F), (E, Hp)):
        body.append(line(a, b_, hd))
    for a, b_ in ((A, B), (B, C), (C, Dp), (Dp, A), (B, F), (F, G), (G, C), (Dp, Hp), (Hp, G)):
        body.append(line(a, b_, e))
    if ticks:
        for a, b_ in ((A, B), (B, C), (Dp, A), (B, F), (F, G), (Dp, Hp)):
            body.append(tick(a, b_, sw=sw, length=7))
    if bold:
        for spec in bold:
            a, b_, dashed = spec[0], spec[1], (len(spec) > 2 and spec[2])
            body.append(line(names[a], names[b_], hidden(sw + 0.8) if dashed else edge(sw + 1.6)))
    if letters:
        for name, p, ox, oy, anc in (
            ("A", A, -2, 16, "end"), ("B", B, 4, 16, "start"),
            ("C", C, 8, 2, "start"), ("D", Dp, -8, 2, "end"),
            ("E", E, -2, 16, "end"), ("F", F, 8, 14, "start"),
            ("G", G, 10, 0, "start"), ("H", Hp, -12, 0, "end"),
        ):
            body.append(text(p[0] + ox, p[1] + oy, name, 15, anc))
    if mid:
        p, q = names[mid[0]], names[mid[1]]
        mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
        body.append(circ(mx, my, 3.6, 'fill="currentColor"'))
        body.append(text(mx, my + 20, "M", 15))
    if tags:
        center = ((A[0] + G[0]) / 2, (Dp[1] + A[1]) / 2)
        for n1, n2, lab in tags:
            p, q = names[n1], names[n2]
            mx, my = (p[0] + q[0]) / 2, (p[1] + q[1]) / 2
            ux, uy = unit(mx - center[0], my - center[1])
            body.append(text(mx + ux * 18, my + uy * 18 + 5, lab, 14))
    if lab_l:
        body.append(text((A[0] + B[0]) / 2, A[1] + 22, lab_l, 16))
    if lab_h:
        body.append(text(A[0] - 12, (A[1] + Dp[1]) / 2 + 5, lab_h, 16, "end"))
    if lab_d:
        mx, my = (B[0] + F[0]) / 2, (B[1] + F[1]) / 2
        body.append(text(mx + 12, my + 16, lab_d, 16, "start"))
    if face_note:
        body.append(text((A[0] + B[0]) / 2, (A[1] + Dp[1]) / 2 + 5, face_note, 15))
    if foot:
        body.append(text((A[0] + B[0]) / 2, A[1] + (44 if lab_l else 26), foot, 15))
    extra_r = 22
    if lab_d or tags:
        extra_r = 108
    if letters:
        extra_r = max(extra_r, 36)
    w = max(G[0], F[0]) + extra_r
    ht = A[1] + 18
    if lab_l or mid:
        ht = max(ht, A[1] + 38)
    if foot:
        ht = max(ht, A[1] + (60 if lab_l else 42))
    if letters:
        ht += 6
    return svg(w, ht, "".join(body))


def _ell_arc(cx, cy, rx, ry, front, attrs):
    """椭圆的前半（靠下）或后半（靠上）。"""
    x1, x2 = cx - rx, cx + rx
    sweep = 1 if front else 0
    return '<path d="M %s %s A %s %s 0 0 %d %s %s" %s/>' % (
        n(x1), n(cy), n(rx), n(ry), sweep, n(x2), n(cy), attrs)


def cylinder(rx=72, ry=22, h=118, r_label=None, h_label=None, base_label=None, sw=2.6, show_radius=False):
    cx, top = rx + 56, 28 + ry
    bot = top + h
    e, hd = edge(sw), hidden(sw)
    body = [
        _ell_arc(cx, bot, rx, ry, False, hd),
        line((cx - rx, top), (cx - rx, bot), e),
        line((cx + rx, top), (cx + rx, bot), e),
        _ell_arc(cx, bot, rx, ry, True, e),
        '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" %s/>' % (n(cx), n(top), n(rx), n(ry), face("0.18")),
        '<ellipse cx="%s" cy="%s" rx="%s" ry="%s" %s/>' % (n(cx), n(top), n(rx), n(ry), e),
    ]
    if show_radius or r_label:
        body.append(line((cx, top), (cx + rx, top), thin(1.6)))
        body.append(circ(cx, top, 2.4, 'fill="currentColor"'))
        if r_label:
            body.append(text(cx + rx * 0.45, top - 8, r_label, 16))
    if h_label:
        body.append(text(cx + rx + 14, (top + bot) / 2 + 5, h_label, 16, "start"))
    if base_label:
        body.append(text(cx, bot + ry + 22, base_label, 16))
    w = cx + rx + (128 if h_label else 36)
    ht = bot + ry + (40 if base_label else 20)
    return svg(w, ht, "".join(body))


def cone(rx=70, ry=20, h=120, r_label=None, h_label=None, l_label=None, base_label=None, sw=2.6):
    cx = rx + 64
    apex = (cx, 26)
    base_y = apex[1] + h
    left = (cx - rx, base_y)
    right = (cx + rx, base_y)
    e, hd = edge(sw), hidden(sw)
    body = [
        _ell_arc(cx, base_y, rx, ry, False, hd),
        line(apex, left, e),
        line(apex, right, e),
        _ell_arc(cx, base_y, rx, ry, True, e),
    ]
    if h_label:
        body.append(line(apex, (cx, base_y), hidden(1.8)))
        body.append(text(cx - 10, (apex[1] + base_y) / 2, h_label, 16, "end"))
    if r_label:
        body.append(line((cx, base_y), right, thin(1.6)))
        body.append(circ(cx, base_y, 2.4, 'fill="currentColor"'))
        body.append(text(cx + rx * 0.48, base_y + ry + 18, r_label, 16))
    if l_label:
        mx = (apex[0] + right[0]) / 2 + 12
        my = (apex[1] + right[1]) / 2
        body.append(text(mx, my, l_label, 16, "start"))
    if base_label:
        body.append(text(cx, base_y + ry + (36 if r_label else 20), base_label, 16))
    w = right[0] + (86 if l_label else 40)
    extra = 18
    if r_label:
        extra = 34
    if base_label:
        extra = 54 if r_label else 36
    ht = base_y + ry + extra
    return svg(w, ht, "".join(body))


def sphere(r=68, sw=2.6, r_label=None, extra_radii=0):
    cx, cy = r + 36, r + 28
    e, hd = edge(sw), hidden(sw)
    ry = r * 0.34
    body = [
        _ell_arc(cx, cy, r * 0.96, ry, False, hd),
        circ(cx, cy, r, e),
        _ell_arc(cx, cy, r * 0.96, ry, True, e),
        # 一条经线：左半虚、右半实
        '<path d="M %s %s A %s %s 0 0 1 %s %s" %s/>' % (
            n(cx), n(cy - r), n(r * 0.42), n(r), n(cx), n(cy + r), hd),
        '<path d="M %s %s A %s %s 0 0 1 %s %s" %s/>' % (
            n(cx), n(cy + r), n(r * 0.42), n(r), n(cx), n(cy - r), e),
    ]
    if r_label or extra_radii:
        body.append(circ(cx, cy, 2.6, 'fill="currentColor"'))
        body.append(line((cx, cy), (cx + r * 0.72, cy - r * 0.28), thin(1.7)))
        if r_label:
            body.append(text(cx + r * 0.28, cy - 8, r_label, 16))
        for i in range(extra_radii):
            ang = math.radians(-20 - i * 38)
            body.append(line((cx, cy), (cx + r * math.cos(ang), cy + r * math.sin(ang)), thin(1.5)))
            body.append(tick((cx, cy), (cx + r * math.cos(ang), cy + r * math.sin(ang)), length=6))
    return svg(cx + r + 28, cy + r + 24, "".join(body))


def prism(sides, rx=58, ry=38, height=96, sw=2.6):
    """正棱柱，顶面朝上，前侧面可见。看不见的棱用虚线。"""
    nside = sides
    rot = math.pi / 2 - math.pi / nside
    cx, top_y = rx + 48, ry + 26
    top = [(cx + rx * math.cos(rot + i * 2 * math.pi / nside),
            top_y + ry * math.sin(rot + i * 2 * math.pi / nside)) for i in range(nside)]
    bot = [(x, y + height) for x, y in top]

    def front_face(i):
        j = (i + 1) % nside
        my = (top[i][1] + top[j][1]) / 2
        return my > top_y + 0.4

    e, hd = edge(sw), hidden(sw)
    body = [poly(top, face("0.18"))]
    for i in range(nside):
        if front_face(i):
            j = (i + 1) % nside
            body.append(poly([top[i], top[j], bot[j], bot[i]], face("0.10")))
    for i in range(nside):
        if not front_face((i - 1) % nside) and not front_face(i):
            body.append(line(top[i], bot[i], hd))
    for i in range(nside):
        if not front_face(i):
            j = (i + 1) % nside
            body.append(line(bot[i], bot[j], hd))
    for i in range(nside):
        j = (i + 1) % nside
        body.append(line(top[i], top[j], e))
    for i in range(nside):
        if front_face((i - 1) % nside) or front_face(i):
            body.append(line(top[i], bot[i], e))
    for i in range(nside):
        if front_face(i):
            j = (i + 1) % nside
            body.append(line(bot[i], bot[j], e))
    w = cx + rx + 40
    ht = top_y + height + ry + 28
    return svg(w, ht, "".join(body))


def pyramid(sw=2.6):
    """四棱锥。底面后两条棱是虚线。"""
    apex = (120, 28)
    A = (46, 150)
    B = (168, 150)
    F = (196, 118)
    E = (74, 118)
    e, hd = edge(sw), hidden(sw)
    body = [
        poly([A, B, F, E], face("0.12")),
        poly([apex, A, B], face("0.08")),
        poly([apex, B, F], face("0.16")),
        line(A, E, hd), line(E, F, hd),
        line(apex, A, e), line(apex, B, e), line(apex, F, e), line(apex, E, e),
        line(A, B, e), line(B, F, e),
    ]
    return svg(230, 180, "".join(body))


def cubes(cells, s=32, sw=2.2):
    """cells: (x 向右, y 向后, z 向上) 的小立方体。"""
    if not cells:
        return svg(40, 40, "")
    dx, dy = s * 0.48, -s * 0.40

    def origin_raw(c):
        return (c[0] * (s + 1) + c[1] * dx, -c[2] * s + c[1] * dy)

    raw = [origin_raw(c) for c in cells]
    min_x = min(o[0] for o in raw)
    max_x = max(o[0] + s + dx for o in raw)
    min_y = min(o[1] - s + dy for o in raw)
    max_y = max(o[1] for o in raw)
    ox0 = 16 - min_x
    oy0 = 16 - min_y

    def origin(c):
        x, y = origin_raw(c)
        return (ox0 + x, oy0 + y)

    e, hd = edge(sw), hidden(sw)
    body = []
    order = sorted(cells, key=lambda c: (-c[1], c[2], c[0]))
    occupied = set(cells)
    for c in order:
        x, y = origin(c)
        A = (x, y)
        B = (x + s, y)
        C = (x + s, y - s)
        Dp = (x, y - s)
        E = (x + dx, y + dy)
        F = (x + s + dx, y + dy)
        G = (x + s + dx, y - s + dy)
        Hp = (x + dx, y - s + dy)
        body.append(poly([A, B, C, Dp], face("0.10")))
        body.append(poly([Dp, C, G, Hp], face("0.22")))
        body.append(poly([B, F, G, C], face("0.16")))
        # 被旁边的块挡住的棱不画虚线，避免乱
        hidden_edges = []
        if (c[0] - 1, c[1] + 1, c[2]) not in occupied and (c[0], c[1] + 1, c[2]) not in occupied:
            hidden_edges.append((A, E))
        if (c[0], c[1] + 1, c[2]) not in occupied:
            hidden_edges.append((E, F))
        if (c[0], c[1] + 1, c[2] + 1) not in occupied and (c[0], c[1] + 1, c[2]) not in occupied:
            hidden_edges.append((E, Hp))
        for a, b_ in hidden_edges:
            body.append(line(a, b_, hd))
        vis = [(A, B), (B, C), (C, Dp), (Dp, A), (B, F), (F, G), (G, C), (Dp, Hp), (Hp, G)]
        for a, b_ in vis:
            body.append(line(a, b_, e))
    max_x = max(origin(c)[0] + s + dx for c in cells) + 16
    max_y = max(origin(c)[1] for c in cells) + 16
    return svg(max_x, max_y, "".join(body))


def net(cells, labels=None, size=46, sw=2.4):
    """cells: (列, 行)，行向下。labels: {(列,行): 文字}。"""
    labels = labels or {}
    cols = [c[0] for c in cells]
    rows = [c[1] for c in cells]
    minc, maxc = min(cols), max(cols)
    minr, maxr = min(rows), max(rows)
    ox, oy = 16, 16
    e = edge(sw)
    body = []
    for c, r in cells:
        x = ox + (c - minc) * size
        y = oy + (r - minr) * size
        body.append('<rect x="%s" y="%s" width="%s" height="%s" %s/>' % (n(x), n(y), n(size), n(size), face("0.12")))
        body.append('<rect x="%s" y="%s" width="%s" height="%s" %s/>' % (n(x), n(y), n(size), n(size), e))
        if (c, r) in labels:
            body.append(text(x + size / 2, y + size / 2 + 7, labels[(c, r)], 20))
    w = ox + (maxc - minc + 1) * size + 16
    h = oy + (maxr - minr + 1) * size + 16
    return svg(w, h, "".join(body))


def sector(deg, r_px=108, r_label=None, ang_label=None, sw=2.6):
    """扇形，顶点在左侧，关于水平线对称。"""
    cx, cy = 36, 130
    half = math.radians(deg / 2.0)
    a1 = -half
    a2 = half
    p1 = (cx + r_px * math.cos(a1), cy + r_px * math.sin(a1))
    p2 = (cx + r_px * math.cos(a2), cy + r_px * math.sin(a2))
    large = 1 if deg > 180 else 0
    e = edge(sw)
    body = [
        '<path d="M %s %s L %s %s A %s %s 0 %d 1 %s %s Z" %s/>' % (
            n(cx), n(cy), n(p1[0]), n(p1[1]), n(r_px), n(r_px), large, n(p2[0]), n(p2[1]), face("0.12")),
        '<path d="M %s %s L %s %s A %s %s 0 %d 1 %s %s Z" %s/>' % (
            n(cx), n(cy), n(p1[0]), n(p1[1]), n(r_px), n(r_px), large, n(p2[0]), n(p2[1]), e),
    ]
    if ang_label:
        body.append(angle_arc(p1, (cx, cy), p2, r=28, label=ang_label, size=16, extra=18))
    if r_label:
        body.append(text((cx + p1[0]) / 2, (cy + p1[1]) / 2 - 10, r_label, 16))
    w = cx + r_px + 28
    h = cy + r_px * math.sin(half) + 28
    return svg(w, max(h, cy + 20), "".join(body))


# ---------------------------------------------------------------- 平面
def _box(x, y, w, h, sw):
    return '<rect x="%s" y="%s" width="%s" height="%s" %s/><rect x="%s" y="%s" width="%s" height="%s" %s/>' % (
        n(x), n(y), n(w), n(h), face("0.12"), n(x), n(y), n(w), n(h), edge(sw))


def shape_rect_plain(sw=3.2):
    return svg(220, 170, _box(26, 42, 168, 86, sw))


shape_rect = shape_rect_plain


def shape_square(sw=3.2, ticks=False):
    x, y, s = 48, 26, 118
    body = _box(x, y, s, s, sw)
    if ticks:
        body += tick((x, y + s), (x + s, y + s), sw=sw) + tick((x + s, y), (x + s, y + s), sw=sw)
        body += tick((x, y), (x + s, y), sw=sw) + tick((x, y), (x, y + s), sw=sw)
    return svg(220, 170, body)


def shape_triangle(sw=3.2):
    pts = [(110, 22), (26, 150), (194, 150)]
    return svg(220, 170, poly(pts, face("0.12")) + poly(pts, edge(sw)))


def shape_circle(sw=3.2, center=True):
    body = circ(110, 86, 64, face("0.1")) + circ(110, 86, 64, edge(sw))
    if center:
        body += circ(110, 86, 3, 'fill="currentColor"')
    return svg(220, 170, body)


def shape_sphere(sw=3.0):
    return sphere(r=62, sw=sw)


def shape_cylinder():
    return cylinder(rx=58, ry=16, h=96, sw=3.0)


def shape_cone():
    return cone(rx=60, ry=16, h=112, sw=3.0)


def shape_cuboid():
    return cuboid(118, 72, 58, sw=3.0, margin=22)


def shape_cube():
    return cuboid(86, 86, 86, ticks=True, sw=3.0, margin=22)


def shape_trapezoid(sw=3.2, iso=False):
    if iso:
        pts = [(60, 46), (160, 46), (190, 140), (30, 140)]
    else:
        pts = [(48, 48), (150, 48), (196, 142), (28, 142)]
    return svg(220, 170, poly(pts, face("0.12")) + poly(pts, edge(sw)))


def shape_parallelogram(sw=3.2):
    pts = [(58, 40), (196, 40), (162, 132), (24, 132)]
    return svg(220, 170, poly(pts, face("0.12")) + poly(pts, edge(sw)))


def shape_iso_triangle(sw=3.2):
    pts = [(110, 22), (36, 152), (184, 152)]
    body = poly(pts, face("0.12")) + poly(pts, edge(sw))
    body += tick(pts[0], pts[1], sw=sw, length=8)
    body += tick(pts[0], pts[2], sw=sw, length=8)
    return svg(220, 170, body)


def shape_right_triangle(sw=3.2):
    """3-4-5 的直角三角形，不是等腰。"""
    C = (40, 142)
    B = (176, 142)
    A = (40, 40)
    body = poly([A, B, C], face("0.12")) + poly([A, B, C], edge(sw)) + right_mark(C, A, B, 16, sw)
    return svg(220, 170, body)


def shape_sector_icon(sw=3.2):
    return sector(120, r_px=120, sw=sw)


def shape_two_circles(sw=3.2):
    body = circ(62, 86, 40, face("0.1")) + circ(62, 86, 40, edge(sw))
    body += circ(150, 86, 40, face("0.1")) + circ(150, 86, 40, edge(sw))
    return svg(220, 170, body)


def two_views_rect(front_w, front_h, left_w, left_h, unit_label="cm"):
    s = 26
    fw, fh = front_w * s, front_h * s
    lw, lh = left_w * s, left_h * s
    gap = 70
    x1, y1 = 36, 48
    x2 = x1 + fw + gap
    body = [
        _box(x1, y1, fw, fh, 2.4),
        _box(x2, y1, lw, lh, 2.4),
        text(x1 + fw / 2, y1 + fh + 24, "主视图", 16),
        text(x1 + fw / 2, y1 - 10, "%s %s" % (n(front_w), unit_label), 15),
        text(x1 - 8, y1 + fh / 2, "%s" % n(front_h), 15, "end"),
        text(x2 + lw / 2, y1 + lh + 24, "左视图", 16),
        text(x2 + lw / 2, y1 - 10, "%s %s" % (n(left_w), unit_label), 15),
        text(x2 + lw + 8, y1 + lh / 2, "%s" % n(left_h), 15, "start"),
    ]
    return svg(x2 + lw + 48, y1 + max(fh, lh) + 48, "".join(body))


def three_views_cylinder():
    """两个相同的矩形加一个圆，不写几何体的名字。"""
    body = [
        _box(24, 36, 70, 90, 2.4),
        text(59, 150, "主视图", 15),
        _box(130, 36, 70, 90, 2.4),
        text(165, 150, "左视图", 15),
        circ(270, 82, 36, face("0.12")),
        circ(270, 82, 36, edge(2.4)),
        text(270, 150, "俯视图", 15),
    ]
    return svg(330, 172, "".join(body))


def top_grid(rows, caption=None):
    """rows: 从上到下、每行从左到右的数字或文字。"""
    s = 54
    nrows = len(rows)
    ncols = max(len(r) for r in rows)
    ox, oy = 28, 36
    body = []
    for r, row in enumerate(rows):
        for c, val in enumerate(row):
            x, y = ox + c * s, oy + r * s
            body.append(_box(x, y, s, s, 2.4))
            body.append(text(x + s / 2, y + s / 2 + 7, str(val), 22))
    w = ox + ncols * s + 24
    h = oy + nrows * s + 16
    if caption:
        body.append(text(ox + ncols * s / 2, h + 8, caption, 16))
        h += 28
    return svg(w, h, "".join(body))


def rotation_arrow(cx, cy, r=18):
    a1, a2 = math.radians(200), math.radians(430)
    p1 = (cx + r * math.cos(a1), cy + r * math.sin(a1))
    p2 = (cx + r * math.cos(a2), cy + r * math.sin(a2))
    defs, mid = defs_arrow()
    return defs + '<path d="M %s %s A %s %s 0 1 1 %s %s" fill="none" stroke="currentColor" stroke-width="2" marker-end="url(#%s)"/>' % (
        n(p1[0]), n(p1[1]), n(r), n(r), n(p2[0]), n(p2[1]), mid)
