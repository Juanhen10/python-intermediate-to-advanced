import os
os.system('cls')
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura)
# w (escrita)
# x (para criação)
# a (escreve ao final) 
# b (binário)
# t (modo texto), + (leitura e escrita)

# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho = 'text'

# arquivo = open(caminho,'w')
# #
# arquivo.close()

# with open(caminho, 'w+') as arquivo:
#     print('Arquivo aberto e fechando.\n')
#     arquivo.write('Escrevendo com comando = WRITE\n')
#     arquivo.write('quebra de linha\n')
    
#     arquivo.writelines(
#         ('linha 4\n', 'Linha 5\n')
#     )
#     print('lendo')
#     arquivo.seek(0,0)
    
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print()
#     print('READLINES')
#     for linha in arquivo.readlines():
#         print(linha.strip())


# with open(caminho,'r') as arquivo:
#     print('lendo arquivos com comando = READ()')
#     print(arquivo.read())
#     print(arquivo.readline())

with open(caminho, 'w', encoding='utf-8') as arquivo:
   for escreve in range(1,5):
       print(arquivo.write(f'atenção {escreve}\n'))
       
# os.unlink(caminho)  
# os.rename(caminho, 'tex2')