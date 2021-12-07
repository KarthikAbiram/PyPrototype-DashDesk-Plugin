""" Importing dependencies """
from reusables.check_url_alive import check_website
from threading import Thread
import webview
import sys
import subprocess
import json
import os
from dash.dependencies import Input, Output, ALL
import dash
from dash import dcc, html

""" 
ALL used to have pattern matching callbacks - Refer pattern matching callbacks for more details 
JSON- To convert string to python dict 
sys, Sub Process  - To start another python file 
Reusables - Importing custom reusables 
webview - Used to render webpage in desktop
Thread - Used to start app in another thread
"""

""" Global variables """
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css',
                        "https://codepen.io/chriddyp/pen/brPBPO.css"]

home_port_number = 8050
home_server = "http://127.0.0.1:" + str(home_port_number) + "/"

plug_in_port_number = 8051
plug_in_server = "http://127.0.0.1:" + str(plug_in_port_number) + "/"

app = dash.Dash(__name__, title="Home",
                external_stylesheets=external_stylesheets)


def get_plugin_names(plug_ins_directory):
    """ Get all the directory name inside the plugins directory """
    plug_in_names = []
    for path in os.listdir(plug_ins_directory):
        full_path = os.path.join(plug_ins_directory, path)
        if os.path.isdir(full_path):
            plug_in_names.append(path)
    return plug_in_names


plug_ins_directory = os.path.join(os.getcwd(), 'plugins')


plug_ins_names = get_plugin_names(plug_ins_directory)


plug_ins_buttons = []

""" Get plug in buttons with link; Tag A is used to attach the link """
for name in plug_ins_names:
    """ Creating a list of plugin buttons with a link for routing"""

    plug_ins_buttons.extend(
        [html.A(html.Button(name), id={"type": "plug-in", "id": name}), html.Br()])

""" To avoid muliple n_clicks worked, created a variable; n_clicks is the button click property to capture button clicks """
trigger_property = 'n_clicks'

app.layout = html.Div([html.Div(plug_ins_buttons),
                       dcc.Location(id='url')
                       ])


@ app.callback(Output('url', 'href'), Input({"type": "plug-in", "id": ALL}, trigger_property))
def change_page(*args):
    """ Store call back contents """
    ctx = dash.callback_context
    """ If trigger is not received i.e button is not clicked do nothing """
    if not ctx.triggered:
        pass
    else:
        """ Find which plug in button is clicked """
        button_id_str = ctx.triggered[0]['prop_id'].rstrip(
            "." + trigger_property)
        button_id_dic = json.loads(button_id_str)
        plug_in_name = button_id_dic["id"]

        """ Form the plug in script path to call """
        plug_in_path = rf"plugins\{plug_in_name}\index.py"

        """ Call the python script """
        subprocess.Popen(sys.executable + " " +
                         plug_in_path + " " + str(plug_in_port_number) + " " + home_server)

        """ Wait for the website to come alive """
        if check_website(plug_in_server):
            print("Plug in Process Started Successfully")
        return plug_in_server


if __name__ == '__main__':
    def run_app():
        app.run_server(debug=False)

    """ Start the app in new thread """
    t = Thread(target=run_app)
    t.daemon = True
    t.start()

    """ Start the desktop application """
    window = webview.create_window('PDMAT', home_server)
    webview.start(debug=True)
