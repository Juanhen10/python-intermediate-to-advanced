# + Web Scraping com python usando requests e bs4 BeautifulSoup
# - Web scraping é o ato de "raspar a web" buscando informações de forma automatizada
# com determinada linguagem de programção, pra uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu código.
# Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML em formato de objetos Python para facilitar a vida do desenvolvedor.
# DOC: htps://www.crummy.com/software/BeaitofulSoup/bs4/doc.ptbr/
# Instalação
import re
from os import system

import requests
from bs4 import BeautifulSoup

system('cls')


url = 'http://localhost:3333/'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

if parsed_html.title is not None:
    print(parsed_html.title.text)
    print('-'*10)
top_kobs_heading = parsed_html.select_one('#intro > div > div> article > h2')

if top_kobs_heading is not None:
    article = top_kobs_heading.parent
    print(article)
    print('-'*10)
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
