#!/usr/bin/env bash
set -euo pipefail

echo "Registering marketplace-merge driver globally..."
git config --global merge.marketplace-merge.driver ".githooks/merge-marketplace.py %O %A %B"

echo "Enabling .githooks/ for this repo..."
git config core.hooksPath .githooks

echo "Hiding local marketplace.json changes from git..."
git update-index --skip-worktree .claude-plugin/marketplace.json

echo "Done. Regenerate marketplace.json for local testing with:"
echo "  python3 scripts/generate-marketplace.py"
