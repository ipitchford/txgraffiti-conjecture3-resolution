.PHONY: core optional verify pdfs manifest archive clean

core:
	./run_core_verification.sh

optional:
	./run_optional_audits.sh

verify:
	RUN_OPTIONAL_AUDITS=1 ./run_verification.sh

pdfs:
	./build_pdfs.sh

manifest:
	python3 make_manifest.py
	python3 check_manifest.py

archive: manifest
	python3 make_release_zip.py

clean:
	rm -f .verify_counterexample.tmp .generate_ids15_certificate.tmp
	rm -rf __pycache__ .pytest_cache _renders
