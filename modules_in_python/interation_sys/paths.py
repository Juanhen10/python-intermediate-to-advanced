# os.path trabalha com caminhos em Windows, linux e MAc
# os.path é um módylo que fornce funções para trabalhar com caminhos de arquivos é um módulo que fornece funções para trabalhar com caminhos de arquivos em
# Windows, MAc ou Linux sem precisar se preocupar com as diferenças entre esses sistemas
# Exemplos dos os.path:
# os.path.join: junta strings em um unico caminho
#         os.pathjoin('pasta1', 'pasta2', 'arquivo.txt') = pastas1\pasta2\arquivo.txt(Windows)
#                                                          pasta1/pasta2/arquivo.txt(mac e linux)
# os.path.split: divide um caminho uma tupla (diretorio, arquivo).
# por ecemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt).
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalah com caminhos de arquivos não faz nenhuma operação de entrada/saida (I/O) com arquivos em si.

import os

os.system('cls')


caminho = os.path.join('Desktop', 'curso', 'arquivo.txt')
print(caminho)
# os.path.split
diretorio, arquivo = (os.path.split(caminho))
print(diretorio)
# os.path.txt
caminho_Arquivo, extensao_arquivo = os.path.splitext(arquivo)
print(caminho_Arquivo)
# os.path.exists
print(os.path.exists('\\Users\\Juan Henrique\\Desktop\\pythonn'))
# os.path.abspath
print(os.path.abspath('.'))
# os.path.username
print(os.path.basename(caminho))
# os.ppath.dirname
print(os.path.dirname(caminho))
