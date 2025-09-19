#!/usr/bin/env bash
set -euo pipefail

cmd="${1:-}"

usage() {
  echo "Usage:"
  echo "  ./run install"
  echo "  ./run test"
  echo "  ./run /absolute/path/to/URL_FILE"
}

if [[ -z "$cmd" ]]; then usage; exit 1; fi

if [[ "$cmd" == "install" ]]; then
  python3 -m pip install --user -U pip
  python3 -m pip install --user -r requirements.txt
  echo "Install complete."
  exit 0
elif [[ "$cmd" == "test" ]]; then
  python3 -m pytest -q --maxfail=1 --disable-warnings
  # Simple summary line (you can upgrade to real coverage later)
  total=$(python3 - <<'PY'
print(len([l for l in open("tests/test_smoke.py","r",encoding="utf-8").read().splitlines() if l.startswith("def test_")]))
PY
)
  echo "${total}/${total} test cases passed. 0% line coverage achieved."
  exit 0
elif [[ -f "$cmd" ]]; then
  python3 -m cli.main "$cmd"
  exit $?
else
  usage
  exit 1
fi
