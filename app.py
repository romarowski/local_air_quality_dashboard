import dash
import dash_bootstrap_components as dbc
import flask

server = flask.Flask(__name__)
app = dash.Dash(__name__)
app.server = server

app.config.suppress_callback_exceptions = True 
#there are callbacks to elements that don't exist in the app.layous as they're spread throughout 
#files
