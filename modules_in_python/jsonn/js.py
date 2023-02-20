import json
import os
# from pprint import pprint
from typing import TypedDict

os.system('cls')
# o Que é Json?
# JSON - JavaScript Object Notation (extensão .json)
# É uma estrutura de dados que permite a serialização de objetos em textos simples
# para facilitar a transmissão de dados através da rede, APIs web ou outros meios de comunicação.
# O JSON supporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: São cadeias de carcteres, como "Olá, mundo!" ou "12345"
#    As strings devem ser envolvidas por aspas duplas
# Booleanos: são listas ordenas de valores, cmo [1,2,3] ou ["oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares nome/valor -> {"nome": "juan", "idade" : 15}
# null: é um valor especial que representa ausência de valor
#
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# True          true
# False         false
# None          null


class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imbd_rating: float
    year: int
    characters: list[str]
    budget: None | float


string_json = '''
{
    "title": "O senhor dos Anéis: A sociedade do Anel",
    "original_title": "The lord of the Rings: The Fellowship of the ring",
    "is_movie": true,
    "imbd_rating" : 8.8,
    "year": 2001,
    "characters": ["frod", "Sam", "Gandalf", "Legolas", "Boromir"],
    "buddget": null
}

'''
movie: Movie = json.loads(string_json)
# pprint(movie)
# print(movie['characters'][0])
# print(movie['characters'][1])
print(json.dumps(movie, ensure_ascii=False, indent=2))
