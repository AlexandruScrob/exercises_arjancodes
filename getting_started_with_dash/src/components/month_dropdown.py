from dash import Dash, html, dcc
from dash.dependencies import Input, Output

import i18n

from ..data.source import DataSource

from . import ids


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        [Input(ids.YEAR_DROPDOWN, "value"), Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks")],
    )
    def select_all_months(years: list[str], _: int) -> list[str]:
        return source.filter(years=years).unique_months

    return html.Div(
        children=[
            html.H6(i18n.t("general.month")),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options=[{"label": month, "value": month} for month in source.unique_months],
                value=source.unique_months,
                multi=True,
            ),
            html.Button(
                className="dropdown-button",
                children=[i18n.t("general.select_all")],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                n_clicks=0,
            ),
        ]
    )
