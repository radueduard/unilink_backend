import json
import requests

geturl_facultate = 'http://127.0.0.1:8000/facultati/get_all'
posturl = 'http://127.0.0.1:8000/serii/create'

data = requests.get(geturl_facultate)
facultati = json.loads(data.text)

serii = ['AA', 'AB', 'AC', 'CA', 'CB', 'CC', 'CD']

for facultate in facultati:
    if facultate['name'] == 'Facultatea de Automatica si Calculatoare':
        for an in facultate['ani']:
            for serie in serii:
                r = requests.post(posturl, {'nume': serie, 'an': an['id']})
