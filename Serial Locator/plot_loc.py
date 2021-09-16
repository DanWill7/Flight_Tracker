# UDFs that provide functionality for PRODAQ the application to be used in main.py
# Author: Daniel Williams
# Date Created: 9/15/2021 9:26PM

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

def live_plot(filepath: str):
    """This function takes in a file locaction to read data and create a live plot of GPS Data.

    Args:
        filepath (str): relative path location for txt file to plot
    """

    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = html.Div(
        html.Div([
            html.H4('GPS Live Feed'),
            dcc.Graph(id='live-update-graph', figure= {}),
            dcc.Interval(
                id='interval-component',
                interval=500, # in milliseconds
                n_intervals=0
            )
        ])
    )

    # Multiple components can update everytime interval gets fired.
    @app.callback(Output('live-update-graph', 'figure'),
                Input('interval-component', 'n_intervals'))
    def update_graph_live(n):
        # Load in data.csv
        gps_data = pd.read_csv(filepath)
        # load data in on DF then specify latitude/longitude column names
        fig = px.line_mapbox(gps_data, lat="Latitude", lon="Longitude", color="color", zoom=3, height=1000)

        fig.update_layout(mapbox_style="stamen-terrain", mapbox_zoom=4, mapbox_center_lat = 41,
            margin={"r":0,"t":0,"l":0,"b":0})

        return fig


    app.run_server()

live_plot("D:\\Documents\\Programs\\Python\\MicroPython Projects\\Serial Locator\\GPS_Data\\data.csv")
