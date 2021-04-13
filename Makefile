install:
	poetry install

gendiff:
	poetry run gendiff

lint:
	poetry run flake8 gendiff

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl

test:
	poetry run pytest --cov=gendiff --cov-report xml tests/

.PHONY: install gendiff lint build package-install

