import dash_bootstrap_components as dbc
import dash_html_components as html
from data import transforms_traffic 

cards = dbc.CardGroup(
    [

        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Home"),
                    dbc.Button(
                        'Go',
                        outline=False,
                        color='success',
                        id='home-button'
                        )
                ]
                )
            ),

        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Weekly Traffic Trend", className="card-title"),
                  #  html.P(
                  #      "This card has some text content, which is a little "
                  #      "bit longer than the second card.",
                  #      className="card-text",
                  #  ),
                    dbc.Button(
                       transforms_traffic.button_format['text'], 
                       color=transforms_traffic.button_format['color'], 
                       className="mt-auto", id="traffic-button"
                        ),
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("AQI Status", className="card-title"),
                 #   html.P(
                 #       "Acceptable in all stations?",
                 #       className="card-text",
                 #   ),
                    dbc.Button(
                        "Click Here", color="secondary", className="mt-auto",
                        id='AQI-button',
                    ),
                ]
            )
        ),
        dbc.Card(
            dbc.CardBody(
                [
                    html.H5("SmartInsight™", className="card-title"),
                  #  html.P(
                  #      "This card has some text content, which is longer "
                  #      "than both of the other two cards, in order to "
                  #      "demonstrate the equal height property of cards in a "
                  #      "card group.",
                  #      className="card-text",
                  #  ),
                    dbc.Button(
                        "Click here", color="primary", className="mt-auto", id='analysis-button',
                    ),
                ]
            )
        ),
    ]
)
