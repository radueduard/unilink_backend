import json
import requests

geturl = 'http://127.0.0.1:8000/facultati/get_all'
posturl = 'http://127.0.0.1:8000/ani/create'

data = requests.get(geturl)
facultati = json.loads(data.text)

for facultate in facultati:
    print(facultate['name'])
    for i in range(4):
        r = requests.post(url=posturl, data={'num': i + 1, 'facultate': facultate['id']})
        print(r.status_code)
