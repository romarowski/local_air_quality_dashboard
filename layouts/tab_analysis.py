import pandas as pd
import dash 
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from data import transforms_pollutants, transforms_traffic
import datetime
import pdb

df_p = transforms_pollutants.data
df_t = transforms_traffic.data  
#pdb.set_trace()
days = datetime.timedelta(days=7)
max_date = datetime.datetime.strptime(max(df_p['To Date']), '%Y-%m-%d %H:%M:%S')
min_date = datetime.datetime.strptime(min(df_p['To Date']), '%Y-%m-%d %H:%M:%S')

layout = html.Div([
    dbc.Row(
        [
       #     dbc.Col(dcc.Dropdown(
       #         id='site-dropdown',
       #         options = [{'label': x, 'value': x} for x in df_p['Station'].unique()],
       #         placeholder='Select a site')),
        dbc.Col(dcc.Dropdown(
            id='pollutant-dropdown',
            options = [{'label': x, 'value': y} for x,y in
                zip(transforms_pollutants.pollutant_name,
                    transforms_pollutants.pollutants)],
            value='AQI',
            placeholder='Select a pollutant')),   
        dbc.Col(dcc.DatePickerRange(
            id='date-picker-range-analysis',
            min_date_allowed=min_date,
            max_date_allowed=max_date,
            start_date = (max_date - days),
            end_date = max_date,
            initial_visible_month=max(df_p['Date']),
            stay_open_on_select=True,
            updatemode='bothdates',
            ),
              ),
        dbc.Col(
        dcc.RadioItems(id='map-style',
            options=[
                {'label': 'Satellite ', 'value': 'satellite'},
                {'label': 'Streets', 'value': 'basic'}
                ],
            value='basic'
            ))
    #dbc.Col(dcc.DatePickerSingle(
        #    id='day-pick',
        #    min_date_allowed = min(df_p['To Date']),
        #    max_date_allowed = max(df_p['To Date']),
        #    placeholder='Select a day'))
    ]
), 
dbc.Row(
    [dbc.Col(html.Div(id='windspeed'), width=3),
     dbc.Col(html.Div(id='map-station'))]
     )
,
dcc.Slider(
    id="hour-slider-analysis",
    min=0,
    max=23,
    value=0,
    step=1,
    included=False,
    marks = {i : '{}h'.format(i) for i in range(24)},
        ),
# html.Div(id='hourly-weekday-fig'),
#   #  html.Br(),
dbc.Row([dbc.Col(html.Div(id='windrose-fig')),
   dbc.Col(html.Div(id='analysis-fig'))]),  
])

    

