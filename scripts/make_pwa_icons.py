#!/usr/bin/env python3
"""用站点 logo（与 favicon 同一图形）和站点配色生成 PWA 图标到 assets/icons/。需要 Pillow。

    python3 scripts/make_pwa_icons.py
"""
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'icons')
BRAND = (15, 110, 98)        # --brand  #0f6e62
SHEET = (223, 243, 239)      # --logo-sheet #dff3ef
WHITE = (255, 255, 255)
SS = 4                       # 超采样倍数


def quad(p0, p1, p2, n=14):
    return [((1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t * t * p2[0],
             (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t * t * p2[1])
            for t in [i / n for i in range(1, n + 1)]]


SHEET_PTS = ([(6.6, 4.8), (17, 4.8), (27.4, 15.2), (27.4, 25)]
             + quad((27.4, 25), (27.4, 27.4), (25.2, 27.4)) + [(6.6, 27.4)]
             + quad((6.6, 27.4), (4.4, 27.4), (4.4, 25.2)) + [(4.4, 7)]
             + quad((4.4, 7), (4.4, 4.8), (6.6, 4.8)))
FOLD_PTS = [(17.7, 6.3), (26.1, 14.7), (17.7, 14.7)]
FOLD_LINE = [(17.7, 6.3), (17.7, 14.7), (26.1, 14.7)]
ARROW_LINE = ([(8.3, 24.2), (12.4, 24.2)] + quad((12.4, 24.2), (14.2, 24.2), (14.2, 22.4))
              + [(14.2, 20.2)] + quad((14.2, 20.2), (14.2, 18.6), (16, 18.6)) + [(18.8, 18.6)])
ARROW_HEAD = [(18.5, 16.85), (23, 18.6), (18.5, 20.35)]


def stroke(d, pts, w, fill, closed=False):
    pts = pts + ([pts[0]] if closed else [])
    d.line(pts, fill=fill, width=int(round(w)), joint='curve')
    r = w / 2
    for x, y in pts:
        d.ellipse([x - r, y - r, x + r, y + r], fill=fill)


def logo_layer(size, logo_px):
    """在 size×size 的透明画布中央画 logo，logo 占 logo_px 像素宽。"""
    s = size * SS
    scale = logo_px * SS / 32.0
    off = (s - 32 * scale) / 2
    T = lambda pts: [(off + x * scale, off + y * scale) for x, y in pts]
    img = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    d.polygon(T(SHEET_PTS), fill=SHEET)
    stroke(d, T(SHEET_PTS), 1.7 * scale, BRAND, closed=True)
    d.polygon(T(FOLD_PTS), fill=WHITE)
    stroke(d, T(FOLD_LINE), 1.35 * scale, BRAND)
    stroke(d, T(ARROW_LINE), 2.15 * scale, BRAND)
    d.polygon(T(ARROW_HEAD), fill=BRAND)
    return img


def make(name, size, logo_frac, radius_frac):
    s = size * SS
    base = Image.new('RGBA', (s, s), (0, 0, 0, 0))
    d = ImageDraw.Draw(base)
    if radius_frac:
        d.rounded_rectangle([0, 0, s - 1, s - 1], radius=int(s * radius_frac), fill=BRAND + (255,))
    else:
        d.rectangle([0, 0, s, s], fill=BRAND + (255,))
    base.alpha_composite(logo_layer(size, size * logo_frac))
    img = base.resize((size, size), Image.LANCZOS)
    path = os.path.join(OUT, name)
    img.save(path, optimize=True)
    print(name, size, os.path.getsize(path), 'bytes')


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    make('icon-192.png', 192, 0.74, 0.22)
    make('icon-512.png', 512, 0.74, 0.22)
    make('icon-maskable-512.png', 512, 0.56, 0)   # 安全区：logo 约占中心 56%
    make('apple-touch-icon.png', 180, 0.70, 0)    # iOS 自己加圆角，需不透明方图
