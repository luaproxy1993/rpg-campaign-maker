# Engine-ready assets

A generated picture is a plate. A game asset is a plate that survives the engine.

## Portraits / NPCs

1. Generate or edit on a **flat hot-magenta** field (`#F8138A` family), not a textured rose.
2. Key with `scripts/chroma_key.py` then `scripts/clean_chroma.py` (or the copies in this skill's `scripts/`).
3. Verify on a **checker / the real scene**, not on black. Pink fringe and enclosed holes are bugs.
4. Protect purple cloth, blood, floral pinks: flood from **transparency**, do not hard-key all magenta-ish pixels.
5. Sand/dust clouds mixed into leftover screen: only on desert plates, and only as ground FX — do not leave them in the PNG.

Output: RGBA PNG, binary or feathered alpha, one subject.

## Scenes

Full-bleed painted or photo plates. JPG is fine. Name by place, not by plot (`filling_station.jpg`, not `scene3.jpg`).

## FX — one family per file

Do not ship a global dust overlay.

| Picture | Allowed family |
|---------|----------------|
| Night sky / windshield | Stars in a **sky rect** |
| Desert ground / dawn road | Ground **sand** (y > ~0.6), optional heat haze |
| Interior fluorescent | **Motes in light shafts only** + optional flicker |
| Fire | Embers + smoke + glow |
| Streetlamps | Cone motes + moths at the lamp |
| Blown door / smoke | Smoke, cool window shafts |

Indoor motes that are not in a cone stay invisible. Sand that is not on desert ground does not exist.

Implement as a canvas overlay (`play/fx.js`) behind portraits, above the painted plate. Recipe keyed by **filename**.

## Audio

- Ambience: CC0 / CC-BY / OGA-BY only. Credit in `assets/audio/CREDITS.md`.
- UI confirm: **recorded** click (Kenney organic CC0 or equivalent). Not an oscillator.
- Official game OSTs are out unless the author has a license.

## Clip-library (photo / voice / video beats)

If the sitting has media beats, files go in `assets/media/`. The product rule (UX ≠ pipeline, Candy-class vs sitting, PixVerse) lives in `MEDIA-LAYERS.md`.

## Cache

Bump `?v=` on scripts and image URLs after every visual replace. Browsers keep the pink PNG otherwise.
