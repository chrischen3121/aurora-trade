##
# artrade Makefile
#
# @description simplify repetitive build environment tasks

OS := $(shell uname -s)
PYTHON_VENV_DIR = $(shell poetry env info --path)

ifeq ($(OS),Windows_NT)
	PYTHON_BIN_DIR = $(PYTHON_VENV_DIR)/Scripts
else
	PYTHON_BIN_DIR = $(PYTHON_VENV_DIR)/bin
endif

init:
	poetry install

test:
	$(PYTHON_BIN_DIR)/pytest

coverage:
	$(PYTHON_BIN_DIR)/pytest --verbose --cov=artrade tests

clean:
	rm -rf .pytest_cache
	rm -rf .coverage
	rm -rf .mypy_cache
	rm -rf .tox
	rm -rf build
	rm -rf dist
	rm -rf artrade.egg-info
