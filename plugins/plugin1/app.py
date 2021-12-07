import dash
from global_variables import *

""" Define the dash app once; To avoid multiple instances """
app = dash.Dash(__name__, suppress_callback_exceptions=True, title=plug_in_name, external_stylesheets=external_stylesheets)
