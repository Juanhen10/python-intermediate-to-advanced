import os 
os.system('cls')
# Criando Exceptions em Python Orientado a Objetos 
# Para cirar uma Exeception em Python, você só precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# Criando exceções (comum colocar Error ao final )
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MyError(Exception):
    ...


class OutroError(Exception):
    ...



def levantar():
    exception_ = MyError('a', 'b', 'c')
    exception_.add_note('você errou isso')
    raise exception_ 

try:
    levantar()
except (ZeroDivisionError, MyError) as error:
    print(error.__class__.__name__)
    print(error.args)
    print()
    exception_ = OutroError('Vou lançar de novo')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error