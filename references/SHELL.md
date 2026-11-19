# Play shell

The shell is the game. A pack of JSON without a playable surface is a design doc.

**Product form decides which shell.** Read `docs/INTENT.md` `product_form` (or the accepted lock if it recorded one) before writing files.

- `doki-mesh-world`: mount a content pack on the **existing DokiDemo GameShell**. The default named shell is `/Users/a123/grokmaker/campaigns/DokiDemo` (or a git worktree of that repo, e.g. `DokiDemo-brew`). The quality bar is frame-by-frame parity with the already-shipped Strahd AVG on that same shell: full-bleed scene plates, dialogue two-shots, intro reel, BGM, HUD. Do **not** create a new `index.html` / walk-look-talk page, even if DokiDemo is missing on this machine — stop and get the shell, don't substitute. Opening a first scene over local HTTP is not done.
- `static-campaign-sitting`: the scaffold below (`index.html` + `play/` + `assets/`) is the shell.
- Leave other product forms alone (`screenshot-first-idle` still uses `game-maker-pipeline`; Godot 2D still uses `build-a-game`).

## Layout

Match the **reference the author pointed at**. If they named a commercial UI (e.g. Shadows of New York), reverse that: full-bleed plate, speaker right, crimson nameplate, CONTINUE, book-icon sheet.

If they named nothing, use the scaffold default: full-bleed bg, speaker right, choices left-bottom, sheet overlay.

## Files

```
index.html          # entry
play/app.js         # runner: node → bg, speaker, text, choices, checks
play/story.js       # tree
play/sheet.js       # dots + items
play/styles.css
play/fx.js          # optional, per-scene recipes
play/audio.js       # optional, CC playlist + click sample
assets/…
mechanics/data/…
```

Serve from the campaign root:

```bash
python3 -m http.server 8767 --bind 127.0.0.1
```

## Original-voice

If the source is English, every player-facing string is English — Marquis-style, not invented Chinese, not LLM-flavored "dark fantasy" paste. Labels on choices stay long when the book wrote them long.

## Speaker slot

Only characters who are **in the room** get `speaker.img`. Flashback faces appear on flashback nodes only.

## Clip-library

If a node has `media`, play the local file (`assets/media/…`). Do not call an API. UX that feels live is still a file on a node — see `MEDIA-LAYERS.md`.

## Cache

`ASSET_V` on image URLs. Script tags `?v=`. Increment both when replacing art.

## What the first playable minute must do

1. Show the start plate (not a blank color).
2. Offer a nested choice or a check, not only CONTINUE.
3. Let the book icon open the sheet.
