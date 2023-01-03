import os 

os.system('cls')
# Funções recursivas e recursividade
# Funções que podem se chmar de volta
# - uteis p/ dividir problemas grandes em partes menores 
# Toda função recursiva deve ter:
#  - Um problema que possa ser dividido em partes menores
#  - Um caso recursivo que resolve o pequeno problema
#  - Um caso base que para a recursão 
#  - fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120


# def  recursiva(inicio = 0 , fim=10):
#     # Caso base
#     if inicio >= fim:
#         return fim
    
#     print(inicio, fim)
    
#     # Caso recursivo
#     # contar até chegar ao final
#     inicio += 1
#     return recursiva(inicio,fim)

# print(recursiva(3,15)) 

def factorial(n):
    if n <=1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(10))
