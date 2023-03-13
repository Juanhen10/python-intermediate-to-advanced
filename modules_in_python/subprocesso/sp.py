# Usando subprocess para executar e comandos externos
# subprocess é ummódulo do Python para executar processos e comandos externos no seu programa.
# O método mais simples para atingir o objetivo é usado subprocess.run().
# Argumentos principais de subprocess.run():
# - stdout, stdin e stder -> Redirecionam saíd, entrada e erros
# - capture_output -> captura a saída e erro para uso posterior
# - text -> Se True, entrada e saídas serão tratadas como
# texto e automaticamnte codificadas ou decodificadas com conjunto de caracteres padrão da plataforma(geralmente UTF-8)
# - shell -> Se True, terá acessoao shell do sistema
#   Ao usar shell (True), recomendo enviar o comando e os argumentos juntos.
# - executabe -> pode ser usado para especificar o caminho do executável que inicará o subprocesso
# Retorno:
# stdout, stderr, returncode e args
# Importante: a codificação dde caracters do Windows pode ser diferente. Tente usar cp1252, cp852, cp850(ou outros).
# Linix e mac, use utf_8.
# Comando de exmplo:
# Windows: ping 127.0.0.1
# Linux/MAc: ping 127.0.0.1 -c 4
import subprocess
import sys

# sys.platform = linux, linux2, darwin, win32
cmd = ['ping', '127.0.0.1']
encoding = 'utg_8'
system = sys.platform

if system == 'win32':
    cmd = ['ping', '127.0.0.1']
    encoding = 'cp850'


proc = subprocess.run(
    cmd, capture_output=True,
    text=True, encoding=encoding
)
print()
# print(proc.args)
# print(proc.stderr)
# print(proc.stdout.decode('cp1252'))
print(proc.stdout)
# print(proc.returncode)
