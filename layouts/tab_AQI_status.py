import dash_daq as daq
import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
#from app import app
from layouts import card_layout
#from data import coordinates
#import plotly.express as px
from data import transforms_pollutants, transforms_traffic, home_gauges
import datetime

df_p = transforms_pollutants.data
df_t = transforms_traffic.data  
days = datetime.timedelta(days=7)
max_date = datetime.datetime.strptime(max(df_p['To Date']), '%Y-%m-%d %H:%M:%S')
min_date = datetime.datetime.strptime(min(df_p['To Date']), '%Y-%m-%d %H:%M:%S')
#coords_df = coordinates.coords_df
#fig = px.scatter_mapbox(coords_df, lat="lat", lon="lon", hover_name="Station",
#        color_discrete_sequence=["fuchsia"], zoom=12, height=400) 
#fig.update_layout(mapbox_style="open-street-map") 
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 

layout = html.Div([
       html.Br(),
       dbc.Row([
                dbc.Col(dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=min_date,
                    max_date_allowed=max_date,
                    start_date=(max_date-days).strftime('%Y-%m-%d'),
                    end_date=max_date.strftime('%Y-%m-%d'),
                    initial_visible_month=max(df_p['Date']),
                    stay_open_on_select=True,
                    updatemode='bothdates',
                        ), width=3
                       ),
                #dbc.Col(daq.BooleanSwitch(
                #    id='bool-info-pollutants',
                #    on=False,
                #    label='More information'
                #        )
                dbc.Col([dbc.Button('Multi chart by station', outline=True, color='success',
                    className='mr-1', id='see-by-station'),
                         dbc.Button('Single chart multi-station with limit', outline=True, color='success',
                    className='mr-1', id='see-with-limit')])
                ]),         
        html.Div(id='map-AQI-placeholder'),
            ])
    
