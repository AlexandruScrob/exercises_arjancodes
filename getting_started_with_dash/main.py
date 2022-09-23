from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
import i18n

from src.data.source import DataSource
from src.data.loader import load_transaction_data
from src.components.layout import create_layout


DATA_PATH = "./data/transactions.csv"
LOCALE = "en"

# getting_started_with_dash/data
def main() -> None:
    i18n.set("locale", LOCALE)
    i18n.load_path.append("locale")
    data = load_transaction_data(DATA_PATH, LOCALE)
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = i18n.t("general.app_title")
    app.layout = create_layout(app, DataSource(data))
    app.run()


if __name__ == "__main__":
    main()
