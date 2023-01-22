import os
os.system('cls')
# Relaçoes entre classes: associação, agregação e composição
# Composição é uma especialização da agragaçao.
# Mas nela, quando o objeto "pai" for apagado, 
# todas as referência dos objetos filhos também são apagadas
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.endereco = []
        
    
    def inserir_endereco(self,rua, numero):
        self.endereco.append(Endereco(rua, numero))
    
    def listar_enderecos(self):
        for e in self.endereco:
            print(e.rua, e.numero)
        

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua, self.numero)

c1 = Cliente('MAria')
c1.inserir_endereco('Av Brasil', 54)
c1.inserir_endereco('RUA B', 4554)
c1.listar_enderecos()