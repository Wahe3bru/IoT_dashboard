import dash
import datetime
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

today = datetime.datetime.strptime("2018-02-28 21:46", '%Y-%m-%d %H:%M')
available_indicators = {"last 1": (today - datetime.timedelta(hours=24)),
                        "last 7": (today - datetime.timedelta(days=7)),
                        "last month": (today - datetime.timedelta(days=30)),
                        "all logs": today}

app.layout = html.Div([
    html.Div([
        html.Div(id="my-div"),
        dcc.Dropdown(
            id='my-id',
            options=[{'label': k, 'value': v} for i,(k, v) in enumerate(available_indicators.items())],
            value= today
        ),
  ])
])
@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)


if __name__ == '__main__':
    app.run_server(debug=True)
