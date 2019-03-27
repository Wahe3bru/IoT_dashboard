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
# external_stylesheets = ['https://codepen.io/wahe3bru/pen/qvvewX.css']
external_stylesheets = ['https://unpkg.com/picnic',
                        "https://fonts.googleapis.com/css?family=Permanent+Marker"]

pallette = {'blue': '#1F77B4', 'orange': '#FF7F0E', 'green': '#44af69',
            'taupe': '#4a4238', 'cream': '#f7fff6'}

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': pallette['cream'], 'padding': '3em'}, children=[
    html.H1(children='Basic IoT Dashboard',
            style={'textAlign': 'center'}),

    html.Div(children='''A Basic layout of the IoT and weather api graphs ''',
             style={'textAlign': 'center'}),
    html.Div(className='Row'),
    html.Div(children=[
        html.Div(className='card', children=[
            html.Div(className="card-header", style={'backgroundColor': pallette['orange'],'textAlign': 'center'}, children='Current Temperature Outside'),
            html.Div(className="card-main", children=[html.H1(
                outside_df['temperature'].iloc[-1])], style={'font-family': 'Permanent Marker', 'textAlign': 'center', 'font-size':'2.5em'}),
            html.Div(className="footer", children='OpenWeatherMap',style={'textAlign': 'center'})
        ]),
        html.Div(className='card',children=[
            html.Div(className="card-header", style={'backgroundColor': pallette['blue'],'textAlign': 'center'}, children='Current Temperature Inside'),
            html.Div(className="card-main", children=[html.H1(
                sensor_df['temperature'].iloc[-1])], style={'font-family': 'Permanent Marker', 'textAlign': 'center', 'font-size':'2.5em'}),
            html.Div(className="main-description", children='DHT11 sensor',style={'textAlign': 'center'})
        ]),
        html.Div(className='card', children=[
            html.Div(className="card-header", style={'backgroundColor': pallette['green'],'textAlign': 'center'}, children='Logged today at:'),
            html.Div(className="card-main", children=[html.H1(
                sensor_df['timestamp'].iloc[-1].split(' ')[1])], style={'font-family': 'Permanent Marker', 'textAlign': 'center', 'font-size':'2.5em'}),
            html.Div(className="main-description", children=sensor_df['timestamp'].iloc[-1].split(' ')[0],style={'textAlign': 'center'})
        ]),
    ], className='flex three center'),

    html.Div(className='Row'),
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
                    title='Temperature: outside vs inside',
                )
            }
        )
    ], className="card"),

    dcc.Markdown('''#### Work In Progress
        I need to learn basic CSS and how to incorporate bootstrap or other
        frameworks to create functionally beautiful Dashboards.
    ''', className='main-description card'),

    html.Div([

    ]),

    html.Div([
        html.Div([
            html.H3(children='add description here'),
            html.P(children='Lorem ipsum dolor sit amet, consectetur adipisicing elit,\
                   sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
                    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\
                    nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in\
                   reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla\
                   pariatur. Excepteur sint occaecat cupidatat non proident, sunt in\
                    culpa qui officia deserunt mollit anim id est laborum.'),
        ], className="card"),

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
        ], className="two-third card"),
    ], className="flex three"),

])  # main div

if __name__ == '__main__':
    app.run_server(debug=True)
