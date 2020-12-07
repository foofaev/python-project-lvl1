install:
	poetry install

build:
	 poetry build

lint:
	poetry run flake8 brain_games

publish:
	poetry publish --dry-run

package-install:
	pip install --user dist/*.whl

setup: install build package-install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even
