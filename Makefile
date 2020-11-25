install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

.PHONY: install gendiff lint

