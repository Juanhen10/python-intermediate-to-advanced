import os 
os.system('cls')
# Context manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho, modo):
    try:
        print('Abbrindo arquivo')
        arquivo = open(caminho, modo, encoding='utf8')
        yield arquivo
    except Exception as e:
        print('Ocorreu erro', e)
    finally:
        print('Fechando arquivo')
        arquivo.close()



with my_open('aula150.txt', 'w') as arquivo:
    arquivo.write('linha1\n')
    arquivo.write('linha2\n', 123)
    arquivo.write('linha3\n')
    print('WITH', arquivo)