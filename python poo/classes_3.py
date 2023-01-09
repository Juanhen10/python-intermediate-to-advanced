import os
os.system('cls')
class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} Já está filmando...')
        print(f'{self.nome} está filmando...')
        self.filmando = True
    
    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} parou de filmar...')
            return

        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
        
        
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar esta filmando...')
            return
        
        print(f'{self.nome} está fotografando')
        self.filmando = False

c1 = Camera('Canon')
c2 = Camera('Sony')
c1.filmar()
c1.parar_filmar()
c1.fotografar()
c1.filmar()
print()
c2.fotografar()
c2.filmar()
c2.parar_filmar()
c2.filmar()
c2.fotografar()



