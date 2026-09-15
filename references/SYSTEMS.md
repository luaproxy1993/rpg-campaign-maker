# Systems

Fun in a short campaign is a **tree** the player can miss, plus a **check** that can fail.

## Nested tree

A one-layer list of choices that all go to the same next scene is a slideshow.

Keep source nesting:

```
life
  ├ working → driving | wilderness | hustle | crime
  ├ social  → …
  ├ military → MOS picks
  └ educated → …
clan
  ├ Ventrue → path art + discipline
  └ …
```

Each leaf writes **different** flags/stats/items. Later nodes `visible:` on those flags.

Store as `play/story.js` nodes `{ id, bg, speaker, text, choices[], continue }` or `content/tree.json`. Either is fine; the player must be able to take a branch another player never sees.

## Sheet

Start from the book's printed stats. Typical VTM-like sitting:

- Attributes start at 1 (or the book's default)
- Skills mostly 0, one or two at 1
- Resource clock (Hunger, HP, time-to-dawn)

`play/sheet.js` renders the sheet. A book icon toggles it. Do not hide the sheet behind chat.

## Checks

One formula, shown when it fires:

```
pool = attr + skill
vs hard (4) or mixed (2)
success | mixed | fail
```

Fail must change the next node or a resource — not only flavor text.

## Items

Choices `give` named items. Sheet lists them. Later choices `require` them. Names stay as printed ("rusty Leatherman", not "多功能刀").

## What not to add

- A second combat engine "for completeness"
- Thirteen clans if the sitting uses four
- Romance tracks that start after the cut
- A companion who only exists in a flashback
