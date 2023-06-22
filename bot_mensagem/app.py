# 1 importar bibliotecas necessarias
import time
from datetime import datetime

import keyboard
import pywhatkit

# 2. Definir para quias contatos iremos enviar as msg
contatos = ['+553311968117826', '+553311986574911']
# 3 definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagens
    pywhatkit.sendwhatmsg_instantly(
        contatos[0], 'Testando o bot')

    del contatos[0]
    time.sleep(10)
    keyboard.press_and_release('ctrl + w')
# 4 testar!
