import json
import requests

geturl_facultate = 'http://127.0.0.1:8000/facultati/get_all'
posturl = 'http://127.0.0.1:8000/grupe/create'

data = requests.get(geturl_facultate)
facultati = json.loads(data.text)


def make_num(param, param1, i):
    return 100 * param + 10 * param1 + i


for facultate in facultati:
    if facultate['num'] == 3:
        for an in facultate['ani']:
            for serie in an['serii']:
                for i in range(5):
                    r = requests.post(
                        url=posturl,
                        data={
                            'num': make_num(facultate['num'], an['num'], i + 1),
                            'serie': serie['id']
                        }
                    )
