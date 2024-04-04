SHELL := /bin/bash
PY_CMD := poetry run python
FLASK :=  -m flask --app main.py run --port 5001
PYTEST_CMD := ${PY_CMD} -m pytest
TEST_DIR := test/
Y = echo 'k'

.PHONY: run
run:
	${PY_CMD} ${FLASK} & open http://localhost:5001

.PHONY: test
test:
	${Y}

