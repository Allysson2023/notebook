import os
from dotenv import load_dotenv
import pathlib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

load_dotenv()
# Caminho do arquivo

CAMINHO_HTML = pathlib.Path(__file__).parent / 'pages/email.html' 

# Dados do remetente e destinatarios



remetente = os.getenv('FROM_EMAIL', '')
destinatario = remetente

# Conf SMTP

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_usermane = os.getenv('FROM_EMAIL', '')
smtp_password = os.getenv('EMAIL_PASSWORD', '')

# messagem de text

with open(CAMINHO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    text_email = template.substitute(nome= 'Allysson')



# Transforma minemultipart


mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = 'Esse é o assunto sobre os e-mail'

# Adiciona o corpo do email
copo_email = MIMEText(text_email, 'html', 'utf-8')
mime_multipart.attach(copo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_usermane, smtp_password)
    server.send_message(mime_multipart)
    print('E-mail enviado com sucesso!')