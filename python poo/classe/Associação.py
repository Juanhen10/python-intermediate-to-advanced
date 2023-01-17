import os
os.system('cls')
# Relações entre classes: associação, agregação e composição 
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objetp terá seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.
# Os objetos podem viver sepradamente, 
# mas pode se tratar de uam relaçao onde um objeto precidade de outro para fazer determianda tarefa.
#(existem controvérsias sobre as definilçoes de agregação).
class Carrinho:
    def __init__(self):
        self._produtos = []
    
    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def inserit_produtos(self, *produtos):
        # self._produtos.extend(produtos)
        # self._produtos += produtos
        for produto in produtos:
            self._produtos.append(produto)
    
    def listar_profutos(self):
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
carrinho = Carrinho()
p1, p2 = Produto('Caneta', 1.20), Produto('camiseta', 125)
carrinho.inserit_produtos(p1,p2)
carrinho.listar_profutos()
print(carrinho.total())