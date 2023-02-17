# os + shutil - MOver, copiar e apagar arquivos
# MOver / Renomear - > shurtil.move
# MOver/ renomear -> os.rename
# Copiar - > shutil.copy
# Apgar - > os.unlink
# Apgar diretório recursivamente - > rmtree
import os
import shutil

os.system('cls')

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'Nova pasta')
NOVA_PASTA = os.path.join(DESKTOP, 'PASTA')

shutil.rmtree(NOVA_PASTA, ignore_errors= True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)

# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)

#     for file in files:
#         caminho_original = os.path.join(root, file)
#         caminho_novo = os.path.join(
#             root.replace(PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_original, caminho_novo)
