import os
os.system('cls')
# @staticmethod (medodo estaticos) são inuteis em python
# Metodos estaticos são metodos que estão dentro da classe
# Mas não tem acesso ao self nem ao cls
# Em resumo, sõa funções que existem dentro da sua classse

class Classe:
    @staticmethod
    def funcao(*args, **kwargs):
        print('o1', args, kwargs)



c1 = Classe()
c1.funcao(1,2,3)
Classe.funcao(momeado = 1)