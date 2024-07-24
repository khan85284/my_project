# Makefile

install:
	poetry install

start:
	poetry run python -m my_project85.main

test:
	poetry run pytest

lint:
	poetry run flake8 my_project tests
