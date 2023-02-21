import os
from pathlib import Path

os.system('cls')
# Usamos a pathlib
# para trabalhar com caminhos, pastas e arquivos
# de forma que um código funcione em Windows, Linux e MAC
#
# HArd coding é uma prática não recomendada de utiliza valores
# fixos no código fonte da aplicação

caminho_projeto = Path()
print(caminho_projeto.absolute())


caminho_arquivo = Path(__file__)
print(caminho_arquivo)


ideias = caminho_arquivo.parent / 'ideias'
print(ideias / 'arquivo.txt')

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
caminho_arquivo.touch()
caminho_arquivo.write_text('Olá mundo')
caminho_arquivo.unlink()

caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)  # criar pastas
subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)


outro_arquivo = subpasta / 'arquivo.txt'
outro_arquivo. touch()
outro_arquivo.write_text('sarve')


files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'files_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    with file.open('a+') as text_file:
        text_file.write('Olá mundo\n')
        text_file.write(f'file_{i}.txt')


def rmtree(root, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('DIR: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE', file)
            file.unlink()
    if remove_root:
        root.rmdir()


rmtree(caminho_pasta)

# if remove_root:
#     root.rmdir()

# caminho_pasta.rmdir() # apagar pastas

# arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

# arquivo.touch()  # criar
# print(arquivo)
# arquivo.write_text('Olá mundo')
# print(arquivo.read_text())
# arquivo.unlink()  # apagar


# caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# caminho_arquivo.write_text('')

# with caminho_arquivo.open('a+') as file:
#     file.write('Uma linha \n')
#     file.write('Outra linha \n')

# print(caminho_arquivo.read_text())
