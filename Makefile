install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

build:
	poetry build

.PHONY: install gendiff lint build

