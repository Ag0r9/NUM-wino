import typer

from src.prepare import prepare_data

app = typer.Typer()


@app.command()
def prepare():
    prepare_data()


@app.command()
def hello():
    print("World")


if __name__ == "__main__":
    app()
