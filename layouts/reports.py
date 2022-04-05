import dash
import dash_html_components as html
import dash_core_components as dcc

layout = html.Div(
        [
            html.Br(),
            html.A(
                'Report April 2021',
                href="/assets/Report_April_2021.pdf",
                target="_blank",
                ),
            html.Br(),
            html.A(
                'Report March 2021',
                href="/assets/Report_March_2021.pdf",
                target="_blank",
                ),
            html.Br(),
            html.A(
                'Report February 2021',
                href="/assets/Report_February_2021.pdf",
                target="_blank",
                )
            ]
        )
