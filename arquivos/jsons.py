import json
import os

# pessoa = {
#     'nome': 'Juan Henrique',
#     'sobrenome': 'correia',
#     'ebdereços': [ 
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#         ],
#     'altura': 1.7,
#     'numeros_preferidos': (4,7,17,10),
#     'dev': True,
#     'nada': None,
# }

# BASE_DIR = os.path.dirname(__file__)
# JSON_FILE = os.path.join(BASE_DIR, 'arquivo-python.json')

# # with open(SAVE_TO, 'w+') as file:
# #     json.dump(pessoa, file, indent=2)
    

# # print(json.dumps(pessoa, indent=2))


# with open(JSON_FILE, 'r+') as file:
#     pessoas = json.load(file)
#     print(json.dumps(pessoas, indent= 2))
    # for p in pessoas:
    #     print(pessoas['nome'])
    
json_string = '''
[{
    "name": "juan",
    "lastname": "Henrique",
    "age": 20,
    "addresses": [
        {"line1": "av.brasil"},
        {"line2": "av.brasil2"}
    ]
}]
'''

pessoas = json.loads(json_string)

for p in pessoas:
    print(p['name'])