import pandas as pd
import pickle

import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from navbar import Navbar


df = pd.read_csv('https://raw.githubusercontent.com/jayohelee/dash-tutorial/master/data/population_il_cities.csv')
df.set_index(df.iloc[:,0], drop=True, inplace=True)
df = df.iloc[:,1:]

nav = Navbar()

header = html.H3(
    'Select the name of an Illinois city to see its population!'
)

options = [{'label':x.replace(', Illinois', ''), 'value': x} for x in df.columns]
dropdown = html.Div(
    dcc.Dropdown(
        id='pop_dropdown',
        options=options,
        value='Abingdon City, Illinois'
    )
)

output = html.Div(
            id='output',
            children=[],
)

def App():
    layout = html.Div([
        nav,
        header,
        droptdown,
        output
    ])

    return layout


def build_graph(city):
    data = [go.Scatter(x = df.index,
                       y = df[city],
                       marker = {'color': 'orange'})]

    graph = dcc.Graph(
                figure = {
                    'data': data,
                    'layout': gp.layout(
                        title = '{} Population Change'.format(city),
                        yaxis = {'title': 'Population'},
                        hovermode = 'closest'
                    )
                }
    )

    return graph
