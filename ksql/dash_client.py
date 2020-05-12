import asyncio

import dash
import dash_html_components as html
import pandas as pd
from dash.dependencies import Input, Output
from dash_table import DataTable
from dash_core_components import Graph, Interval

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

figure = {
    'data': [
        {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
        {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
    ],
    'layout': {
        'title': 'Dash Data Visualization'
    }
}


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Streaming query demo: ksql'),
    DataTable(
        id='live-update-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    Graph(id='live-update-graph',
          figure=figure
    ),
    Interval(
        id='interval-component',
        interval=1*1000, # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    Output(component_id='live-update-table', component_property='data'),
    [Input('interval-component', 'n_intervals')]
)
def update_table(df):
    import random
    df.append({'x': [random.randint(0,10), 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'New York'})
    return df.to_dict()

@app.callback(
    Output(component_id='live-update-graph', component_property='figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(df):
    from random import randint
    figure['data'].append({'x': [randint(1,10), 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'NYC'})
    return figure

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(app.run_server(debug=True))