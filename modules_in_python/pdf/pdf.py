# PyPDF2 - Para manipular arquivos PDF
# PyPDF2 é uma biblioteca de manpulação de arquivos PDF de feita em Python puro, gratuita e de codigo aberto.
# Ela é capaz de ler, manipular, escrever e unir dados de arquivos PDF, assim como adiconar anotações, trasformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessária para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
import os
from pathlib import Path

from PyPDF2 import PdfMerger, PdfReader, PdfWriter

os.system('cls')


ROOT = Path(__file__).parent
PASTA_ORIGINAIS = ROOT / 'pdfs_originais'
PASTA_NOVA = ROOT / 'arquivos_novos'

RELATORIO_BACEN = PASTA_ORIGINAIS/'R20230310.pdf'
PASTA_NOVA.mkdir(exist_ok=True)


reader = PdfReader(RELATORIO_BACEN)


# print(len((reader.pages)))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]
# print(page0.extract_text())
# print(len(page0.images))
# print(page0.images[0])

# with open(PASTA_NOVA/imagem0.name, 'wb') as fp:
# fp.write(imagem0.data)


for i, page in enumerate(reader.pages):
    writer = PdfWriter()
    with open(PASTA_NOVA / f'page{i}.pdf', 'wb') as fp:
        writer.add_page(page)
        writer.write(fp)


files = [
    PASTA_NOVA / 'page1.pdf',
    PASTA_NOVA / 'page0.pdf'
]


marger = PdfMerger()
for file in files:
    marger.append(file)

with open(PASTA_NOVA / 'MERGED.pdf', 'wb') as fp:
    marger.write(fp)
