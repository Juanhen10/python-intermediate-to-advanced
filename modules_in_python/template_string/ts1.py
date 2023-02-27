# String.Template para substituir variáveis em textos
# Métodos:
# substitute: substitui mas gera eros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Voce também pode trocar o delimitador e outras coisas criando uma subclasse tamplate.
import locale
# import os
import string
from datetime import datetime
from pathlib import Path

LOCAL = Path(__file__).parent / 'ts1.txt'

# os.system('cls')

locale.setlocale(locale.LC_ALL, '')


def converte_para_br1(numero: float | int) -> str:
    brl = 'R$ ' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl


data = datetime(2022, 12, 28)
dados = dict(
    nome='João',
    valor=converte_para_br1(1_234_456),
    data=data.strftime('%d/%m/%Y'),
    empresa='O. M.',
    telefone='+55 (11) 7890-5432'
)


# print(json.dumps(dados, indent=2, ensure_ascii=False))
texto = '''
Prezado(a) $nome,

Informamos que sua mensalidade será cobrada no valor de ${valor} no dia $data. Caso deseje cancelar o serviço, 
entre em contato com a $empresa pelo telefone $telefone.

Atenciosamente,

${empresa}
'''


class MyTemplate(string.Template):
    delimiter = '%'


with open(LOCAL, 'r') as file:
    texto = file.read()
    template = string.Template(texto)
    print(template.substitute(dados))
