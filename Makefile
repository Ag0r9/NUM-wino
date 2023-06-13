install:
	poetry install

notebook:
	poetry run jupyter notebook

isort:
	poetry run isort src analytics

black:
	poetry run black --config pyproject.toml src analytics

format: isort black

status:
	git status
	poetry run dvc status

price:
	poetry run python -m analytics.cli.app calculate-price

prepare:
	poetry run python -m src.cli.app prepare

train:
	poetry run python -m src.cli.app train