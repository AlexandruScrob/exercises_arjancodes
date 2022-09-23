from dash import Dash, dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
import i18n

from ..data.source import DataSource

from src.data.loader import DataSchema

from . import ids

MEDAL_DATA = px.data.medals_long()


# def render(app: Dash) -> html.Div:
#     # called every time the input changes without having an explicit call
#     @app.callback(Output(ids.BAR_CHART, "children"), Input(ids.NATION_DROPDOWN, "value"))
#     def update_bar_chart(nations: list[str]) -> html.Div:
#         filterted_data = MEDAL_DATA.query("nation in @nations")

#         if filterted_data.shape[0] == 0:
#             return html.Div("No data selected")
#         fig = px.bar(filterted_data, x="medal", y="count", color="nation", text="nation")
#         return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

#     return html.Div(id=ids.BAR_CHART)


def render(app: Dash, source: DataSource) -> html.Div:
    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [Input(ids.YEAR_DROPDOWN, "value"), Input(ids.MONTH_DROPDOWN, "value"), Input(ids.CATEGORY_DROPDOWN, "value")],
    )
    def update_bar_chart(years: list[str], months: list[str], categories: list[str]) -> html.Div:
        filtered_source = source.filter(years=years, months=months, categories=categories)

        if not filtered_source.row_count:
            return html.Div("no data selected")

        fig = px.bar(
            filtered_source.create_pivot_table(),
            x=DataSchema.CATEGORY,
            y=DataSchema.AMOUNT,
            color=DataSchema.CATEGORY,
            labels={"category": i18n.t("general.category"), "amount": i18n.t("general.amount")},
        )

        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(id=ids.BAR_CHART)
