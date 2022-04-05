import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_daq as daq
from data import transforms_pollutants, home_gauges
limits = home_gauges.values(transforms_pollutants.data)
CO = limits[limits["Pollutant"]=='CO (mg/m³)']['Limits'].iloc[0]
NO2 = limits[limits["Pollutant"]=='NO₂ (µg/m³ )']['Limits'].iloc[0]
SO2 = limits[limits["Pollutant"]=='SO₂ (µg/m³)']['Limits'].iloc[0]
O3 = limits[limits["Pollutant"]=='O₃ (µg/m³ )']['Limits'].iloc[0]
PM25 = limits[limits["Pollutant"]=='PM₂.₅ (µg/m³ )']['Limits'].iloc[0]
PM10 = limits[limits["Pollutant"]=='PM₁₀ (µg/m³)']['Limits'].iloc[0]

layout = html.Div([
    html.Div(
        [
        dcc.RadioItems(id='map-style',
            options=[
                {'label': 'Satellite ', 'value': 'satellite'},
                {'label': 'Streets', 'value': 'basic'}
                ],
            value='basic'
            ),
        ],
        style={
            'display': 'inline-block',
            'position': 'absolute',
            'width': '300px',
            'right': '0px',
            'padding': '10px'
            }
        ),
    html.Br(), html.Br(),
    dcc.Graph(id='map-aqi-p'),
    #html.Div(id='map-aqi-poll-tab'),
    html.Br(),
    dbc.Card(
        [
            
        dbc.CardHeader(html.Div(id='title_gauges_p',
                                style={
                                      'fontSize': 16,
                                      'color': 'black'
                                     }),
                                ),
        dbc.Row(
            [
                dbc.Col([daq.Gauge(
                    id='gauge_p_O3',
                    color={'gradient':False,'ranges':{'green':[0, O3*.9],
                        'yellow':[O3*.9, O3],
                        'red':[O3, 1.5*O3]}},
                    label='O₃ (µg/m³)',
                    scale={'start':0,'interval': .5*O3,
                        'labelInterval': 1},
                    max=1.5*O3,
                    min=0,
                    size=150,
                    ),
                   # html.Div(id='treshold-O3_p',
                   #     style={
                   #         'textAlign': 'center',
                   #         'fontSize': 18
                   #         })
                        ]
                ),
                dbc.Col([daq.Gauge(
                    id='gauge_p_CO',
                    color={'gradient':False,'ranges':{'green':[0,CO*.9],
                        'yellow':[CO*.9,CO],'red':[CO,1.5*CO]}},
                    label='CO (mg/m³)',
                    scale={'start':0,'interval': .5*CO, 'labelInterval': 1},
                    max=1.5*CO,
                    min=0,
                    size=150,
                    ),
                   # html.Div(id='treshold-CO_p',
                   #     style={
                   #         'textAlign': 'center',
                   #         'fontSize': 18
                   #         })
                        ]
                ),
                dbc.Col([daq.Gauge(
                    id='gauge_p_NO2',
                    color={'gradient':False,'ranges':{'green':[0,NO2*.9],
                        'yellow':[NO2*.9,NO2],'red':[NO2,NO2*1.5]}},
                    label='NO₂ (µg/m³)',
                    scale={'start':0,'interval': .5*NO2, 'labelInterval': 1},
                    max=NO2*1.5,
                    min=0,
                    size=150,
                    ),
                  #  html.Div(id='treshold-NO2_p',
                  #      style={
                  #          'textAlign': 'center',
                  #          'fontSize': 18
                  #          })
                        ]
                ),
                dbc.Col([daq.Gauge(
                    id='gauge_p_SO2',
                    color={'gradient':False,'ranges':{'green':[0,SO2*.9],
                        'yellow':[SO2*.9,SO2],'red':[SO2,SO2*1.5]}},
                    label='SO₂ (µg/m³)',
                    scale={'start':0,'interval': .5*SO2, 'labelInterval': 1},
                    max=SO2*1.5,
                    min=0,
                    size=150,
                    ),
                  #  html.Div(id='treshold-SO2_p',
                  #      style={
                  #          'textAlign': 'center',
                  #          'fontSize': 18
                  #          })
                        ]
                ),
                dbc.Col([daq.Gauge(
                    id='gauge_p_PM25',
                    color={'gradient':False,'ranges':{'green':[0,PM25*.9],
                        'yellow':[PM25*.9,PM25],'red':[PM25,PM25*1.5]}},
                    label='PM₂.₅ (µg/m³)',
                    scale={'start':0,'interval': .5*PM25, 'labelInterval': 1},
                    max=PM25*1.5,
                    min=0,
                    size=150,
                    ),
                  #  html.Div(id='treshold-PM25_p',
                  #      style={
                  #          'textAlign': 'center',
                  #          'fontSize': 18
                  #          })
                        ]
                ),
                dbc.Col([daq.Gauge(
                    id='gauge_p_PM10',
                    color={'gradient':False,'ranges':{'green':[0,PM10*.9],
                        'yellow':[PM10*.9,PM10],'red':[PM10,PM10*1.5]}},
                    label='PM₁₀ (µg/m³)',
                    scale={'start':0,'interval': .5*PM10, 'labelInterval': 1},
                    max=PM10*1.5,
                    min=0,
                    size=150,
                    ),
                #   html.Div(id='treshold-PM10_p',
                #        style={
                #            'textAlign': 'center',
                #            'fontSize': 18
                #            })
                    ]
                )
            ]
        ),
        html.Hr(),
        html.H6("Exceedances", 
                style={
                    'textAlign': 'center'
                    }
                ),
        dbc.Row(
                [
                    dbc.Col(daq.LEDDisplay(
                        id='treshold-O3_p',
                        value=0,                      
                        style={
                            'justifyContent': 'center',
                            'display': 'flex'
                            }
                            
                        ),
                        align='center'),
                    dbc.Col(daq.LEDDisplay(
                        id='treshold-CO_p',
                        value=0,
                        style={
                            'justifyContent': 'center',
                            'display': 'flex'
                            }

                        )),
                    dbc.Col(daq.LEDDisplay(
                        id='treshold-NO2_p',
                        value=0,
                        style={
                            'justifyContent': 'center',
                            'display': 'flex'
                            }

                        )),
                    dbc.Col(daq.LEDDisplay(
                        id='treshold-SO2_p',
                        value=0,
                        style={
                            'justifyContent': 'center',
                            'display': 'flex'
                            }

                        )),
                    dbc.Col(daq.LEDDisplay(
                        id='treshold-PM25_p',
                        value=0,
                        style={
                            'justifyContent': 'center',
                            'display': 'flex'
                            }

                        )),
                    dbc.Col(daq.LEDDisplay(
                        id='treshold-PM10_p',
                        value=0,
                        style={
                            'justifyContent': 'center',
                            'display': 'flex'
                            }

                        )),
                ],
            )
    ],
    #className="w-75 mb-3")
    style={"width": "85%",
           "left": "10px"})
    ])
    
