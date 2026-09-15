#!/usr/bin/env python3
"""Remove leftover hot-pink / magenta chroma from RGBA cutouts.

Protects purple cloth, muted floral pinks, and blood. Keys hot-pink screen
plus magenta fringe connected to transparency (or enclosed hot-pink holes).
"""
from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image, ImageDraw


def _hsv(r: int, g: int, b: int) -> tuple[float, float, int]:
    mx = r if r >= g and r >= b else (g if g >= b else b)
    mn = r if r <= g and r <= b else (g if g <= b else b)
    if mx == 0:
        return 0.0, 0.0, 0
    sat = (mx - mn) / mx
    if mx == mn:
        hue = 0.0
    elif mx == r:
        hue = (60.0 * ((g - b) / (mx - mn))) % 360.0
    elif mx == g:
        hue = 60.0 * ((b - r) / (mx - mn) + 2.0)
    else:
        hue = 60.0 * ((r - g) / (mx - mn) + 4.0)
    return hue, sat, mx


def strong_key(r: int, g: int, b: int) -> bool:
    """Obvious chroma-screen hot pink. Must not match dress / roses / blood."""
    if r < 170 or g > 110:
        return False
    if (r - g) < 70:
        return False
    if b < 55:
        return False
    hue, sat, val = _hsv(r, g, b)
    if sat < 0.58 or val < 100:
        return False
    # hot pink / magenta hue band (wraps slightly toward rose)
    if 308.0 <= hue <= 348.0:
        return True
    if hue >= 350.0 and sat >= 0.72 and (r - g) >= 110:
        return True
    return False


def weak_key(r: int, g: int, b: int) -> bool:
    """Magenta fringe / dusty leftover screen, still not fabric or skin."""
    if r < 58 or g > 130:
        return False
    if (r - g) < 36:
        return False
    if b < 32:
        return False
    # reject red blood (B much lower than R, hue near 0)
    if r > 140 and b < 70 and g < 90 and (r - b) > 80:
        return False
    hue, sat, val = _hsv(r, g, b)
    if sat < 0.40 or val < 50:
        return False
    if val < 90 and sat < 0.58:
        # dark purple fabric (D'Espine)
        return False
    return 305.0 <= hue <= 358.0


def dusty_key(r: int, g: int, b: int) -> bool:
    """Bright leftover screen mixed into dust/smoke (young woman sand cloud)."""
    if r < 130 or g > 140:
        return False
    if (r - g) < 24:
        return False
    if b < 60:
        return False
    hue, sat, val = _hsv(r, g, b)
    if sat < 0.30 or val < 110:
        return False
    return hue >= 325.0 or hue <= 10.0


def spray_key(r: int, g: int, b: int) -> bool:
    """Rose/tan dust spray far from the body. Rejects wood, metal, sheer fabric."""
    if is_fillable(r, g, b):
        return True
    if r < 110:
        return False
    if (r - g) < 18:
        return False
    hue, sat, val = _hsv(r, g, b)
    if sat < 0.32 or val < 80 or val > 210:
        return False
    return hue <= 22.0 or hue >= 320.0


def is_fillable(r: int, g: int, b: int) -> bool:
    return strong_key(r, g, b) or weak_key(r, g, b) or dusty_key(r, g, b)


def _largest_component(opaque: bytearray, w: int, h: int) -> bytearray:
    n = w * h
    seen = bytearray(n)
    best: list[int] = []
    for i in range(n):
        if not opaque[i] or seen[i]:
            continue
        q = deque([i])
        seen[i] = 1
        blob = [i]
        while q:
            cur = q.popleft()
            y, x = cur // w, cur % w
            for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= w or ny >= h:
                    continue
                j = ny * w + nx
                if opaque[j] and not seen[j]:
                    seen[j] = 1
                    q.append(j)
                    blob.append(j)
        if len(blob) > len(best):
            best = blob
    keep = bytearray(n)
    min_keep = max(800, int(n * 0.02))
    if len(best) < min_keep:
        return opaque
    for j in best:
        keep[j] = 1
    return keep


def clean(src: Path, dst: Path) -> dict:
    im = Image.open(src).convert("RGBA")
    w, h = im.size
    pix = im.load()
    n = w * h

    keyed = 0
    # 1. hard-key remaining hot pink anywhere (enclosed holes + fields)
    for y in range(h):
        for x in range(w):
            r, g, b, a = pix[x, y]
            if a and strong_key(r, g, b):
                pix[x, y] = (0, 0, 0, 0)
                keyed += 1

    # 2. 8-connected flood from transparent into leftover screen
    q: deque[tuple[int, int]] = deque()
    vis = bytearray(n)
    for y in range(h):
        row = y * w
        for x in range(w):
            if pix[x, y][3] == 0:
                q.append((x, y))
                vis[row + x] = 1
    extra = 0
    nbr = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
    while q:
        x, y = q.popleft()
        for dx, dy in nbr:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx >= w or ny >= h:
                continue
            j = ny * w + nx
            if vis[j]:
                continue
            r, g, b, a = pix[nx, ny]
            if a == 0 or is_fillable(r, g, b):
                vis[j] = 1
                if a:
                    pix[nx, ny] = (0, 0, 0, 0)
                    extra += 1
                q.append((nx, ny))
            else:
                vis[j] = 1

    # 2b. lower-half only: eat rose/tan dust clouds (never touch faces/horns)
    y0 = int(h * 0.50)
    q = deque()
    vis = bytearray(n)
    for y in range(y0, h):
        row = y * w
        for x in range(w):
            if pix[x, y][3] == 0:
                q.append((x, y))
                vis[row + x] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in nbr:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < y0 or nx >= w or ny >= h:
                continue
            j = ny * w + nx
            if vis[j]:
                continue
            r, g, b, a = pix[nx, ny]
            if a == 0 or spray_key(r, g, b):
                vis[j] = 1
                if a:
                    pix[nx, ny] = (0, 0, 0, 0)
                    extra += 1
                q.append((nx, ny))
            else:
                vis[j] = 1

    # 3. erode 3px of magenta-tinted fringe next to transparency
    for _ in range(3):
        kill: list[tuple[int, int]] = []
        for y in range(h):
            for x in range(w):
                r, g, b, a = pix[x, y]
                if a == 0:
                    continue
                if not is_fillable(r, g, b):
                    continue
                if (
                    (x and pix[x - 1, y][3] == 0)
                    or (x + 1 < w and pix[x + 1, y][3] == 0)
                    or (y and pix[x, y - 1][3] == 0)
                    or (y + 1 < h and pix[x, y + 1][3] == 0)
                ):
                    kill.append((x, y))
        for x, y in kill:
            pix[x, y] = (0, 0, 0, 0)
            extra += 1

    # 4. drop specks / torn black frames: keep largest opaque component
    opaque = bytearray(n)
    for y in range(h):
        row = y * w
        for x in range(w):
            if pix[x, y][3]:
                opaque[row + x] = 1
    keep = _largest_component(opaque, w, h)
    specks = 0
    for y in range(h):
        row = y * w
        for x in range(w):
            if pix[x, y][3] and not keep[row + x]:
                pix[x, y] = (0, 0, 0, 0)
                specks += 1

    # 5. despill remaining silhouette edge (do not punch holes)
    for y in range(h):
        for x in range(w):
            r, g, b, a = pix[x, y]
            if a == 0:
                continue
            near = (
                (x and pix[x - 1, y][3] == 0)
                or (x + 1 < w and pix[x + 1, y][3] == 0)
                or (y and pix[x, y - 1][3] == 0)
                or (y + 1 < h and pix[x, y + 1][3] == 0)
            )
            if not near:
                continue
            if r > g + 16 and (b > g + 4 or (r > 170 and b > 70)):
                g2 = min(255, g + ((r - g) + max(0, b - g)) // 5)
                r2 = min(255, max(g2, r - 40))
                b2 = min(255, max(g2, b - 32))
                pix[x, y] = (r2, g2, b2, 255)
            elif a != 255:
                pix[x, y] = (r, g, b, 255)

    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "PNG")
    return {
        "file": str(src.relative_to(src.parents[2]) if len(src.parts) > 2 else src.name),
        "keyed": keyed,
        "extra": extra,
        "specks": specks,
        "size": f"{w}x{h}",
    }


def qa_preview(src: Path, dst: Path) -> None:
    im = Image.open(src).convert("RGBA")
    w, h = im.size
    bg = Image.new("RGBA", (w, h), (32, 140, 72, 255))
    # checker to catch leftover near-black frames
    draw = ImageDraw.Draw(bg)
    cell = 24
    for y in range(0, h, cell):
        for x in range(0, w, cell):
            if ((x // cell) + (y // cell)) % 2 == 0:
                draw.rectangle((x, y, x + cell, y + cell), fill=(18, 110, 58, 255))
    bg.alpha_composite(im)
    dst.parent.mkdir(parents=True, exist_ok=True)
    bg.convert("RGB").save(dst, "JPEG", quality=86)


def main() -> None:
    import argparse
    import sys

    p = argparse.ArgumentParser(description="Clean leftover magenta on RGBA cutouts.")
    p.add_argument(
        "root",
        nargs="?",
        default="assets",
        help="assets directory (default: ./assets)",
    )
    p.add_argument("--qa", action="store_true", help="write checker previews to <root>/_qa")
    args = p.parse_args()
    pack = Path(args.root)
    if not pack.is_dir():
        sys.exit(f"not a directory: {pack}")
    qa = pack / "_qa"
    files: list[Path] = []
    for folder in ("npcs", "enemies", "portraits"):
        d = pack / folder
        if d.is_dir():
            files.extend(sorted(d.rglob("*.png")))
    if not files:
        sys.exit(f"no pngs under {pack}/{{npcs,enemies,portraits}}")
    for f in files:
        info = clean(f, f)
        if args.qa:
            qa_preview(f, qa / f"{f.parent.name}_{f.stem}.jpg")
        print(info, flush=True)


if __name__ == "__main__":
    main()
