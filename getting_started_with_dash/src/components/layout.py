from dash import Dash, html

from ..data.source import DataSource
from . import year_dropdown, month_dropdown, category_dropdown, bar_chart, pie_chart


# def create_layout(app: Dash) -> html.Div:
#     return html.Div(
#         className="app-div",
#         children=[
#             html.H1(app.title),
#             html.Hr(),
#             html.Div(className="dropdown-container", children=[year_dropdown.render(app)]),
#             bar_chart.render(app),
#         ],
#     )


def create_layout(app: Dash, source: DataSource) -> html.Div:
    return html.Div(
        className="app-div",
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(app, source),
                    month_dropdown.render(app, source),
                    category_dropdown.render(app, source),
                ],
            ),
            bar_chart.render(app, source),
            pie_chart.render(app, source),
        ],
    )
