import json
import os

os.system('cls')

NOME_ARQUIVO = 'test.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

movie = {
    'title': 'O senhor dos Anéis: A sociedade do Anel',
    'original_title': 'The lord of the Rings: The Fellowship of the ring',

    'is_movie': True,
    'imbd_rating': 8.8,
    'year': 2001,
    'characters': ['frod', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'buddget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    json.dump(movie, arquivo, ensure_ascii=False, indent=2)


with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
    movie_json = json.load(arquivo)
    print(movie_json)
