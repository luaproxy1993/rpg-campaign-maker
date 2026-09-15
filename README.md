# RPG Campaign Maker

A coding-agent skill that turns a **short campaign slice** (original, or a dropped campaign book) into a playable one-sitting RPG.

Install once. Then in Claude Code, Cursor, Codex, Antigravity, Grok, or any agent that reads `SKILL.md`:

```text
/rpg-campaign-maker
```

Drop a ChoiceScript file, a WoD sitting, a PDF module, or a one-paragraph premise. The skill locks the **cut**, keeps nested **trees**, keys portraits, and ships a static `index.html`.

## Install

```bash
# From this folder (works before GitHub)
npx skills add /absolute/path/to/rpg-campaign-maker -y

# Target specific agents
npx skills add /absolute/path/to/rpg-campaign-maker --agent claude-code --agent cursor -y

# After you push to GitHub
npx skills add <you>/rpg-campaign-maker -y
```

Manual:

```bash
./install.sh                  # ~/.grok/skills/rpg-campaign-maker
./install.sh --all-agents     # also Claude / Cursor / Codex / .agents
./install.sh --dir ~/.claude/skills/rpg-campaign-maker
```

## What it is not

Not a dating-calendar mutator. Not a grid crawl. Not a **companion OS** (Candy-class chat + live video). Not a digital-human R1 pipeline. Those stay in `doki-game-maker` / `pixverse-r1`. This skill is the **campaign sitting**: lock → tree → engine-ready art → playable shell.

Photo / voice / video that *do* belong in a sitting are a **clip-library** on the tree (`references/MEDIA-LAYERS.md`) — author-time files, not play-time gen.

## Why it exists

A "small AVG excerpt" still needs: nested choice depth, a sheet that fires, original-language copy, keyed cutouts, and one FX family per scene. Skipping any of those produces a slideshow. The skill makes the agent refuse the slideshow.

## License

Skill text and scripts: use and modify. Do not ship other people's campaign books or OSTs unless you have the rights. CC audio must be credited in `assets/audio/CREDITS.md`.
