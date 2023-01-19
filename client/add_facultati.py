import requests

endpoint = 'http://127.0.0.1:8000/facultati/create'

facultati = [
    "Facultatea de Inginerie Electrica",
    "Facultatea de Energetica",
    "Facultatea de Automatica si Calculatoare",
    "Facultatea de Electronica, Telecomunicatii si Tehnologia Informatiei",
    "Facultatea de Inginerie Mecanica si Mecatronica",
    "Facultatea de Inginerie Industriala si Robotica",
    "Facultatea de Ingineria Sistemelor Biotehnice",
    "Facultatea de Transporturi",
    "Facultatea de Inginerie Aerospatiala",
    "Facultatea de Stiinta si Ingineria Materialelor",
    "Facultatea de Inginerie Chimica si Biotehnologii",
    "Facultatea de Inginerie in Limbi Straine",
    "Facultatea de Stiinte Aplicate",
    "Facultatea de Inginerie Medicala",
    "Facultatea de Antreprenoriat, Ingineria si Managementul Afacerilor"
]

for facultate in facultati:
    r = requests.post(
        url=endpoint,
        data=
        {
            'num': facultati.index(facultate) + 1,
            'name': facultate,
        }
    )
    print(r.json())
    print(r.status_code)
