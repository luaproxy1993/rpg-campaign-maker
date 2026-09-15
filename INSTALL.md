# Install — rpg-campaign-maker v1.1.0

## The one command

```bash
npx skills add /path/to/rpg-campaign-maker -y
```

The `skills` CLI copies `SKILL.md` into whichever coding agents it detects (Claude Code, Cursor, Codex, OpenCode, …).

After you publish the folder as a GitHub repo:

```bash
npx skills add <owner>/rpg-campaign-maker -y
npx skills add <owner>/rpg-campaign-maker --agent claude-code --agent cursor -g -y
```

## Manual copy

```bash
./install.sh
./install.sh --all-agents --force
./install.sh --dir ~/.claude/skills/rpg-campaign-maker --force
```

| Agent | Typical path |
|-------|----------------|
| Grok | `~/.grok/skills/rpg-campaign-maker/` |
| Claude Code | `~/.claude/skills/rpg-campaign-maker/` |
| Cursor | `~/.cursor/skills/rpg-campaign-maker/` or project `.agents/skills/` |
| Codex | `~/.codex/skills/` (CLI also writes `.agents/skills/`) |
| Antigravity / others | `npx skills add … --agent <name>` |

## Verify

```bash
test -f ~/.grok/skills/rpg-campaign-maker/SKILL.md && echo grok-ok
npx skills list | grep rpg-campaign-maker
```

Then in the agent: `/rpg-campaign-maker` or “make a campaign from this book”.

## New campaign

```bash
~/.grok/skills/rpg-campaign-maker/scripts/scaffold.sh my-sitting ~/projects
cd ~/projects/my-sitting
python3 -m http.server 8767 --bind 127.0.0.1
```

Fill `docs/LOCK.md` before generating art.
