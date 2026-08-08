# Execution environment

## Assurance status

The exact release contains a **declarative, version-pinned container definition** and a hash-locked optional Python dependency file. The theorem-critical core replay was executed successfully in the recorded local environment and again from a clean extracted copy. Docker or Podman was not available in the authoring environment, so the container definition itself was not built here. The environment status is therefore **definition pinned; container replay pending**.

## Recorded successful environment

- Operating system: Debian GNU/Linux 13.3 (`trixie`)
- Python: 3.13.5
- C++ compiler: GNU C++ 14.2.0
- NumPy: 2.3.5, optional
- SciPy: 1.17.0, optional
- gzip: 1.13
- locale: `C.UTF-8`
- timezone: `UTC`
- `PYTHONHASHSEED=0`
- `SOURCE_DATE_EPOCH=1785974400`

The C++ programs use:

```text
-std=c++20 -O3 -Wall -Wextra -Wconversion -Wshadow -pedantic
```

All finite searches are deterministic. No random seed enters the theorem-critical replay. The optional mixed-integer programmes use SciPy's `milp` interface and report the solver status and optimality gap.

## Pinned container definition

`environment/Containerfile` fixes the Debian 13.3 slim base by the multi-platform image digest

```text
sha256:1d3c811171a08a5adaa4a163fbafd96b61b87aa871bbc7aa15431ac275d3d430
```

and requests exact Debian package versions. `environment/requirements-milp.lock` fixes the Linux x86-64 CPython 3.13 NumPy and SciPy wheels by URL and SHA-256.

The base-image digest fixes the image bytes. Exact Debian package retrieval remains dependent on Debian's repositories retaining those versions; this is a residual reproducibility limitation rather than a hidden guarantee. The core proof does not require NumPy, SciPy or any network access once the compiler and Python interpreter exist.

## Commands

Core proof only:

```sh
./run_core_verification.sh
```

Optional corroborative optimisation:

```sh
./run_optional_audits.sh
```

Combined entry point; the optional audit is opt-in:

```sh
RUN_OPTIONAL_AUDITS=1 ./run_verification.sh
```

Container core build:

```sh
docker build -f environment/Containerfile --target core -t txgraffiti-c3:4.0.0-rc1 .
```

Container with optional MILP audit:

```sh
docker build -f environment/Containerfile --target optional-audit -t txgraffiti-c3:4.0.0-rc1-milp .
```
