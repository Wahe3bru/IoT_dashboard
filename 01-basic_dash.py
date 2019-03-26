import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import helper_dash

sensor_df = helper_dash.worksheet_as_df('IoT_env', 'Mar-2019')
outside_df = helper_dash.worksheet_as_df('Outside_env', 'Mar-2019')
daily_stat_df = helper_dash.worksheet_as_df('daily_stats', '2019')

# external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
external_stylesheets = ['https://codepen.io/wahe3bru/pen/qvvewX.css']
pallette = {'blue': '#1F77B4', 'orange': '#FF7F0E', 'green': '#44af69',
          'taupe': '#4a4238', 'cream': '#f7fff6'}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': pallette['cream']}, children=[
    html.H1(children='Basic IoT Dashboard',
            style={'textAlign': 'center'}),

    html.Div(children='''A Basic layout of the IoT and weather api graphs ''',
             style={'textAlign': 'center'}),

    html.Div(className='Row', style={'justify-content': 'center'}, children=[
        html.Div(className='card three columns', children=[
            html.Div(className="card-header", style={'backgroundColor': pallette['orange']}, children='Current Temperature Outside'),
            html.Div(className="card-main", children=[html.H1(
                outside_df['temperature'].iloc[-1])]),
            html.Div(className="main-description", children='OpenWeatherMap')
        ]),
        html.Div(className='card three columns',children=[
            html.Div(className="card-header", style={'backgroundColor': pallette['blue']}, children='Current Temperature Inside'),
            html.Div(className="card-main", children=[html.H1(
                sensor_df['temperature'].iloc[-1])]),
            html.Div(className="main-description", children='DHT11 sensor')
        ]),
        html.Div(className='card three columns', children=[
            html.Div(className="card-header", style={'backgroundColor': pallette['green']}, children='Logged today at:'),
            html.Div(className="card-main", children=[html.H1(
                sensor_df['timestamp'].iloc[-1].split(' ')[1])]),
            html.Div(className="main-description", children=sensor_df['timestamp'].iloc[-1].split(' ')[0])
        ]),
    ]),

    html.Div(className='row'),



    html.Div([
        dcc.Graph(
            id='temps',
            figure={
                'data': [
                    go.Scatter(
                        x=sensor_df['timestamp'],
                        y=sensor_df['temperature'],
                        mode='lines+markers',
                        name='DHT sensor (lounge)'
                    ),
                    go.Scatter(
                        x=outside_df['timestamp'],
                        y=outside_df['temperature'],
                        mode='lines+markers',
                        name='Outside temperature'
                    ),
                ],
                'layout': go.Layout(
                    title='temperature from DHT11',
                )
            }
        )
    ],
    style={'className': 'nine columns'}),

    dcc.Markdown('''#### Work In Progress
        I need to learn basic CSS and how to incorporate bootstrap or other
        frameworks to create functionally beautiful Dashboards.
    ''', className='main-description'),

    html.Div([
        dcc.Graph(id='daily_temp',
        figure={
            'data': [
                go.Scatter(
                    x=daily_stat_df['Date'],
                    y=daily_stat_df['Temperature-Mean'],
                    line = dict(
                        color = (pallette['green']),
                        width = 6),
                    error_y=dict(
                        type='data',
                        symmetric=False,
                        array=daily_stat_df['Temperature-Max']-daily_stat_df['Temperature-Mean'],
                        arrayminus=daily_stat_df['Temperature-Mean']-daily_stat_df['Temperature-Min'],
                        thickness=4.5,
                        width=6,
                    )
                )
            ],
            'layout': go.Layout(
                title='Daily temperature stats',
            )
        })
    ])

])  # main div

if __name__ == '__main__':
    app.run_server(debug=True)
