# Variáveis de ambiente com Python
# Para variáveis de ambiente
# Windows PS: $env: VARIAVEL = "VALOR" | dir env:
# Linux e Mac: export NOME_VARIAVEL= "VALOR" | echo $VARIAVEL
# PAra obter o valor das variáveis de ambiente
# os.getenv ou os.environ['VARIAVEL']
# Para configurar variáveis de ambiente
# os.eviron['VARIAVEl'] = 'Valor'
# Ou usando python-dotenv
# from dotenv import load_dotenv
# load_dotenv()
# OBS.: sempre lembre-se de criar um .env-exanple
import os

from dotenv import load_dotenv

load_dotenv()

# print(os.environ)
print(os.getenv('BD_PASSWORD'))
