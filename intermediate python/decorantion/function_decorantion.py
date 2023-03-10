import os
os.system('cls')
# Funções decoradoras e decoradores
# Decorar = adicionar / Remover / Restringir / Aleterar
# Funçções decoradoras são funções que decoram outras funções
# Decoradores são usadas para fazer o Python
# usar as funções decoradoras em outras funções
def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'o seu resultado foi {resultado}')
        print('ok, agora você foi decorada')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param,str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)