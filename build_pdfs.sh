#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1785974400}"
APA_CSL="/usr/share/texlive/texmf-dist/tex/latex/citation-style-language/styles/apa.csl"
COMMON=(
  --from=markdown+tex_math_single_backslash
  --pdf-engine=xelatex
  --citeproc
  --bibliography=references.bib
  --csl="$APA_CSL"
  --resource-path=.
  -V papersize:a4
  -V geometry:margin=22mm
  -V fontsize=10pt
  -V linestretch=1.04
  -V colorlinks=true
  -V linkcolor=blue
  -V urlcolor=blue
  -V documentclass=article
)
pandoc MANUSCRIPT.md "${COMMON[@]}" -o MANUSCRIPT.pdf
pandoc EVIDENCE_SUPPLEMENT.md "${COMMON[@]}" -o EVIDENCE_SUPPLEMENT.pdf
