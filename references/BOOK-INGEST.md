# Book ingest

Use when the user drops a campaign book, ChoiceScript, PDF, markdown dump, Foundry module, or screenshots of pages.

## Goal

A **tree** and a **sheet** that a player of the book would recognize — not a summary in another language.

## Detect the source

| Clue | Treat as |
|------|----------|
| `*choice` / `*stat_chart` / `*if` | ChoiceScript (Choice of Games, Hosted Games) |
| "You are in a…" numbered rooms | Paragraph-choice / CYOA |
| Stats block + scenes + NPCs, WoD/PbtA/FitD jargon | Tabletop adventure |
| Foundry `src/` + packs | VTT export — extract journals + actors |
| PDF of an AP / module | Adventure path — ingest **one sitting**, not the book |

If unsure, ask which **sitting** to ship. Do not ingest a 400-page AP into one game.

## ChoiceScript

1. Copy the relevant `scenes/*.txt` into `source/`.
2. Walk `*choice` / `*fake_choice` / `*if` / `*goto` / `*label`. Nested `*choice` stays nested.
3. Preserve printed labels. Do not rewrite "I served in the military…" into a shorter Chinese/English paraphrase.
4. Map `*set` and `*stat_chart` into `mechanics/data/stats.json`.
5. Items from `*set` flags or inventory commands become `give` on choices.
6. Cut: stop at the **lock** label. Delete later `*goto` targets from the playable tree.

## Tabletop adventure (WoD, Pathfinder, 5e, PbtA…)

1. One sitting = one site + one clock + one fight-or-talk fork.
2. Convert boxed text to **original-voice** narration (same language as the book).
3. Convert "DC 15 Dexterity (Stealth)" into this game's check formula (see SYSTEMS.md). Do not invent a second math.
4. Named NPCs get portraits only if they appear on screen. Flashback names stay in prose.

## PDF / photos of pages

OCR if needed. Quote, then structure. Never "improve" the author's sentence rhythm.

## Output of ingest

```
source/                 # raw excerpts, immutable
docs/BIBLE.md           # scenes, NPCs, clocks, cut
docs/TREE.md            # nested outline with source labels
mechanics/data/stats.json
```

**Done:** every playable node cites a source line or page. Nodes past the cut do not exist.
