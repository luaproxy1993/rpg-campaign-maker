---
name: rpg-campaign-maker
description: >-
  Turn a short RPG campaign slice — original or a dropped campaign book —
  into a playable one-sitting game. Covers campaign lock, nested choice trees,
  stats/checks/items, engine-ready art (chroma, per-scene FX), original-voice
  copy, CC audio, a playable shell, and in-sitting photo/voice/video as a
  clip-library on the tree. For product_form doki-mesh-world, C3 mounts a content
  pack on the existing DokiDemo GameShell (frame-by-frame parity with the shipped
  Strahd AVG) and C5 cannot accept a thinner paper shell. Use when the user runs
  /rpg-campaign-maker, says "make a campaign", "campaign book", "ChoiceScript",
  "adventure path", "one-shot RPG", "short campaign", "drag this module in", or
  wants a playable AVG/RPG from a PDF, .txt, Foundry, or World of Darkness book.
  Not for dating-sim calendars, grid crawls, companion OS (Candy-class chat+live
  video), or digital-human R1.
---

# RPG Campaign Maker

A **slice** is not a skeleton. Fun in a one-sitting RPG comes from nested **tree**, real **checks**, and **engine-ready** pictures — not from a linear smash-through with placeholder art.

This skill ships a playable sitting. **Product form decides the shell** (`docs/INTENT.md` `product_form`, or the accepted lock if it recorded one):

- `static-campaign-sitting` (default when no mesh/Doki world was chosen): a static game (`index.html` + `play/` + `assets/`). Optional later: wrap as a Dokiworld pack via `doki-game-maker`. Do not start there.
- `doki-mesh-world` (Barovia-quality narrative worlds, not Barovia content): C0–C2 still lock the sitting here; C3 **mounts a content pack on the existing DokiDemo GameShell**. Do not start by writing a new `index.html` / walk-look-talk page. See C3.
- Other forms stay on their own conductors (`screenshot-first-idle` → `game-maker-pipeline`; Godot 2D → `build-a-game`). This skill is not their shell.

## Product formula

```text
lock (cut + systems + 3-min accept)
  → ingest (write original  OR  eat the book)
  → tree + sheet (nested choices, dots, items, checks)
  → original-voice shell (UI that matches the source, not a generic VN)
  → engine-ready assets (keyed portraits, per-scene FX, CC audio)
  → playtest at the author-gate
  → static dist
```

Two intakes, same pipeline:

| Intake | User brings | Agent does first |
|--------|-------------|------------------|
| **Original** | Premise, tone, cut | Write the **lock**, invent nothing past the slice |
| **Book** | PDF / ChoiceScript / markdown / Foundry / photos of pages | **Ingest** into lock + tree; **original-voice** — no paraphrase into another language |

Load on demand:

- Book / PDF / ChoiceScript / module drop → `references/BOOK-INGEST.md`
- Stats, nested trees, items, checks → `references/SYSTEMS.md`
- Art, chroma, FX, audio → `references/ASSETS.md`
- Play shell, UI, copy → `references/SHELL.md`
- Companion / live video / “she sends” media / PixVerse / Candy → `references/MEDIA-LAYERS.md`
- What actually broke a real slice → `references/PITFALLS.md`
- Gate checklist → `references/CHECKLIST.md`

## Commands

```
/rpg-campaign-maker
/rpg-campaign-maker new <slug>
/rpg-campaign-maker lock | ingest | systems | shell | assets | playtest | ship
```

| Arg | Action |
|-----|--------|
| (none) | Read `pipeline_state.json` and continue; else ask intake |
| `new <slug>` | Scaffold, then **lock** |
| `lock` | C0 |
| `ingest` | C1 |
| `systems` | C2 |
| `shell` | C3 |
| `assets` | C4 |
| `playtest` | C5 |
| `ship` | C6 |

Session root = the campaign folder (`<slug>/`). Resolve: current workspace pack named by the user → `./<slug>` → ask.

---

## C0 · Lock

**Done when** `docs/LOCK.md` exists and the author can quote the cut, the systems, and the 3-minute accept sentence.

Write `docs/LOCK.md`:

1. **Slice** — where it starts, where it **stops**, what is explicitly out.
2. **Systems on the table** — which of talk / fight / check / inventory / clock actually fire in this sitting. Name them. A system that never fires is not in the slice.
3. **3-minute accept** — one sentence the player can feel that this is not a chat window.
4. **Voice** — language of the source. If the book is English, the game is English. Do not "helpfully" translate.
5. **IP** — unofficial remix / original / licensed. State it.
6. **Entry face** — whose portrait is the card; who is flashback-only.
7. **Media beats** — if the brief names chat companions, live video, PixVerse, Candy, or “she sends” photo/voice/video: load `references/MEDIA-LAYERS.md` first. In-slice beats are a **clip-library**. A **companion OS** is another product, not this `dist/`.

Then `pipeline_state.json`:

```json
{
  "skill": "rpg-campaign-maker",
  "skill_version": "1.1.0",
  "slug": "<slug>",
  "intake": "original | book",
  "step": "C0",
  "status": "in_progress"
}
```

Scaffold if the folder is empty:

```bash
{SKILL_ROOT}/scripts/scaffold.sh <slug> [parent_dir]
```

**STOP** — `step C0: accept`

Template: `references/LOCK.md`.

---

## C1 · Ingest

**Done when** every scene in the slice has a source citation, and no scene past the cut exists in the outline.

- **Original:** write `docs/BIBLE.md` from the lock. Do not pad with extra acts "for completeness". If a World Bible (`WORLD_BIBLE.md` / `/world-bible`) already exists, **cut the sitting from it**; do not rewrite the world.
- **Book:** load `references/BOOK-INGEST.md`. Extract nested **tree** (not a flattened list), stat names as printed, item names as printed. Dump raw excerpts into `source/` and keep them.

Mark flashback-only characters in the bible. They do not get a live companion slot.

**STOP** — `step C1: accept`

---

## C2 · Systems

**Done when** a player can fail a check, spend an item, and take a branch that another player never sees.

Load `references/SYSTEMS.md`. Minimum ship:

| Piece | File |
|-------|------|
| Nested node tree | `play/story.js` (or `content/tree.json` + loader) |
| Sheet | `play/sheet.js` + `mechanics/data/stats.json` |
| Checks | `mechanics/data/checks.json` + one visible formula in the UI |
| Items | granted by choices, listed on the sheet |

One-layer "A/B/C then next scene" is not a campaign. If the source has MOS / clan / class / background nested under life-path, keep that nesting.

**STOP** — `step C2: accept`

---

## C3 · Shell

Load `references/SHELL.md`. The done-when depends on `product_form`.

### `doki-mesh-world`

**Done when** the sitting is a content pack **mounted on the existing DokiDemo GameShell**, and a cold load on that shell is at **frame-by-frame parity** with the already-shipped Strahd AVG running on the same shell: full-bleed scene plates, dialogue two-shots, intro reel, BGM, HUD, in the locked play language (`docs/LOCK.md`; fall back to the source language if none is locked).

The default named shell is `/Users/a123/grokmaker/campaigns/DokiDemo` (or a git worktree of that repo, e.g. `DokiDemo-brew`). Use that shell, or a worktree of it — not a replacement page that looks thinner.

- Do **not** create a new `index.html` / walk-look-talk page, even if DokiDemo is not on the current machine. **Stop and get the shell. Do not substitute.** A box with no Doki engine is not a reason to write a paper shell. Opening the first scene over local HTTP is **not** done.
- Cache-bust `?v=` on every script and asset URL after visual changes.
- Copy is **original-voice** in the locked play language. Do not silently switch languages. Invented translation is a bug, not a draft.
- Julian-class error: a flashback NPC must not sit in the live speaker slot.

### Other product forms this skill still shells (`static-campaign-sitting`)

**Done when** `python3 -m http.server` from the campaign root opens a playable first scene in the **locked play language** (`docs/LOCK.md`; fall back to the source language if none is locked), with the layout the author pointed at (not a generic VN unless they asked for one).

- Root `index.html` is the entry.
- Cache-bust `?v=` on every script and asset URL after visual changes.
- Copy is **original-voice** in the locked play language. Do not silently switch languages. Invented translation is a bug, not a draft.
- Julian-class error: a flashback NPC must not sit in the live speaker slot.

**STOP** — `step C3: accept`

---

## C4 · Assets

**Done when** every portrait is a clean RGBA cutout on the game's actual background, every scene has **one** FX recipe that belongs to that picture, audio (if any) is credited CC, and every media beat (if any) is a clip-library file on a node.

Load `references/ASSETS.md`. Photo, voice, or video beats: also `references/MEDIA-LAYERS.md` — they are a **clip-library** on the tree, generated at author time.

Iron rules, from a real slice:

1. Generated art is not engine-ready until keyed.
2. Magenta screen + flood-from-transparent + largest-component. Protect purple cloth and blood.
3. One FX family per scene. Indoor motes live in light shafts. Sand stays on desert ground. Stars stay in sky rects.
4. UI clicks are recorded samples (CC0), not oscillators.
5. Ambience is CC-credited or silent.

**STOP** — `step C4: accept`

---

## C5 · Playtest

**Done when** the 3-minute accept sentence is true on a cold load, the author has walked the deepest nested branch once, **and** (for `doki-mesh-world`) the running pack passes the **reference-shell parity** gate below. A sitting that only opens a first scene over local HTTP, or that plays in a thinner / paper walk-look-talk shell, is not a C5 accept.

Load `references/CHECKLIST.md`. Hit:

- Nested branch exists and is reachable
- A failed check changes the next node
- Cut is respected (no Lettow-class character appears)
- No pink fringe on portraits over the real background
- Hard-refresh after asset changes (`?v=` bumped)
- Media beats (if any) play from `assets/media/`; `play/` calls no generator

For `doki-mesh-world` also hit:

- The pack is mounted on the named DokiDemo GameShell (see C3). Compare the running pack to the already-shipped Strahd AVG on that same shell: full-bleed scene plates, dialogue two-shots, intro reel, BGM, HUD. Paths, loading, or assets without this visual parity is not a pass — including an internal preview.
- Placeholder VO (`edge-tts` and the like) may be accepted on this playtest for an **internal preview** only. It cannot be a public `ship: accept`. `/world-ship-qa` must keep that distinction.

**STOP** — `step C5: accept`

---

## C6 · Ship

**Done when** `dist/` is a static tree: `index.html`, `play/`, `assets/`, `mechanics/`, no keys, no `node_modules`, no `_raw` / `_pre_clean`.

```bash
rsync -a --delete \
  --exclude node_modules --exclude .git --exclude _raw --exclude _pre_clean \
  --exclude .venv --exclude '*.pyc' \
  play/ assets/mechanics content index.html dist/   # adjust to the scaffold
```

Prefer a pack `scripts/build.mjs` if present. Write `assets/audio/CREDITS.md` if audio shipped.

**STOP** — `step C6: accept`

---

## Quality bar

1. The **lock** is shorter than the game.
2. A second playthrough can miss a scene the first playthrough saw.
3. Portraits are cutouts, not cards-on-pink.
4. Copy matches the source language.
5. FX is per-scene, not a global dust preset.
6. No API keys in `dist/`.
7. Photo/voice/video beats are clip-library files on nodes, not play-time gen.

## Hard guardrails

State the target, not the ban:

- Write the **lock** before generating a single image.
- Keep the source language.
- Keep nested **tree**.
- Key portraits until they hold over the real scene.
- Assign one FX recipe per scene file.
- Credit CC audio or ship silent.
- Ship in-sitting photo/voice/video as a **clip-library** on the tree.

Battle log: `references/PITFALLS.md`.

---

## Session bootstrap

```
SKILL_ROOT = this skill directory
CAMPAIGN   = the slug folder

load:
  - SKILL.md (this file)
  - CAMPAIGN/pipeline_state.json, docs/LOCK.md   (if they exist)
  - ~/.grok/skills/world-bible/SKILL.md          when a WORLD_BIBLE.md exists or the brief is a world, not a sitting
  - references/BOOK-INGEST.md   when intake is book
  - references/SYSTEMS.md       at C2
  - references/SHELL.md         at C3
  - references/ASSETS.md        at C4
  - references/MEDIA-LAYERS.md  when the brief has companion / live video / PixVerse / Candy / “she sends” media
  - references/CHECKLIST.md     at C5
  - references/PITFALLS.md      when something looks "good enough" and is not
```

`todo_write` tracks C0–C6. Checkpoint → `pipeline_state.json`.
