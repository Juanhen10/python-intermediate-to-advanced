import os 
os.system('cls')
# Context Manger com Classes Você pode implementar seu proprios protocolos apenas implementando os dunder methodos que o Python vai usar. 
# Isso é chamado de Duck Typing. 
# Um conceito relacionado com tippagem diânima onde o Python não está interessado no tipo, 
# mas se alguns métods exisatem no objeto para que ele funcine de forma adequada.
# Duck Typing:
# Quando vejo um pássaro que caminha como um pato, nada como
# um pato e grasna como pato, eu chamo aquele passari de pato
# PAra criar um contet manager, os métodos __enter__e _exit__ devem ser implementados.
# O método __exit_- recebá a classe de exceção, a exceção e traceback. Se ele tretornar True, exceção no with será suprimidas.
# EX:
# with open('aula149.txt', 'w') as arquivo:
class myOpen:
    def __init__(self, caminho, modo):
        self.caminho = caminho
        self.modo = modo
        self._arquivo = None
    
    def __enter__(self):
        print('ABRINDO ARQUIVO')
        self._arquivo = open(self.caminho, self.modo, encoding='utf8')
        return self._arquivo
    
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('FECHANDO ARQUIVO')
        self._arquivo.close()
        


with myOpen('aula149','w') as arquivo:
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.write('Linha 3\n')
    print('With', arquivo) 