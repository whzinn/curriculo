import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Configurações do servidor SMTP
smtp_server = 'smtp-relay.brevo.com'
smtp_port = 587  # Substitua pela porta SMTP apropriada

smtp_username = 'xmalesant@gmail.com'

smtp_password = 'qnvhWOfLJYm8zydg'   


# Configuração da mensagem de email
from_email = 'xmalesant@gmail.com'

to_email = 'bwmbybr@gmail.com'
subject = 'Documento Importante'

# Crie uma instância do objeto MIMEMultipart
msg = MIMEMultipart()

msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = subject

# Adicione o corpo do email


def send(uid):
    body = 'Documentação abaixo.'
    msg.attach(MIMEText(body, 'plain'))

    # Anexe uma imagem
    with open("geral/"+uid+'selfie.jpg', 'rb') as img_file:
        image1 = MIMEImage(img_file.read(), name='selfie.png')
    
    with open("geral/"+uid+'verso.jpg', 'rb') as img_file:
        image2 = MIMEImage(img_file.read(), name='verso.png')

    with open("geral/"+uid+'frente.jpg', 'rb') as img_file:
        image3 = MIMEImage(img_file.read(), name='frente.png')
    msg.attach(image1)
    msg.attach(image2)
    msg.attach(image3)

    # Conecte-se ao servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Use SSL/TLS para criptografar a conexão (pode variar conforme o servidor)

    # Faça login na conta
    server.login(smtp_username, smtp_password)

    # Envie o email
    server.sendmail(from_email, to_email, msg.as_string())

    # Encerre a conexão
    server.quit()
