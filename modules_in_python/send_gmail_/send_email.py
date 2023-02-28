# Enviando E-mails SMTP com python
import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv

os.system('cls')

load_dotenv()

# Caminho arquivo HTML
CAMINHO_HTML = pathlib.Path(__file__).parent / 'test.html'

# Dados remetente
rementente = os.getenv('FROM_EMAIL', '')
destinatario = rementente

# configuração SMTP
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# Mensagem de texto
with open(CAMINHO_HTML, 'r') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome='João')


# transformar nossa mensgame em MIMEmultipart
mime_multipart = MIMEMultipart()
mime_multipart['from'] = rementente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Este é o assunto do email'

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)


# Enviando email
with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(mime_multipart)
    print('E-MAIL enviado com sucesso')
