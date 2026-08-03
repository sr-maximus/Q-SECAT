.PHONY: install test validate coverage export sync-data check all

install:
	python -m pip install -e .[dev]

test:
	pytest

validate:
	qsecat validate examples/assessment-example.yaml

coverage:
	qsecat coverage

export:
	python scripts/export_catalog.py

sync-data:
	python scripts/sync_package_data.py

check:
	python scripts/check_traceability.py

all: sync-data check validate coverage test export
