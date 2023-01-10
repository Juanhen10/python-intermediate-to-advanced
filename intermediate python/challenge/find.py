'''
Exercício
Crie um função que encontra o primeiro duplicado considerando o 
segundo número como a duplicação.
Requisitos:
    A ordem do número duplicado é considerada a partir da segunda 
    ocorrência do número, ou seja, o número duplicado em si.
    Exemplo:
        [1,2,3,3,2,1] -> 1,2, e 3 são duplicados (retorne 3)
        [1,2,3,4,5,6] -> Retorne -1 (não tem duplicaods)
    se não encontrar duplicados na lista, retorne -1
    
(exercise
Create a function that finds the first duplicate given the
second number as doubling.
Requirements:
    The order of the duplicate number is considered from the second
    occurrence of the number, that is, the duplicated number itself.
    Example:
        [1,2,3,3,2,1] -> 1,2, and 3 are doubled (back 3)
        [1,2,3,4,5,6] -> Return -1 (has no duplicates)
    if no duplicates are found in the list, return -1)
'''
import os 
os.system('cls')


lista_num = [[1,2,3,4,5,6,7,7,8,10],
         [9,1,8,99,7,2,1,6,8],
         [1,3,2,2,8,6,5,9,6,7],
         [3,8,2,8,6,7,7,3,1,7],
         [1,3,7,2,2,1,5,1,9,9],
         [10,2,2,1,3,5,10,5,9,2,5,7],
         [1,3,7,1,10,5,9,2,5,7],
         [4,7,6,5,2,9,2,1,2,1],
         [5,3,1,8,5,7,1,8,8,7],
         [10,9,8,7,6,5,4,3,2,1]
]

def primeiro_duplicado(lista):
    numeros_checados = set()
    primeiro_duplicado = -1
    
    for num in lista:
        if num in numeros_checados:
            primeiro_duplicado = num
            break
        
        numeros_checados.add(num)
       
        
    return primeiro_duplicado

for lista in lista_num:
    print(lista)
    print(f'primeiro número: {primeiro_duplicado(lista)}')