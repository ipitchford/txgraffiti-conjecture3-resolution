# Publisher core-container replay — 8 August 2026

This is a publisher-side replay record for the exact package files. It is not
an independent reproduction or peer review.

```text
command: docker build -f environment/Containerfile --target core -t txgraffiti-c3:4.0.0-rc1 .
base: debian:13.3-slim@sha256:1d3c811171a08a5adaa4a163fbafd96b61b87aa871bbc7aa15431ac275d3d430
runtime: OrbStack Docker 29.4.0, linux/arm64
image: sha256:86e20990556aaf0a2bc25b8aec3b8c09282cea2d5f67502336eb45b76558edc5
result: PASS — ./run_core_verification.sh
```

The replay passed encoding consistency, formula properties, graph checks,
proof-tree verification, byte-identical certificate regeneration, four
targeted mutation rejections, release metadata checks and the 60-file
manifest. The optional MILP layer was not run: its supplied lock file pins
Linux x86-64 wheels, while this host/container is arm64.
