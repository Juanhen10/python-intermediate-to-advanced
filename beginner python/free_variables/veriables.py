import os 
os.system('cls')
# print(globals())
# def fora(x):
#     a = x
#     def dentro():
#         # print(locals())
#         print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)

# print(dentro1())
# print(dentro2())

def concatenar(string_inicial):
    valor = string_inicial
    
    def interna(valor_a_concatenar):
        nonlocal valor
        valor += valor_a_concatenar
        return valor
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))

