import json
import os
os.system('cls')

def linha(msg = None):
    if msg is None:
        print(f'--'*15)
    else:
        print(f'-{msg}-')
        print('--'*15)
    
lista = []
BASE_DIR = 'C:\\Users\\Juan.Henrique\\Desktop\\pythonn\\challenge\\task'
JSON_FILE = os.path.join(BASE_DIR, 'list-task.json')

with open(JSON_FILE, 'w', encoding='utf8') as file:
    json.dump(lista, file, indent=2)
    
while True:
    opc = int(input('ecolhas as opções: \n[1] - Criar tarefa \n[2]- Refazer lista\n[3]- Deletar algum item da lista\n[4]- ver lista\n[5] - Sair \nQual opc:  '))
    linha()
    if opc == 1:
        tarefas = str(input('Digite uma tarefa: '))
        lista.append(tarefas)
        print('tarefa criada!')
        linha()
        continue
    if opc == 2:
        refaz = str(input('Quer refazer? [S/N]: ')).upper()
        if refaz == 'S':
            lista.clear()
            print('Tarefas limpas')
            linha
        if refaz == 'N':
            continue
    if opc == 3:
        try:
            for pos, itens in enumerate(lista):
                print(f'{pos}-----{itens}')
            delete = int(input("Qual tarefa quer deletar: "))
            if delete == pos:
                lista.pop(pos)
                print('item deletado!')
                linha()
        except:
            print('não tem itens na lista')
            linha()
            continue
    if opc == 4:
        linha('lista de tarefas')
        with open(JSON_FILE, 'w', encoding='utf8') as file:
             json.dump(lista, file, indent=2)
        for i in lista:
            print(i)
        linha()
    if opc == 5:
        print('volte sempre!')
        linha()
        break
        
BASE_DIR = '\\Users\\Juan.Henrique\\Desktop\pythonn\\challenge\\task'

    