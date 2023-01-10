import json
import os
os.system('cls')

def linha(msg = None):
    if msg is None:
        print(f'--'*15)
    else:
        print(f'-{msg}-')
        print('--'*15)


def save(file, letra):
    with open(file, letra, encoding='utf8') as file:
        json.dump(lista, file, indent= 2)


def ler(file, letra):
    with open(file, letra,encoding='utf8') as file:
        task = json.load(file)
        for pos, item in enumerate(task):
            print(f'{pos}------{item}')

             
      


    
lista = []
BASE_DIR = 'C:\\Users\\Juan.Henrique\\Desktop\\pythonn\\challenge\\task'
JSON_FILE = os.path.join(BASE_DIR, 'list-task.json')

# with open(JSON_FILE, 'w', encoding='utf8') as file:
#     json.dump(lista, file, indent=2)
    
while True:
    opc = int(input('ecolhas as opções: \n[1] - Criar tarefa \n[2]- Refazer lista\n[3]- Deletar algum item da lista\n[4]- ver lista\n[5] - Sair \nQual opc:  '))
    linha()
    if opc == 1:
        tarefas = str(input('Digite uma tarefa: '))
        lista.append(tarefas)
        print('tarefa criada!')
        save(JSON_FILE, 'w')
        linha()
        continue
    elif opc == 2:
        refaz = str(input('Quer refazer? [S/N]: ')).upper()
        if refaz == 'S':
            lista.clear()
            print('Tarefas limpas')
            linha
        save(JSON_FILE, 'w')
        if refaz == 'N':
            continue
    elif opc == 3:
        ler(JSON_FILE,'r')
        deletar = input('delete uma tarefa: ')
        for key, item in enumerate(lista):
            lista.pop(key)
        save(JSON_FILE,'w')
    elif opc == 4:
        linha('lista de tarefas')
        ler(JSON_FILE,'r')
        linha()
    elif opc == 5:
        print('volte sempre!')
        linha()
        break
        
with open(JSON_FILE, 'w', encoding='utf8') as file:
        json.dump(lista, file, indent=2)




# BASE_DIR = '\\Users\\Juan.Henrique\\Desktop\pythonn\\challenge\\task'

    