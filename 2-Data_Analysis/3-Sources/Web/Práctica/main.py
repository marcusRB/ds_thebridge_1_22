import requests
import pandas as pd
import os
from funciones import json_to_df
from variables import url, params

os.chdir(os.path.dirname(__file__))

# Primera llamada a la API
params['limit'] = 100
params['nameStartsWith'] = "M"
data = requests.get(url,params=params).json()

# Transoforma respuesta api a un df
df_1 = json_to_df(data)

# Segunda llamada a la API
params['offset'] = 100
data = requests.get(url,params=params).json()

# Transoforma respuesta api a un df
df_2 = json_to_df(data)

# Concatenamos ambos resultados
df_results_tot = pd.concat([df_1, df_2]).reset_index(drop=True)

# Guardamos los resultados en un csv
df_results_tot.to_csv('results_marvel_api.csv')

