from dash import dcc, html
from global_variables import *

plug_in_name = plug_in_name + '_'


""" Layout for the plugin app """
layout = html.Div([html.H3(plug_in_name),
                   dcc.Dropdown(id=plug_in_name + 'dropdown', options=[
                       {'label': '{} - {}'.format(plug_in_name, i), 'value': i} for i in ['NYC', 'MTL', 'LA']]),
                   html.Div(id=plug_in_name + 'display-value'),
                   html.Button("Event Detector",
                               id=plug_in_name + 'event-detector'),
                   html.Div(id=plug_in_name + 'no-of-clicks'),
                   dcc.Location(id=plug_in_name + 'url'),
                   html.Button("Go to Home", id=plug_in_name + 'go-to-home')
                   ])
