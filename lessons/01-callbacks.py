import dash
import datetime
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import helper_dash
import datetime


sensor_df = helper_dash.worksheet_as_df('IoT_env', 'Mar-2019')
outside_df = helper_dash.worksheet_as_df('Outside_env', 'Mar-2019')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
now = datetime.datetime.now()
dropdown_options = [{'label':'last 24 hours', 'value': (now - datetime.timedelta(hours=24))},
                    {'label':'last 7 days', 'value': (now - datetime.timedelta(days=7))},
                    {'label':'last 30 days', 'value': (now - datetime.timedelta(days=30))},
                    {'label':'all logs', 'value': (now - datetime.timedelta(days=365))}]

today = datetime.datetime.strptime("2018-02-28 21:46", '%Y-%m-%d %H:%M')

app.layout = html.Div([
    dcc.Dropdown(
        id='dropdown',
        options=dropdown_options,
        value=(now - datetime.timedelta(hours=24))
),
    html.Div(id='my-div')
])
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='dropdown', component_property='value')]
)
def update_output_div(input_value):
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
            )
        }
    )]


if __name__ == '__main__':
    app.run_server(debug=True)
