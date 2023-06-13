install:
	poetry install

notebook:
	poetry run jupyter notebook

isort:
	poetry run isort src

black:
	poetry run black -- config pyproject.toml src

format: isort black

