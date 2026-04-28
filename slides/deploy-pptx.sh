#!/usr/bin/env bash
# Build all workshop slide decks to PPTX (and optionally PDF/HTML) using Marp CLI.
#
# Usage:
#   ./deploy-pptx.sh              # PPTX only
#   ./deploy-pptx.sh --all        # PPTX + PDF + HTML
#   ./deploy-pptx.sh --pdf        # PPTX + PDF
#   ./deploy-pptx.sh --html       # PPTX + HTML
#   ./deploy-pptx.sh --clean      # remove dist/ before building
#
# Requirements:
#   - Node.js (for npx) OR a global install of @marp-team/marp-cli
#   - Chromium/Chrome available to Marp for PPTX/PDF export
#     (Marp will try to download one automatically on first run)

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SLIDES_DIR="$SCRIPT_DIR"
DIST_DIR="$SCRIPT_DIR/dist"

BUILD_PDF=false
BUILD_HTML=false
CLEAN=false

for arg in "$@"; do
  case "$arg" in
    --all)   BUILD_PDF=true; BUILD_HTML=true ;;
    --pdf)   BUILD_PDF=true ;;
    --html)  BUILD_HTML=true ;;
    --clean) CLEAN=true ;;
    -h|--help)
      sed -n '2,16p' "$0"; exit 0 ;;
    *)
      echo "Unknown argument: $arg" >&2
      echo "Run '$0 --help' for usage." >&2
      exit 1 ;;
  esac
done

# Resolve a Marp CLI runner: prefer global 'marp', fall back to 'npx'.
if command -v marp >/dev/null 2>&1; then
  MARP=(marp)
elif command -v npx >/dev/null 2>&1; then
  MARP=(npx --yes @marp-team/marp-cli@latest)
else
  echo "Error: neither 'marp' nor 'npx' found in PATH." >&2
  echo "Install Node.js or run: npm i -g @marp-team/marp-cli" >&2
  exit 1
fi

if $CLEAN; then
  echo "Cleaning $DIST_DIR ..."
  rm -rf "$DIST_DIR"
fi

mkdir -p "$DIST_DIR/pptx"
$BUILD_PDF  && mkdir -p "$DIST_DIR/pdf"
$BUILD_HTML && mkdir -p "$DIST_DIR/html"

shopt -s nullglob
DECKS=("$SLIDES_DIR"/part-*.md)
if [ ${#DECKS[@]} -eq 0 ]; then
  echo "No part-*.md decks found in $SLIDES_DIR" >&2
  exit 1
fi

echo "Found ${#DECKS[@]} deck(s). Building ..."

for deck in "${DECKS[@]}"; do
  base="$(basename "${deck%.md}")"
  echo
  echo "==> $base"

  echo "    -> PPTX"
  "${MARP[@]}" --allow-local-files --pptx \
    -o "$DIST_DIR/pptx/${base}.pptx" "$deck"

  if $BUILD_PDF; then
    echo "    -> PDF"
    "${MARP[@]}" --allow-local-files --pdf \
      -o "$DIST_DIR/pdf/${base}.pdf" "$deck"
  fi

  if $BUILD_HTML; then
    echo "    -> HTML"
    "${MARP[@]}" --allow-local-files --html \
      -o "$DIST_DIR/html/${base}.html" "$deck"
  fi
done

echo
echo "Done. Output:"
echo "  PPTX:  $DIST_DIR/pptx/"
$BUILD_PDF  && echo "  PDF:   $DIST_DIR/pdf/"
$BUILD_HTML && echo "  HTML:  $DIST_DIR/html/"
