import sys, os


dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

# Import app
from app import app

""" Get arguments before importing call back; Callback needs the home server"""
home_server = "http://127.0.0.1:8050/"
port = 8051
try:
    """ Override the website name """
    home_server = sys.argv[2]
    """ If port number is given override the port number """
    port = int(sys.argv[1])
except:
    pass

# Import the layout & callbacks
import callback
from layout import layout

app.layout = layout

if __name__ == "__main__":
    app.run_server(debug=False, port=port)
