# Módulos padrão do Python (import, rrom)
# Inteiro - import <name_modulo>
import os
os.system('cls')

#partes - from <name_modulo> import <objeto1, objeto2>
from os import system
system('cls')

#alias 1 - import <name> as apelido
#alias 2 - from <name> import <obj> as apelido
import os as limpar
limpar.system('cls')

from time import sleep as lento
lento(0.1)