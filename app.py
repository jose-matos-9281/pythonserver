from distutils.log import debug
from dash import Dash, html,dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("data/Base_de_datos_COVID.csv")
fig = px.bar(df, x="Nacionalidad", y = "CONFIRMADO" barmode="group" )

app.layout = html.Div( children=[
    html.H1(children='hello Dash'),
    html.Div(children='''
        Dash: A web application framework
    '''),
    dcc.Graph(
        id='ejemplo',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug= True)