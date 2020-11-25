insall:
	poetry install

build:
	 poetry build

lint:
	poetry run flake8 brain_games

package-install:
	pip install --user dist/*.whl

brain-games:
	poetry run brain-games
