import typer

from src.prepare import prepare_data
from src.train import train_data

app = typer.Typer()


@app.command()
def prepare():
    prepare_data()
    
    
@app.command()
def train():
    train_data()


@app.command()
def hello():
    print("World")


if __name__ == "__main__":
    app()
