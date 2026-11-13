#!/usr/bin/env bash
# ci_build.sh -- compile the .tex files changed since a base commit, in all
# four variants, the way build.ps1 does on Windows (build.ps1 itself is
# Windows-only: backslash paths and a ';'-separated TEXINPUTS).
#
#   tools/ci_build.sh <base-ref>
#
# A change under shared/ also compiles tools/smoke/, because the class files
# affect every document (CLAUDE.md: "If you change shared\, rebuild these
# first"). Fails on any compile error, or if a key comes out SHORTER than its
# student build -- the corpus invariant (CLAUDE.md, convention 2).
set -euo pipefail

base="${1:?usage: tools/ci_build.sh <base-ref>}"
root="$(git rev-parse --show-toplevel)"
cd "$root"
aux="$root/build/aux"
mkdir -p "$aux"

mapfile -t changed < <(git diff --name-only --diff-filter=d "$base" HEAD)
files=()
for f in "${changed[@]}"; do
  case "$f" in
    Units/*.tex|Chapters/*.tex|tools/smoke/*.tex) files+=("$f") ;;
  esac
done
if printf '%s\n' "${changed[@]}" | grep -q '^shared/'; then
  files+=(tools/smoke/*.tex)
fi
mapfile -t files < <(printf '%s\n' "${files[@]}" | grep . | sort -u || true)

if [ "${#files[@]}" -eq 0 ]; then
  echo "No .tex sources changed since $base -- nothing to compile."
  exit 0
fi
echo "Compiling ${#files[@]} file(s) x 4 variants:"
printf '  %s\n' "${files[@]}"

declare -A preamble=(
  [student-print]=''
  [student-lms]='\def\ISLMS{1}'
  [key-print]='\def\ISKEY{1}'
  [key-lms]='\def\ISKEY{1}\def\ISLMS{1}'
)
export TEXINPUTS=".:$root/shared//:"
failed=0

for src in "${files[@]}"; do
  dir="$(dirname "$src")"
  name="$(basename "$src")"
  stem="${name%.tex}"
  declare -A pages=()
  for variant in student-print student-lms key-print key-lms; do
    job="$stem-$variant"
    ok=1
    # Two passes: tcolorbox/needspace layout settles on the second.
    for pass in 1 2; do
      if ! (cd "$dir" && pdflatex -interaction=nonstopmode -halt-on-error \
              -jobname="$job" -output-directory="$aux" \
              "${preamble[$variant]}\\input{$name}" >/dev/null 2>&1); then
        echo "::error file=$src::$variant failed to compile (pass $pass)"
        grep -A4 '^!' "$aux/$job.log" | head -20 || true
        ok=0
        failed=1
        break
      fi
    done
    [ "$ok" -eq 1 ] || continue
    pages[$variant]="$(pdfinfo "$aux/$job.pdf" | awk '/^Pages:/ {print $2}')"
    boxes="$(grep -c 'Overfull\|Underfull' "$aux/$job.log" || true)"
    if [ "$boxes" -gt 0 ]; then
      echo "::warning file=$src::$variant has $boxes over/underfull box warning(s)"
    fi
  done
  for medium in print lms; do
    s="${pages[student-$medium]:-}"
    k="${pages[key-$medium]:-}"
    [ -n "$s" ] && [ -n "$k" ] || continue
    echo "  $stem [$medium] student $s pages, key $k pages"
    if [ "$k" -lt "$s" ]; then
      echo "::error file=$src::key-$medium ($k pages) is shorter than student-$medium ($s) -- the footprint invariant is broken"
      failed=1
    fi
  done
  unset pages
done

exit "$failed"
