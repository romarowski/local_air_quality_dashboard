import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output


tabs_styles = {
    'height': '44px',
    'width': '95%'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'borderRight': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold', 
    'alignItems': 'center',
    'justifyContent': 'center'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'borderRight': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px',
}

tabs = html.Div([
    dcc.Tabs(id="tabs-styled-with-inline", value='tab-1', children=[
        dcc.Tab(label='Home', value='tab-1', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Traffic', value='tab-2', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Pollutants', value='tab-3', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Analysis', value='tab-4', style=tab_style, selected_style=tab_selected_style),
        dcc.Tab(label='Reports', value='tab-5', style=tab_style, selected_style=tab_selected_style),
    ], style=tabs_styles),
    html.Div(id='tabs-content-inline')
])
