# Media layers — companion OS vs sitting

A live-feeling product is not one model. It is **stacked lines** glued by an economy. This sitting ships at most one of those lines: a **clip-library** hung on the tree. Everything else is already this skill (authored copy, keyed stills) or a different product.

Load when the brief names any of: AI girlfriend, Candy, chat companion, “she sends” photos/voice/video, live video, Roulette, Play With Me, PixVerse, R1, realtime digital human, NSFW video.

## Companion OS vs this sitting

| Product | What it is | Home |
|---------|------------|------|
| **Campaign sitting** | Nested tree, checks, items, keyed plates, original-voice shell | this skill → static `dist/` |
| **Companion OS** (Candy-class) | Uncensored chat + memory + image factory + TTS + clip-library + optional live head, glued by tokens | chat host + `doki-game-maker` + `pixverse-r1` |

**Candy-class** failure: a chat window that generates pics/video, labeled a campaign. The 3-minute accept already forbids it. If the author also wants a companion OS, the sitting stays the tree; the companion is a later wrap, not a node type.

## UX is not the pipeline

| Player feels | Actual line | In this sitting |
|--------------|-------------|-----------------|
| She talks, stays in character | LLM + persona card, re-fed every turn | Out. Tree copy is authored. |
| She remembers last week | Facts table + vector recall + rolling summaries | Out. Flags and items on the sheet. |
| Selfie / outfit / “show this scene” | Character-locked stills (seed + LoRA/IP-Adapter), cheap vs premium engines | Keyed portrait or scene plate. Generate at **author time**. |
| Voice note / call | TTS / STT, billed per clip or per minute | Optional CC (or licensed) audio file on a node. |
| She *randomly* sends a pic | Scheduler (“Realistic mode”), not model emergence | A clock or a node. Write it in the tree. |
| Action menu / Play With Me | Finite **clip-library**, some free, some gated | **The sitting pattern.** A node `give`s a clip the way it `give`s an item. |
| 10–120s “make that happen” | Async I2V/T2V queue, seconds to a minute | Author-time render → then clip-library. Not play-time. |
| Live video chat (Roulette / Cam) | Looping talking-head ± clip swap; user camera is chrome; Cam public chat is often fake | Live head → `pixverse-r1`. Fake-live → looping clip on a node. |
| Shorts / episodes | Pre-produced linear content | Scene plates + CONTINUE. |

Do not put a generator behind `play/`. Play-time gen is a companion OS.

## Clip-library

Photo, voice, and video beats in a sitting are assets on the tree, same class as items.

- One file per beat, named by place/action (`filling_station_knock.mp4`), not `clip3`.
- Directory: `assets/media/`.
- Node field: `media: { type: "photo"|"voice"|"video", src, credit? }`.
- Gate with the same `require` / resource / choice used for items.
- Engine-ready before C5: file exists, poster or duration known, URL has `?v=`, no secret in the path.
- Switching clips is a **node transition**. It is not a prompt.

Candy’s Play With Me is this. The menu is a library. Marketing calls it live.

## PixVerse / R1

Do not re-implement. Runtime facts live in `pixverse-r1` and `doki-game-maker`.

- **R1** is reservation + Agora stream + DataStream prompts. It maps to a Roulette-like live head, not to a porn clip factory.
- Seed first (locked-portrait, Ambient). Close the session.
- Explicit sexual video through PixVerse fails policy (input+output audit, `audit_result`, account risk). Do not send it. If the author still wants hardcore clips, that is a **self-hosted I2V line at author time**, then clip-library — never the PixVerse key, never play-time.
- C6 already bans keys in `dist/`. `PIXVERSE_API_KEY` is the same ban.

Live digital human **and** a sitting = two products. Sitting ships static. A doki pack may later embed that SPA. Do not start the sitting as an R1 session.

## Lock

When the brief has media beats, `docs/LOCK.md` names:

1. Which beats are **clip-library** (in slice).
2. Which lines are **out** (chat LLM, live R1, play-time I2V).
3. Whether a companion OS is a later wrap — not this `dist/`.

No media section means stills + copy only. That is the default sitting.
