import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import helper_dash

sensor_df = helper_dash.worksheet_as_df('IoT_env', 'Mar-2019')
outside_df = helper_dash.worksheet_as_df('Outside_env', 'Mar-2019')
daily_stat_df = helper_dash.worksheet_as_df('daily_stats', '2019')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
pallette = {'blue': '#1F77B4', 'orange': '#FF7F0E', 'green': '#44af69',
          'taupe': '#4a4238', 'cream': '#f7fff6'}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': pallette['cream']}, children=[
    html.H1(children='Basic IoT Dashboard',
            style={'textAlign': 'center'}),

    html.Div(children='''A Basic layout of the IoT and weather api graphs ''',
             style={'textAlign': 'center'}),
    html.Div(children=[
    html.Div(style={'backgroundColor': pallette['orange'], 'textAlign': 'center'},
        children=[
        html.H5(children='Current temperature outside'),
        html.H3(children=outside_df['temperature'].iloc[-1],
            style={'color': 'red'}),
    ], className='four columns'),

    html.Div(style={'backgroundColor': pallette['blue'], 'textAlign': 'center'},
        children=[
        html.H5(children='Current temperature indoors'),
        html.H3(children=sensor_df['temperature'].iloc[-1],
            style={'color': 'red'})
    ], className='four columns'),


    html.Div(style={'backgroundColor': pallette['green'], 'textAlign': 'center'},
        children=[
        html.H5(children='Logged today at:'),
        html.H3(children=sensor_df['timestamp'].iloc[-1].split(' ')[1],
            style={'color': 'red'})
    ], className='four columns'),
    ], className='row'),

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
