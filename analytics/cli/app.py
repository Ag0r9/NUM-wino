import typer

from analytics.utils import calculate_wine_price

app = typer.Typer()


@app.command()
def calculate_price():
    calculate_wine_price()


@app.command()
def hello():
    print("World")


if __name__ == "__main__":
    app()
