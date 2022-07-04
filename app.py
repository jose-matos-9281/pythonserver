from distutils.log import debug
from itertools import count
from dash import Dash, html,dcc
import plotly.express as px
import pandas as pd
import numpy as np

app = Dash(__name__)

df = pd.read_csv("data/Base_de_datos_COVID.csv")

pd.pivot_table(df,index='Nacionalidad',columns='CONFIRMADO', values= "OBJECTID",aggfunc=np.count)
'''df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})'''

fig = px.bar(df, x="Nacionalidad", y = "CONFIRMADO", color = "SEXO", barmode="group" )
#fig = px.bar(df, x="Fruit", y = "Amount", color="City", barmode="group" )

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