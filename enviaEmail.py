import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def enviaEmail():
    
    with open("files/new.txt", "r") as file:
        arquivo = file.read()

    if arquivo == "":

        print("Não ha links Novos")

        file = r'files/new.txt'
        os.remove(file)

    else:

        # Configuração
        host = 'smtp.gmail.com'
        port = 587
        user = 'gustavoacm06@gmail.com'
        password = 'itnrqkeqikawpkiv'

        # Criando objeto
        print('Criando objeto servidor...')
        server = smtplib.SMTP(host, port)

        # Login com servidor
        print('Login...')
        server.ehlo()
        server.starttls()
        server.login(user, password)

        # Criando mensagem
        with open("files/new.txt", "r") as file:
            message = "Segue os links atualizados \n " + file.read()

        print('Criando mensagem...')
        email_msg = MIMEMultipart()
        email_msg['From'] = user
        email_msg['To'] = 'Gustavoacm06@gmail.com'
        #email_msg['To'] = 'Valdemir_bezerra@yahoo.com.br'
        email_msg['Subject'] = 'Novos Posts'
        print('Adicionando texto...')
        email_msg.attach(MIMEText(message, 'plain'))

        # Enviando mensagem
        print('Enviando mensagem...')
        server.sendmail(email_msg['From'],
                        email_msg['To'], email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()

        file = r'files/new.txt'
        os.remove(file)
        