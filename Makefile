install:
	poetry install

notebook:
	poetry run jupyter notebook

isort:
	poetry run isort src analytics

black:
	poetry run black --config pyproject.toml src analytics

format: isort black

create_price:
	poetry run python -m analytics.cli.app calculate-price

status:
	git status
	poetry run dvc status

