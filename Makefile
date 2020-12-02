install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

build:
	poetry build

package-install:
	python3.8 -m pip install --user dist/*.whl

.PHONY: install gendiff lint build package-install

