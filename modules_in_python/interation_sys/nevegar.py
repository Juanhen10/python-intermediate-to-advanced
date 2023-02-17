# os.listdir par anevegar em caminhos
# C:\Users\Juan Henrique\Desktop\Nova pasta
import os

os.system('cls')


caminho = os.path.join('\\Users', 'Juan Henrique', 'Desktop', 'Nova pasta')


for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    for item in os.listdir(caminho_completo_pasta):
        print(' ', item)
