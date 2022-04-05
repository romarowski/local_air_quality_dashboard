import pandas as pd
import dash_daq as daq
import dash 
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from data import transforms_pollutants

layout = html.Div([
    dbc.Row(
        [
     #dbc.Col(html.Div(id='title-AQI'), width=6),
     dbc.Col(dcc.Dropdown(
        id='site-dropdown-multi',
        options = [{'label': x, 'value': x} for x in transforms_pollutants.data['Station'].unique()],
                placeholder='Select a site', multi=True) ),
    # dbc.Col(dcc.Dropdown(
    #    id='month-dropdown',
    #    options = [{'label': x, 'value': x} for x in transforms_pollutants.data['Month'].unique()],
    #        placeholder='Select a month'), width=1),
     dbc.Col(dcc.Dropdown(
        id='pollutant-dropdown-multi',
        options = [{'label': x, 'value': y} for x,y in zip(transforms_pollutants.pollutant_name,
                                                           transforms_pollutants.pollutants)],
        placeholder='Select a pollutant'))
     
        #dbc.Col(daq.BooleanSwitch(
        #    id='bool-info-limits',
        #    on=False,
        #    label='See pollutant concentration with allowable limits'))
                                
        ]
    ),
  dbc.Row(
      [
    #dbc.Col(html.Div(id='map-AQI-placeholder-more-info'), width=6),
     dbc.Col(html.Div(id='tab-pollutants-limit')),
   # html.Div(id='hourly-weekday-fig'),
   #   #  html.Br(),
   ]),
#  dbc.Row(
#      [
#          #dbc.Col(html.Div(), width=6), 
#          dbc.Col(html.Div(id='hourly-monthly-weekday-fig')),  
#    
#    ])
])
    
        

