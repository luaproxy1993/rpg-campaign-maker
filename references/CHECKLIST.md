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

- [ ] `python3 -m http.server` from campaign root plays the first scene
- [ ] `dist/` has no keys, no `node_modules`, no `_raw`
