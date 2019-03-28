import dash
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ["https://codepen.io/wahe3bru/pen/jJjwvB.css",
    'https://unpkg.com/picnic',
    "https://fonts.googleapis.com/css?family=Permanent+Marker"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

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
                html.Div(className="footer", children=["26"], style={'font-family': 'Permanent Marker', 'textAlign': 'center', 'font-size':'2.5em'}),
                html.Div(className="", children=['OpenWeatherMap']),
            ], style={'backgroundColor': 'black'})
        ]),
        html.Div([
            html.Article(className="card", children=[
                html.Div(className="", children=['Logged today at:']),
                html.Div(className="", children=['10:30'], style={'font-family': 'Permanent Marker', 'textAlign': 'center', 'font-size':'2.5em'}),
                html.Div(className="footer", children=['28-03-2019']),
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
    html.Div(["dcc-g1"], className="box i graph1", id="dcc-g1"),
    html.Div(["dcc-g2"], className="box j graph2", id="dcc-g2"),
    html.Div(["dcc-g3"], className="box k graph3", id="dcc-g3"),
    html.Footer(["box footer"], className="box footer"),
], className="wrapper")

if __name__ == '__main__':
    app.run_server(debug=True)
