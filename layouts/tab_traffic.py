import dash 
import plotly.express as px


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime
import pdb
#from app import app
from data import transforms_traffic 



#pctge_flights_per_terminal = transforms_traffic.pctge_flights_per_terminal


#fig = px.bar(pctge_flights_per_terminal,
#             labels={'index' : 'Terminal', 'value': 'Number of Flights [%]'})

df = transforms_traffic.data
days = datetime.timedelta(days=7)
max_date = datetime.datetime.strptime(max(df['To Date'].astype(str)), '%Y-%m-%d %H:%M:%S')
min_date = datetime.datetime.strptime(min(df['To Date'].astype(str)), '%Y-%m-%d %H:%M:%S')


layout = html.Div([

 #   html.H1("Traffic Data", style={'text align': 'center'}),
#H1 typical html header
#    dcc.Dropdown(id='month-dropdown',
#                options = [{'label': x, 'value': x} for x in df['Month'].unique()],
#                placeholder='Select a month'),
    dcc.DatePickerRange(
        id='date-picker-range-traffic',
        min_date_allowed=min_date,
        max_date_allowed=max_date,
        start_date = (max_date-days).strftime('%Y-%m-%d'),
        end_date = max_date.strftime('%Y-%m-%d'),
        initial_visible_month=max(df['Date']),
        stay_open_on_select=True,
        updatemode='bothdates',
            ),
    html.Div(id='fig-pct-flights-per-terminal'),
    html.Div(id='fig-pct-flights-per-runway'),
    html.Div(id='fig-pct-flights-per-runway-day'),
    html.Div(id='fig-count-top'),
    html.Div(id='fig-count-bottom')
    ])


