import os
os.system('cls')
'''
Entendendo os seus próprios módulos Python
O primeiro módulo executado chama-se: __main__
Você pode importar outro módulo inteiro ou parte do módulo
O pythhon conhece a pasta onde o "__main__" está as pastas abaixo dele.
Ele não reconhece pastas e módulos acima do "__main__" por padrão
O python conhce todos os módulos e pacotes prestente nos caminhos de "sys.path" 
-------------------------------------------------------------------------------
Understanding your own Python modules
The first module executed is called: __main__
You can import another whole module or part of the module
pythhon knows the folder where "__main__" is and the folders below it.
It does not recognize folders and modules above "__main__" by default
python knows all modules and packages present in the "sys.path" paths
'''
import sys

from modulation_test import variavel_modulo, soma

print(variavel_modulo)
print(soma(1,2))
# print(*sys.path, sep='\n')