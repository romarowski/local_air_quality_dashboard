import dash 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
from layouts import card_layout, tabs
#from data import coordinates
#import plotly.express as px
from data import transforms_pollutants, transforms_traffic

df_p = transforms_pollutants.data
df_t = transforms_traffic.data  
#coords_df = coordinates.coords_df
#fig = px.scatter_mapbox(coords_df, lat="lat", lon="lon", hover_name="Station",
#        color_discrete_sequence=["fuchsia"], zoom=12, height=400) 
#fig.update_layout(mapbox_style="open-street-map") 
#fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) 

layout = html.Div([
    tabs.tabs,
   # dbc.Row(
   #     [
   # dbc.Col(html.Div(id='parent-content')),
   # dbc.Col(html.Img(src=app.get_asset_url('sensors.png')))
   #     ]),
    #html.Label('Map style'),
    html.Div(id='parent-content'),
    #html.Br(), html.Br(),
    #html.Div(id='sensor-info'),
   # html.Img(src=app.get_asset_url('sensors.png')),
    html.A([
            html.Img(
                src=app.get_asset_url('logo.png'),
                style={
                    'height' : '5%',
                    'width' : '5%',
                    'float' : 'right',
                    'position' : 'absolute',
                    'top' : 0,
                    'right' : 0
                })
    ], href='https://www.env-isa.com/', target='_blank' )
   # dcc.Graph(figure=fig)
      

])

