#!/usr/bin/env bash
# Scaffold a campaign folder from this skill's template.
# Usage: scaffold.sh <slug> [parent_dir]
set -euo pipefail
SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SLUG="${1:?slug required (lowercase-hyphen)}"
PARENT="${2:-.}"
PARENT="${PARENT/#\~/$HOME}"
DEST="$PARENT/$SLUG"

if [[ -e "$DEST" ]]; then
  echo "ERROR: $DEST already exists" >&2
  exit 1
fi

mkdir -p "$DEST"
rsync -a "$SKILL_ROOT/templates/campaign/" "$DEST/"
# chroma helpers into the campaign
mkdir -p "$DEST/scripts"
cp "$SKILL_ROOT/scripts/chroma_key.py" "$DEST/scripts/"
cp "$SKILL_ROOT/scripts/clean_chroma.py" "$DEST/scripts/"

# stamp slug
if command -v sed >/dev/null; then
  find "$DEST" -type f \( -name '*.json' -o -name '*.md' -o -name '*.html' -o -name '*.js' \) \
    -exec sed -i.bak "s/{{SLUG}}/$SLUG/g" {} +
  find "$DEST" -name '*.bak' -delete
fi

chmod +x "$DEST/scripts/"*.py 2>/dev/null || true

echo "Scaffolded $DEST"
echo "Next: write docs/LOCK.md, then /rpg-campaign-maker lock"
echo "Preview:  cd $DEST && python3 -m http.server 8767 --bind 127.0.0.1"
