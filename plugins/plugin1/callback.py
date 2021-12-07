import dash
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output
from flask import request
from global_variables import *
from app import app
from index import home_server

""" Imports
flask - To shut down the server
global variables - To reuse the common variables like plugin name across all the files
app - Holds the dash app
index-homes_server - To go to home server

"""

def shutdown():
    """ Shutdown the app server """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

plug_in_name = plug_in_name + '_'

@app.callback(Output(plug_in_name + 'display-value', 'children'), Input(plug_in_name + 'dropdown', 'value'))
def display_value(value):
    """ Dropdown value change """
    return 'You have selected "{}"'.format(value)


@app.callback(Output(plug_in_name + 'no-of-clicks', 'children'), Input(plug_in_name + 'event-detector', 'n_clicks'))
def do_nothing(n_clicks):
    """ To detect the number of button clicks """
    return str(n_clicks)


@app.callback(Output(plug_in_name + 'url', 'href'),
              [Input(plug_in_name + 'go-to-home', 'n_clicks')])
def display_page(*args):
    ctx = dash.callback_context
    if not ctx.triggered:
        PreventUpdate
    else:
        """ Shutdown the plugin server & go to home server """
        shutdown()
        return home_server
