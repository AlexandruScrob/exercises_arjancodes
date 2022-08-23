from dash import Dash, dcc, html
import plotly.express as px
from dash.dependencies import Input, Output

from . import ids

MEDAL_DATA = px.data.medals_long()


def render(app: Dash) -> html.Div:
    # called every time the input changes without having an explicit call
    @app.callback(Output(ids.BAR_CHART, "children"), Input(ids.NATION_DROPDOWN, "value"))
    def update_bar_chart(nations: list[str]) -> html.Div:
        filterted_data = MEDAL_DATA.query("nation in @nations")

        if filterted_data.shape[0] == 0:
            return html.Div("No data selected")
        fig = px.bar(filterted_data, x="medal", y="count", color="nation", text="nation")
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
