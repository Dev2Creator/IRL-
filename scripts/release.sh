#!/usr/bin/env bash
# IRL™ release ritual: verify, build, tag. Pushing and publishing stay human decisions.
set -euo pipefail
cd "$(dirname "$0")/.."

VERSION="${1:-}"
if [[ -z "$VERSION" ]]; then
    echo "Usage: scripts/release.sh 2.0.0" >&2
    exit 1
fi

TAG="v$VERSION"

echo "==> Checking version in pyproject.toml matches $VERSION"
grep -q "^version = \"$VERSION\"" pyproject.toml || {
    echo "pyproject.toml version does not match $VERSION. Fix it first." >&2
    exit 1
}

echo "==> Running ruff"
python -m ruff check .

echo "==> Running tests"
python -m pytest

echo "==> Building sdist + wheel"
rm -rf dist
python -m build --no-isolation

echo "==> Verifying with twine"
python -m twine check dist/*

echo "==> Tagging $TAG (local only — pushing is a human decision)"
git tag -a "$TAG" -m "IRL $VERSION — The Glow-Up Update"

cat <<EOF

Done. To ship:
  1. git push origin main --tags          # needs credentials
  2. Set up PyPI trusted publishing on the repo (Settings → Environments → pypi)
  3. The 'Release' workflow publishes on the tag; or manually:
     python -m twine upload dist/*
EOF
