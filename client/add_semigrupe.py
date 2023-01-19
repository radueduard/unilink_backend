import json
import requests

geturl = 'http://127.0.0.1:8000/facultati/get_all'
posturl = 'http://127.0.0.1:8000/semigrupe/create'

data = requests.get(geturl)
facultati = json.loads(data.text)

serii = ['AA', 'AB', 'AC', 'CA', 'CB', 'CC', 'CD']

for facultate in facultati:
    if facultate['num'] == 3:
        for an in facultate['ani']:
            for serie in an['serii']:
                for grupa in serie['grupe']:
                    requests.post(posturl, {'nume': "a", 'grupa': grupa['id']})
                    requests.post(posturl, {'nume': "b", 'grupa': grupa['id']})
