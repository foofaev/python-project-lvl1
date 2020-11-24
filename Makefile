insall:
	poetry install

build:
	 poetry build

package-install:
	pip install --user dist/*.whl

brain-games:
	poetry run brain-games
