# Author-gate checklist

Walk this at C5. Unchecked items fail the sitting.

## Slice

- [ ] Start plate is the locked start, not a menu
- [ ] Stop beat is honored; the named out-of-slice character never appears
- [ ] 3-minute accept sentence is true on a cold load

## Tree

- [ ] At least one nested branch another playthrough can miss
- [ ] A failed check changes node or resource
- [ ] An item is granted and later required or listed

## Voice

- [ ] Player-facing text is in the source language
- [ ] Choice labels keep source length and wording
- [ ] Flashback-only names are not live speakers

## Assets

- [ ] Portraits are RGBA cutouts; no magenta fringe on the real scene
- [ ] Each scene file has at most one FX family, and it belongs to that picture
- [ ] `?v=` bumped after the last art replace
- [ ] Audio, if present, has `assets/audio/CREDITS.md`
- [ ] Photo/voice/video beats (if any) are clip-library files on nodes; `play/` calls no generator; `dist/` has no API keys

## Ship

- [ ] For `static-campaign-sitting`: `python3 -m http.server` from campaign root plays the first scene
- [ ] For `doki-mesh-world`: the pack is mounted on the named DokiDemo GameShell and matches the shipped Strahd AVG on that shell (full-bleed plates, dialogue two-shots, intro reel, BGM, HUD). A thinner / paper walk-look-talk page, or “HTTP opened the first scene,” is not a pass — including an internal preview.
- [ ] Placeholder VO (`edge-tts` etc.) may ride an internal preview; it cannot be a public `ship: accept`
- [ ] `dist/` has no keys, no `node_modules`, no `_raw`
