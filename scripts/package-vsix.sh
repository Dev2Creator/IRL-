#!/usr/bin/env bash
# Package the IRL™ VS Code extension into a .vsix.
# Requires Node.js; vsce is fetched on the fly (no repo pollution).
set -euo pipefail
cd "$(dirname "$0")/../irl-vscode"

if ! command -v npx >/dev/null 2>&1; then
    echo "npx not found. Install Node.js first: https://nodejs.org" >&2
    exit 1
fi

npx --yes @vscode/vsce package --no-dependencies
echo ""
echo "Done. Upload with: npx @vscode/vsce publish"
echo "(Publishing needs a Personal Access Token: https://dev.azure.com → User settings → PAT)"
