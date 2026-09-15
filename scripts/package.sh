#!/usr/bin/env bash
# Build a shareable tarball for npx skills add / install.sh
set -euo pipefail
SKILL_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$SKILL_ROOT/VERSION")"
NAME="rpg-campaign-maker-v${VERSION}"
OUT_DIR="${1:-$SKILL_ROOT/dist}"
STAGING="$OUT_DIR/.staging-$NAME"
ARCHIVE="$OUT_DIR/${NAME}.tar.gz"

rm -rf "$STAGING"
mkdir -p "$OUT_DIR" "$STAGING/$NAME"
rsync -a --exclude dist --exclude '.staging-*' --exclude .DS_Store --exclude .git \
  "$SKILL_ROOT/" "$STAGING/$NAME/"
chmod +x "$STAGING/$NAME/install.sh" "$STAGING/$NAME/scripts/"*.sh 2>/dev/null || true
tar -czf "$ARCHIVE" -C "$STAGING" "$NAME"
rm -rf "$STAGING"
echo "Package: $ARCHIVE"
echo "Install: tar -xzf $NAME.tar.gz && cd $NAME && ./install.sh"
echo "Or:      npx skills add $SKILL_ROOT -y"
