import os
os.system('cls')
# dir, hasattr and getattr in python

# dir - traz todos atributos definidos no valor
# hasattr - checa se tem o objeto
# getatte checa se existe o metodo
string = 'Juan'
metodo = 'upper'
# print(dir(string))

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string,metodo)())
else:
    print('não existe o método',metodo)
