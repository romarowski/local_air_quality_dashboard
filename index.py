import dash 
import dash_table
#import plotly
import dash_core_components as dcc
import dash_html_components as html
#import plotly.graph_objs as go
#import plotly.express as px
import dash_auth
from dash.dependencies import Input, Output
#from plotly.subplots import make_subplots
from dash.exceptions import PreventUpdate
#from pandas.api.types import CategoricalDtype

#from datetime import date

import dash_bootstrap_components as dbc

#from app import app
from layouts import sidepanel, tab_traffic, tab_pollutants, tab_analysis,\
        tab_AQI_status, tab_pollutants_with_limit, home, AQI_status_map, \
        reports
from data import transforms_traffic, transforms_pollutants, coordinates,\
    location_data, home_gauges, home_gauges_now, tresholds, gauges_now,\
    gauges, filter_dates

from plotting import *#AQI_map, plot_traffic, plot_pollutant, plot_analysis, 
                     #plot_pollutant_all_stations 

#import pandas as pd

import pdb
#app = dash.Dash(__name__)

VALID_USERNAME_PASSWORD_PAIRS = {
        'envisa' : 'environment'
}


app = dash.Dash(__name__,
   external_stylesheets=[dbc.themes.BOOTSTRAP],

    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
   meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

auth = dash_auth.BasicAuth(
         app,
         VALID_USERNAME_PASSWORD_PAIRS
)
app.title = 'LAQ Monitoring'
server = app.server
app.config.suppress_callback_exceptions = True 

#set the app.layout 
app.layout = sidepanel.layout

maxi = max(transforms_pollutants.data['To Date'])
obj = datetime.strptime(maxi, '%Y-%m-%d %H:%M:%S')
year = obj.year
month_name = obj.strftime("%B")

@app.callback(Output('tabs-content-inline', 'children'),
              Input('tabs-styled-with-inline', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return home.layout
    elif tab == 'tab-2':
        return tab_traffic.layout
    elif tab == 'tab-3':
        return tab_AQI_status.layout
    elif tab == 'tab-4':
        return tab_analysis.layout
    elif tab == 'tab-5':
        return reports.layout


#@app.callback(Output('parent-content', 'children'),
#               #Output('sensor-info', 'children')],
#              [Input('traffic-button', 'n_clicks'),
#               Input('analysis-button', 'n_clicks'),
#               Input('AQI-button', 'n_clicks'),
#               Input('home-button', 'n_clicks')])
#def render_content(traffic_click, AQI_click, analysis_button, home_click): #, map_type):
#   ctx = dash.callback_context
#   if not ctx.triggered:    
#        return home.layout
#   else:
#       button_id = ctx.triggered[0]['prop_id'].split('.')[0]
#       if button_id == 'traffic-button':
#           #pdb.set_trace()
#           return tab_traffic.layout #, {}]
#       elif button_id =='AQI-button':
#           return tab_AQI_status.layout#, {}]     
#       elif button_id =='analysis-button':
#           return tab_analysis.layout#, {}]    
#       elif button_id == 'home-button':
#           #pdb.set_trace()
#           return home.layout
#
#############-------------Home Callback------------------------##########
@app.callback([Output('map-aqi', 'children'),
              Output('traffic-home', 'children'),
              Output('title_traffic', 'children')],
               Input('map-style', 'value'))
def update_figure(map_type):
    fig = AQI_map(coordinates.coords_df, transforms_pollutants.data,
            map_type)
    fig2, title = plot_weekly_traffic_trend(transforms_traffic.data_weekly)
    df = location_data.data
#    data_table = dash_table.DataTable(
#            id='table',
#            style_data={
#                'whiteSpace': 'normal',
#                'height': 'auto',
#                'lineHeight' : '15px'
#            },
#            style_cell_conditional=[
#                {'if': {'column_id': 'Measured Variable'},
#                    'width': '200px'},
#                ],
#           css=[
#               {
#                   'selector': 'table',
#                   'rule': 'width: 50%'
#             }],
#            columns = [{"name": i, "id": i} for i in df.columns],
#            data=df.to_dict('records')
#            )
    return [dcc.Graph(id='home_map', figure=fig), dcc.Graph(figure=fig2), title] 
            #data_table]
            #html.Img(src=app.get_asset_url('sensors.png'),
            #         style={'height':'10%',
            #                'width':'65%'})]
@app.callback([Output('gauge_O3', 'value'),
               Output('gauge_CO', 'value'),
               Output('gauge_NO2', 'value'),
               Output('gauge_SO2', 'value'),
               Output('gauge_PM25', 'value'),
               Output('gauge_PM10', 'value'),
               Output('title_gauges', 'children'),
               Output('treshold-PM10', 'value'),
               Output('treshold-PM10', 'color'),
               Output('treshold-O3', 'value'),
               Output('treshold-O3', 'color'),
               Output('treshold-CO', 'value'),
               Output('treshold-CO', 'color'),
               Output('treshold-NO2', 'value'),
               Output('treshold-NO2', 'color'),
               Output('treshold-SO2', 'value'),
               Output('treshold-SO2', 'color'),
               Output('treshold-PM25', 'value'),
               Output('treshold-PM25', 'color'),],
               Input('home_map', 'clickData'))
def update_gauges(selection):
    coloring = lambda x: 'red' if x > 0  else 'green'
    df1 = transforms_pollutants.data
    df8 = transforms_pollutants.data8
    df24 = transforms_pollutants.data24
    
    maxi = max(df1['To Date'])
    obj = datetime.strptime(maxi, '%Y-%m-%d %H:%M:%S')
    year = obj.year
    month = obj.month
    df1 = df1[(df1['Month Index']==month) &
                (df1['Year']==year)]
    df8 = df8[(df8['Month Index']==month) &
                (df8['Year']==year)]
    df24 = df24[(df24['Month Index']==month) &
                (df24['Year']==year)]

    
    if selection is None:
        station='Privet Aviation'
        limits = home_gauges.values(transforms_pollutants.data)
        values = home_gauges_now.values(limits)
        title = 'Averaged concentrations and treshold exceedances for: ' +\
                station + ' during ' + month_name + ' ' + str(year)
        data = tresholds.count(df1, df8, df24, limits, station)
        return values['O3'], values['CO'], values['NO2'], values['SO2'],\
            values['PM25'], values['PM10'], title, data['PM10'],\
            coloring(data['PM10']), data['O3'], coloring(data['O3']),\
            data['CO'], coloring(data['CO']), data['NO2'], \
            coloring(data['NO2']), data['SO2'], coloring(data['SO2']),\
            data['PM25'], coloring(data['PM25'])
    else:
        station=selection['points'][0]['hovertext']
        limits = home_gauges.values(transforms_pollutants.data, station)
        values = home_gauges_now.values(limits)
        title = 'Averaged concentrations and treshold exceedances for: ' +\
                station + ' during ' + month_name + ' ' + str(year)
        data = tresholds.count(df1, df8, df24, limits, station)
        return  values['O3'], values['CO'], values['NO2'], values['SO2'],\
            values['PM25'], values['PM10'], title, data['PM10'],\
            coloring(data['PM10']), data['O3'], coloring(data['O3']),\
            data['CO'], coloring(data['CO']), data['NO2'], \
            coloring(data['NO2']), data['SO2'], coloring(data['SO2']),\
            data['PM25'], coloring(data['PM25'])


                     
                     
##############-------------Traffic Callback--------------------###########
@app.callback([Output('fig-pct-flights-per-terminal', 'children'),
               Output('fig-pct-flights-per-runway', 'children'),          
               Output('fig-pct-flights-per-runway-day', 'children'),
               Output('fig-count-top', 'children'),
               Output('fig-count-bottom', 'children')],
              [Input('date-picker-range-traffic', 'start_date'),
               Input('date-picker-range-traffic', 'end_date')])
def update_figure(start_date, end_date):
    if  start_date is not None and end_date is not None:
        fig, fig2, fig3 = plot_traffic_date(transforms_traffic.data, start_date, end_date)
        fig4, fig5 = plot_traffic_bars(start_date, end_date, transforms_traffic.data)
        
        
        return [dcc.Graph(figure=fig), dcc.Graph(figure=fig2), 
                dcc.Graph(figure=fig3), dcc.Graph(figure=fig5),
                dcc.Graph(figure=fig4)]
    else:
        raise PreventUpdate



########################-------Pollutants callback----------############

#Callback for first appearance of AQI_Status tab

@app.callback(Output('map-AQI-placeholder', 'children'),
             [Input('my-date-picker-range', 'start_date'),
              Input('my-date-picker-range', 'end_date'),
              Input('see-by-station', 'n_clicks'),
              Input('see-with-limit', 'n_clicks')])
def update_figure(start_date, end_date, n_by_station, n_with_limit):
    ctxt = dash.callback_context
    button_idd = ctxt.triggered[0]['prop_id'].split('.')[0]
    if start_date is not None and end_date is not None and n_by_station is None and n_with_limit is None:
        return AQI_status_map.layout
    #[dcc.Graph(figure=fig), {}]
    elif start_date is not None and end_date is not None and button_idd == 'see-by-station':
       return tab_pollutants.layout
    elif start_date is not None and end_date is not None and button_idd == 'see-with-limit':
       return tab_pollutants_with_limit.layout
    else:
        raise PreventUpdate

##############-------------AQI MAP CALLBACK---------------##############
@app.callback(Output('map-aqi-p', 'figure'),
              [Input('map-style', 'value'),
               Input('my-date-picker-range', 'start_date'),
               Input('my-date-picker-range', 'end_date')])
def update_figure(map_style, start_date, end_date):
        fig = AQI_map_date(start_date, end_date,
                           coordinates.coords_df, transforms_pollutants.data,
                           map_style)
        return fig

#############--------------GAUGES CALLBACK----------------#############
@app.callback([Output('gauge_p_O3', 'value'),
               Output('gauge_p_CO', 'value'),
               Output('gauge_p_NO2', 'value'),
               Output('gauge_p_SO2', 'value'),
               Output('gauge_p_PM25', 'value'),
               Output('gauge_p_PM10', 'value'),
               Output('title_gauges_p', 'children'),
               Output('treshold-PM10_p', 'value'),
               Output('treshold-PM10_p', 'color'),
               Output('treshold-O3_p', 'value'),
               Output('treshold-O3_p', 'color'),
               Output('treshold-CO_p', 'value'),
               Output('treshold-CO_p', 'color'),
               Output('treshold-NO2_p', 'value'),
               Output('treshold-NO2_p', 'color'),
               Output('treshold-SO2_p', 'value'),
               Output('treshold-SO2_p', 'color'),
               Output('treshold-PM25_p', 'value'),
               Output('treshold-PM25_p', 'color')],
              [Input('map-aqi-p', 'clickData'),
               Input('my-date-picker-range', 'start_date'),
               Input('my-date-picker-range', 'end_date')])
def update_gauges(selection, start_date, end_date):
    coloring = lambda x: 'red' if x > 0  else 'green'
    start_date_object = date.fromisoformat(start_date)
    start_date_s = start_date_object.strftime('%B %d, %Y')
    end_date_object = date.fromisoformat(end_date)
    end_date_s = end_date_object.strftime('%B %d, %Y')
    if selection is None:
        station='Privet Aviation'
        limits = gauges.values(start_date, end_date, transforms_pollutants.data)
        values = gauges_now.values(limits)

        title = 'Averaged concentrations and treshold exceedances for: ' +\
                station + ' from ' + start_date_s + ' to  ' + end_date_s
        df1 = filter_dates.filtered(start_date, end_date, 
                transforms_pollutants.data)
        df8 = filter_dates.filtered(start_date, end_date, 
                transforms_pollutants.data8)
        df24 = filter_dates.filtered(start_date, end_date, 
                transforms_pollutants.data24)
        data = tresholds.count(df1, df8, df24, limits, station)
        return   values['O3'], values['CO'], values['NO2'], values['SO2'],\
            values['PM25'], values['PM10'], title, data['PM10'],\
            coloring(data['PM10']), data['O3'], coloring(data['O3']),\
            data['CO'], coloring(data['CO']), data['NO2'], \
            coloring(data['NO2']), data['SO2'], coloring(data['SO2']),\
            data['PM25'], coloring(data['PM25'])
    else:
        station=selection['points'][0]['hovertext']
        limits = home_gauges.values(transforms_pollutants.data, station)
        values = home_gauges_now.values(limits)
        title = 'Averaged concentrations and treshold exceedances for: ' +\
                station + ' from ' +start_date_s + ' to ' + end_date_s
        df1 = filter_dates.filtered(start_date, end_date, 
                transforms_pollutants.data)
        df8 = filter_dates.filtered(start_date, end_date, 
                transforms_pollutants.data8)
        df24 = filter_dates.filtered(start_date, end_date, 
                transforms_pollutants.data24)
        data = tresholds.count(df1, df8, df24, limits, station)
        return  values['O3'], values['CO'], values['NO2'], values['SO2'],\
            values['PM25'], values['PM10'], title, data['PM10'],\
            coloring(data['PM10']), data['O3'], coloring(data['O3']),\
            data['CO'], coloring(data['CO']), data['NO2'], \
            coloring(data['NO2']), data['SO2'], coloring(data['SO2']),\
            data['PM25'], coloring(data['PM25'])



    
    


#Callback for see by station tabin AQI_Status tab

@app.callback([Output('tab-pollutants', 'children'),
               Output('hourly-monthly-weekday-fig','children')],
               #Output('map-AQI-placeholder-more-info', 'children')],
              [Input('my-date-picker-range', 'start_date'),
               Input('my-date-picker-range', 'end_date'), 
               Input('site-dropdown', 'value'),
               #Input('month-dropdown', 'value'),
               Input('pollutant-dropdown', 'value')])
def update_figure(start_date, end_date, site, pollutant):
    if site is not None and pollutant is not None:
        fig, fig1 = plot_pollutant_date(site, start_date, end_date, pollutant,
                                   transforms_pollutants.data, 
                                   transforms_pollutants.pollutants)
        #fig3 = AQI_map_date(start_date, end_date,
        #                   coordinates.coords_df, transforms_pollutants.data)
        return [dcc.Graph(figure=fig1), dcc.Graph(figure=fig)]#, dcc.Graph(figure=fig3)]
    else:    
        #fig3 = AQI_map_date(start_date, end_date,
        #                   coordinates.coords_df, transforms_pollutants.data)
        #return [{}, {}, dcc.Graph(figure=fig3)]
        raise PreventUpdate


#Callback for see with limit tab in AQI status

@app.callback(Output('tab-pollutants-limit', 'children'),
               #Output('map-AQI-placeholder-more-info', 'children')],
              [Input('my-date-picker-range', 'start_date'),
               Input('my-date-picker-range', 'end_date'), 
               Input('site-dropdown-multi', 'value'),
               #Input('month-dropdown', 'value'),
               Input('pollutant-dropdown-multi', 'value')])
def update_figure(start_date, end_date, site, pollutant):
    if site is not None and pollutant is not None:
        #Logic for picking the correct dataset
        lim = transforms_pollutants.limits
        #pdb.set_trace()
        if pollutant in lim['Pollutant'].to_numpy():
            if lim[lim["Pollutant"]==pollutant]['Averaging time [h]'].to_numpy()[0] == 24:
                df = transforms_pollutants.data24
                title = '24 hour average'
            elif lim[lim["Pollutant"]==pollutant]['Averaging time [h]'].to_numpy()[0] == 8:
                df = transforms_pollutants.data8
                title = '8 hour average'
            else:
                df = transforms_pollutants.data
                title = '1 hour average'
        else:
            df = transforms_pollutants.data
            title = '1 hour average'


        fig = plot_pollutant_multi_stations_date(start_date, end_date, pollutant, 
                                          df, site, transforms_pollutants.limits,
                                          title)
        #fig3 = AQI_map_date(start_date, end_date,
        #                   coordinates.coords_df, transforms_pollutants.data)
        return dcc.Graph(figure = fig) #, dcc.Graph(figure=fig3)]
    else:    
        #fig3 = AQI_map_date(start_date, end_date,
        #                   coordinates.coords_df, transforms_pollutants.data)
        #return [{}, {}, dcc.Graph(figure=fig3)]
        raise PreventUpdate

###############-------ANALYSIS CALLBACK-------##########

@app.callback([Output('analysis-fig', 'children'),
              Output('windrose-fig','children'),
              Output('map-station', 'children'), 
              Output('windspeed', 'children')],              
              [Input('date-picker-range-analysis', 'start_date'),
               Input('date-picker-range-analysis', 'end_date'),
               Input("hour-slider-analysis", 'value'),
               Input('pollutant-dropdown', 'value'),
               Input('map-style', 'value')])
def update_figure(start_date, end_date, hour,  pollutant, map_style):
    if start_date is not None and end_date is not None and pollutant is not None:
        site, date_value = find_pollutant_max(pollutant, start_date, end_date,
                                              transforms_pollutants.data)
        #pdb.set_trace()
        fig = plot_analysis(site, date_value, pollutant,
                            transforms_traffic.data, transforms_pollutants.data)
        fig2 = plot_windrose(site, date_value, transforms_pollutants.data)
        fig3 = plot_pollutant_hour_date(date_value, hour, site, 
                                        coordinates.coords_df, transforms_pollutants.data, 
                                        pollutant, transforms_traffic.data, 
                                        transforms_pollutants.runway_loc, map_style)
        fig4 = plot_wind_speed_direction(date_value, hour, site, transforms_pollutants.data)
        return [dcc.Graph(figure=fig), dcc.Graph(figure=fig2), dcc.Graph(figure=fig3),
                dcc.Graph(figure=fig4)]                  
    else:
        raise PreventUpdate


if __name__ == '__main__':
    app.run_server(debug = True, threaded=True)


