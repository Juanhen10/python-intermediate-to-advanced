import os
os.system('cls')
# groupby - agrupando valores (itertools)
from itertools import groupby

aluno = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabiricio', 'nota': 'A'},
    {'nome': 'Juan', 'nota': 'A'},
    {'nome': 'Victor', 'nota': 'C'},
    {'nome': 'gabriel', 'nota': 'B'},
    {'nome': 'Gustavo', 'nota': 'C'},
    {'nome': 'Luffy', 'nota': 'A'},
]

def ordena(aluno):
    return aluno['nota']

aluno_agrupados = sorted(aluno, key=ordena)

grupos = groupby(aluno_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)



# grupos = groupby((aluno))

# for chave, grupo in grupos:
#     print(chave)
#     print(list(grupo))


# alunos = ['a','a','a','b','b','b','c','c','c',]
# grupos = groupby(sorted(alunos))
