import json
import os
os.system('cls')
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
'''
SOLUÇÃO DO PROFESSOR.
'''

def listar(tarefas):
    print()
    if not tarefas:
        print('nenhuma tarefa para listar')
        return
    
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
    listar(tarefas)
    print()
        

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('nenhuma tarefa para desfazer')
        return
    
    tarefa = tarefas.pop()
    print(f'{tarefa} removida da lista de tarefa')
    tarefas_refazer.append(tarefa)  
    listar(tarefas)
    print()  
    

def refazer(tarfas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nehuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    print(f'{tarefa} adiconada novamente na lista de tarefa')
    tarefas.append(tarefa)
    listar(tarefas)
    print()
    
    
def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Nenhuma tarefa') 
        return
    tarefas.append(tarefa)
    print(f'{tarefa} adicionada na lista de tarefa')
    listar(tarefas)
    print()
        
tarefas = []
tarefas_refazer = []


while True:
    print('Comandos: listar, desfazer e refazer')
    tarefa = input('Digite uma tarefa ou comando: ')
    
    # comandos = {
    #     'listar': lambda: listar(tarefas),
    #     'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
    #     'refazer': lambda: refazer(tarefas, tarefas_refazer),
    #     'clear':lambda: os.system('cls'),
    #     'adicionar':lambda: adicionar(tarefa, tarefas),
    # }
    # comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
    #     comandos['adicionar'] 
    # comando()
    
    
    if tarefa == 'listar':
        listar(tarefas)
        
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        listar(tarefas)
        continue
    elif tarefa == 'clear':
        os.system('cls')
        continue
    else:
        adicionar(tarefa, tarefas)
        listar(tarefas)
        continue