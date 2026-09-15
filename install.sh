#!/usr/bin/env bash
# Install rpg-campaign-maker into a coding-agent skills directory.
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
FORCE=0
ALL=0
DEST=""

usage() {
  cat <<'EOF'
Usage: install.sh [OPTIONS]

Options:
  --dir PATH      Install destination
  --all-agents    Also copy to ~/.claude/skills, ~/.cursor/skills,
                  ~/.codex/skills, ~/.agents/skills
  --force         Overwrite
  -h, --help

Default: ~/.grok/skills/rpg-campaign-maker

  npx skills add <this-folder> -y
EOF
}

while [ $# -gt 0 ]; do
  case "$1" in
    --dir) DEST="${2:?}"; shift 2 ;;
    --all-agents) ALL=1; shift ;;
    --force) FORCE=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
  esac
done

install_one() {
  local target="$1"
  case "$target" in
    "~/"*) target="$HOME/${target#~/}" ;;
  esac
  mkdir -p "$(dirname "$target")"
  if [ -e "$target" ] && [ "$FORCE" -ne 1 ]; then
    echo "skip existing $target  use --force to overwrite"
    return 0
  fi
  rm -rf "$target"
  mkdir -p "$target"
  rsync -a --exclude dist --exclude .git --exclude .DS_Store "$SCRIPT_DIR/" "$target/"
  chmod +x "$target/install.sh" "$target/scripts/"*.sh 2>/dev/null || true
  echo "installed -> $target"
}

if [ -n "$DEST" ]; then
  install_one "$DEST"
else
  install_one "$HOME/.grok/skills/rpg-campaign-maker"
fi

if [ "$ALL" -eq 1 ]; then
  install_one "$HOME/.claude/skills/rpg-campaign-maker"
  install_one "$HOME/.cursor/skills/rpg-campaign-maker"
  install_one "$HOME/.codex/skills/rpg-campaign-maker"
  install_one "$HOME/.agents/skills/rpg-campaign-maker"
fi

VERSION="$(cat "$SCRIPT_DIR/VERSION" 2>/dev/null || echo unknown)"
echo ""
echo "rpg-campaign-maker v${VERSION}"
echo "In the agent: /rpg-campaign-maker"
echo "npx skills add $SCRIPT_DIR -y"
