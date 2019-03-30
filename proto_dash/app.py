import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import helper_dash
import datetime

external_stylesheets = ["https://codepen.io/wahe3bru/pen/jJjwvB.css",
    'https://unpkg.com/picnic',
    "https://fonts.googleapis.com/css?family=Permanent+Marker"]

# Data
sensor_df = helper_dash.worksheet_as_df('IoT_env', 'Mar-2019')
outside_df = helper_dash.worksheet_as_df('Outside_env', 'Mar-2019')

now = datetime.datetime.now()

# id='dcc-g1'
dropdown_options = [{'label':'last 24 hours', 'value': (now - datetime.timedelta(hours=24))},
                    {'label':'last 7 days', 'value': (now - datetime.timedelta(days=7))},
                    {'label':'last 30 days', 'value': (now - datetime.timedelta(days=30))},
                    {'label':'all logs', 'value': (now - datetime.timedelta(days=365))}]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

######################### APP Layout ###########################################
app.layout = html.Div(children=[
    html.Div(["logo"], className="box a", id="logo"),
    html.Div(["nav-bar"], className="box b", id="nav"),

    html.Div(["kpi-home"], className="box c", id="kpi-home"),
    # 2 cards
    html.Div(
    children=[html.Div(className="flex two", children=[
        html.Div([
            html.Article(className="card", children=[
                html.Div(className="", children=['Current Temperature Outside']),
                html.Div(className="footer", children=[outside_df['temperature'].iloc[-1]],
                    style={'font-family': 'Permanent Marker', 'textAlign': 'center', 'font-size':'2.5em'}
                ),
                html.Div(className="", children=['OpenWeatherMap']),
            ], style={'backgroundColor': 'black'})
        ]),
        html.Div([
            html.Article(className="card", children=[
                html.Div(className="", children=['Logged today at:']),
                html.Div(className="footer", children=[sensor_df['timestamp'].iloc[-1].split(' ')[1]], style={'font-family': 'Permanent Marker', 'textAlign': 'center', 'font-size':'2.5em'}),
                html.Div(className="", children=[sensor_df['timestamp'].iloc[-1].split(' ')[0]]),
            ], style={'backgroundColor': 'black'})
        ]),
    ]),
    ], id="kpi-api", className="box d"),

    html.Div(["weather pic"], className="box pic", id="weather-pic"),
    html.Div(["dilly graph"], className="box e graph1", id="daily-graph"),
    html.Div(["Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."], className="box f", id="text"),
    html.Div(["daily-stat"], className="box g graph2", id="daily-stat"),
    html.Div(["text will change depending on mouse location"], className="box mouse-txt", id="mouse-txt"),
    html.Div(["alt-graph"], className="box h graph3", id="alt-graph"),
    html.Div(["text depends on alt-graph selected"], className="box alt-txt", id="alt-txt"),
    html.Div([
        dcc.Dropdown(
            id='dcc-g1',
            options=dropdown_options,
            value=(now - datetime.timedelta(hours=24))
    ),
    ], className="box i graph1"),
    html.Div(["dcc-g2"], className="box j graph2", id="dcc-g2"),
    html.Div(["dcc-g3"], className="box k graph3", id="dcc-g3"),
    html.Footer(["box footer"], className="box footer"),
], className="wrapper")

######################### Updating #############################################

@app.callback(
    Output(component_id='daily-graph', component_property='children'),
    [Input(component_id='dcc-g1', component_property='value')]
)
def update_sensor_graph(input_value):
    if input_value < sensor_df['timestamp'].min():
        input_value = sensor_df['timestamp'].min()
    filter_df_in = sensor_df[sensor_df['timestamp'] >= input_value]
    filter_df_out = outside_df[outside_df['timestamp'] >= input_value]
    return [dcc.Graph(
        figure={
            'data': [
                go.Scatter(
                    x=filter_df_in['timestamp'],
                    y=filter_df_in['temperature'],
                    mode='lines+markers',
                    name='DHT sensor (lounge)'
                ),
                go.Scatter(
                    x=filter_df_out['timestamp'],
                    y=filter_df_out['temperature'],
                    mode='lines+markers',
                    name='Outside temperature'
                ),
            ],
            'layout': go.Layout(
                title='Temperature: outside vs inside',
                height=270,
            )
        }
    )]

if __name__ == '__main__':
    app.run_server(debug=True)
