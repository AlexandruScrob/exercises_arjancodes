from pathlib import Path
from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from src.data.loader import load_transaction_data
from src.components.layout import create_layout


BASE_PATH = Path(__file__).parent
DATA_PATH = "data/transactions.csv"


def main() -> None:
    data = load_transaction_data(f"{BASE_PATH}/{DATA_PATH}")
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = "Financial dashboard"
    app.layout = create_layout(app, data)
    app.run()


if __name__ == "__main__":
    main()
