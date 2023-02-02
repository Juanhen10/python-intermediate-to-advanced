import os 
os.system('cls')
# metodo especial __call__
# callable é algo que pode ser executado com parênteses 
# Em calsses nromais, __call__ faz a instância de uma classe "callable"
class Callme:
    def __init__(self, phone):
        self.phone = phone
    
    def __call__(self, nome,*args, **kwds):
        print(nome,'Chamando', self.phone)
        return 1234


call1 = Callme('1213212')
retorno = call1('Juan')
print(retorno)