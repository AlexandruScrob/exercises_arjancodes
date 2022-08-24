from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import pandas as pd

from src.data.loader import DataSchema

from . import ids


def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_years = data[DataSchema.YEAR].tolist()
    unique_years = sorted(set(all_years), key=int)

    @app.callback(Output(ids.YEAR_DROPDOWN, "value"), Input(ids.SELECT_ALL_YEARS_BUTTON, "n_clicks"))
    def select_all_years(_: int) -> list[str]:
        return unique_years

    return html.Div(
        children=[
            html.H6("Year"),
            dcc.Dropdown(
                id=ids.YEAR_DROPDOWN,
                options=[{"label": year, "value": year} for year in unique_years],
                value=unique_years,
                multi=True,
            ),
            html.Button(className="dropdown-button", children=["Select ALL"], id=ids.SELECT_ALL_YEARS_BUTTON),
        ]
    )
