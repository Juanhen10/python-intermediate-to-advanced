import os 
os.system('cls')
# Relaçoes entre classes: associação, agregação e composiçã
# Associação é um tipo de relação onde os objetos estão ligados dentro do sistema
# Essa é a relação mais cumum entre objetos e tem subconjuntos 
# como agregação e composição(que veremos depos).
# Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto
# A associação não especifica como um objeto controla o ciclo de via de outro objeto
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None
        
    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self,ferramenta):
        self._ferramenta = ferramenta


class ferramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome
        
    def escrever(self):
        return f'{self.nome} esta escrevendo'
    
#################################################   


escritor = Escritor('Juan')
caneta = ferramentaDeEscrever('caneta Bic')
maquina_de_escrever = ferramentaDeEscrever('Maquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())
            