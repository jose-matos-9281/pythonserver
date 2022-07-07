# importar librerias

from distutils.log import debug
from itertools import count
from dash import Dash, html,dcc
import plotly.express as px
import pandas as pd
import numpy as np
import datetime as dt

# funciones definidas
def num(data,col):
    '''
    limpia la data numerica que tiene un caracter extra '-1
    '''
    for i in col:
        data[i]= data[i].str.replace("'","").astype("int32")
    return data

def data_pivot(data,serie):
    '''
    dado un dataframe crea la serie de tiempo por provincias, segun el parametro solicitado
    '''
    Frame = data.pivot_table(
        index = "fecha",
        columns = 'Provincia',
        values = serie
    )
    return Frame

#Filtra cuales provincias seran usadas
filtro_P = lambda data,prov: data[data.Provincia.isin(prov)]

#Filtra la data por un periodo especifico de tiempo
def filtro_F (data,inicio = dt.datetime(2020,3,19), fin = dt.datetime(2022,7,3)): 
    return data[[data['fecha']>= inicio] and [data['fecha'] <= fin][0]]



def diferencia(serie):
    '''
    dada una serie de tiempo obtiene la serie con la diferencia de valore entre cada periodo
    '''
    a = [serie[0]]
    for i in range(1,len(serie)):
        a.append(serie[i]-serie[i-1])
    return a


# lectura de los datos

hosp = pd.read_csv('data/hospitalizacion.csv')
data = pd.read_csv('data/data.csv')

# limpieza de los datos
data['fecha']= pd.to_datetime(data['fecha'])
data = num(data,['Confirmados', 'Fallecidos', 'Muestras','Recuperados'])
hosp['fecha']= pd.to_datetime(hosp['fecha'])





# aplicacion Dash
app = Dash(__name__)


#Creacion de la estructura de la pagina 
app.layout = html.Div( children=[
    html.H1(children='hello Dash'),
    html.Div(children='''
        Dash: A web application framework
    '''),
    dcc.Graph(
    )
])

#Creacion de callbacks, o llamadas


# correr servidor
if __name__ == '__main__':
    app.run_server(debug= True)