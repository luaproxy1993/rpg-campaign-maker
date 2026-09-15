#!/usr/bin/env python3
"""Key near-magenta (and sampled corner chroma) to RGBA PNG."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def is_chroma(r: int, g: int, b: int, cr: int, cg: int, cb: int, tol: int) -> bool:
    if abs(r - cr) <= tol and abs(g - cg) <= tol and abs(b - cb) <= tol:
        return True
    # Magenta / hot-pink family used as generation key.
    if r >= 180 and b >= 180 and g <= 90:
        return True
    if r >= 200 and b >= 140 and g <= 70:
        return True
    # Some gens drift to hot magenta-white.
    if r >= 220 and b >= 180 and g <= 140 and (r + b) - 2 * g > 160:
        return True
    return False


def key_image(src: Path, dst: Path, tol: int = 48) -> dict:
    im = Image.open(src).convert("RGBA")
    w, h = im.size
    pix = im.load()
    samples = [
        pix[0, 0],
        pix[w - 1, 0],
        pix[0, h - 1],
        pix[w - 1, h - 1],
        pix[w // 2, 0],
        pix[0, h // 2],
    ]
    cr = sum(p[0] for p in samples) // len(samples)
    cg = sum(p[1] for p in samples) // len(samples)
    cb = sum(p[2] for p in samples) // len(samples)

    keyed = 0
    for y in range(h):
        for x in range(w):
            r, g, b, a = pix[x, y]
            if is_chroma(r, g, b, cr, cg, cb, tol):
                pix[x, y] = (0, 0, 0, 0)
                keyed += 1
            else:
                # Magenta despill on remaining fringe.
                if r > g + 25 and b > g + 25:
                    g2 = min(255, g + ((r - g) + (b - g)) // 6)
                    r2 = min(255, max(g2, r - 20))
                    b2 = min(255, max(g2, b - 20))
                    pix[x, y] = (r2, g2, b2, a)
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "PNG")
    return {
        "src": str(src),
        "dst": str(dst),
        "size": f"{w}x{h}",
        "corner": (cr, cg, cb),
        "keyed_pct": round(100.0 * keyed / (w * h), 1),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("src")
    p.add_argument("dst")
    p.add_argument("--tol", type=int, default=48)
    args = p.parse_args()
    info = key_image(Path(args.src), Path(args.dst), args.tol)
    print(info)


if __name__ == "__main__":
    main()
