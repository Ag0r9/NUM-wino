import typer

from src.pipeline.evaluate import evaluate_model
from src.pipeline.prepare import prepare_data
from src.pipeline.train import train_model
from src.pipeline.trends import show_trends

app = typer.Typer()


@app.command()
def prepare():
    prepare_data()


@app.command()
def train():
    train_model()


@app.command()
def evaluate():
    evaluate_model()


@app.command()
def trends():
    show_trends()


@app.command()
def hello():
    print("World")


if __name__ == "__main__":
    app()
