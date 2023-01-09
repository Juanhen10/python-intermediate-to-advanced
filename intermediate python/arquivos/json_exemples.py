
# JSON(JAvaScript Object Notation) é um formato leve de  troca de dados no formato de JavaScript objeto
import os 
import json
os.system('cls')




# pessoa = {
#     'nome': 'Juan Henrique',
#     'sobrenome': 'correia',
#     'endereços': [ 
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55},
#         ],
#     'altura': 1.7,
#     'numeros_preferidos': (4,7,17,10),
#     'dev': True,
#     'nada': None,
# }

# with open('json_exemple.json','w', enconding = 'utf8) as arquivo:
#     json.dump(pessoa, 
#               arquivo, 
#               ensure_ascii=False,
#               indent=2,)

with open('json_exemple.json','r' ) as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa,)
    print(pessoa['nome'])