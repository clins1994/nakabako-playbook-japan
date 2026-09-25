#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Install this checkout's complete skill into the caller's current project.
set -euo pipefail
ROOT="$(CDPATH= cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
export DISABLE_TELEMETRY=1
export DO_NOT_TRACK=1
export npm_config_audit=false
export npm_config_fund=false
if ! command -v npx >/dev/null 2>&1; then
  printf '%s\n' 'Node.js/npm (including npx) is required. Install it, then rerun this script.' >&2
  exit 1
fi
# Do not change cwd: the CLI installs into the user's chosen current project.
# No --yes/--global: let the user review agent and installation choices.
exec npx --yes skills@1.7.0 add "$ROOT" --skill health-checkup --copy "$@"
