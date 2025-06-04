# send_email.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# 🔧 CONFIGURE AQUI
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
USERNAME = "seuemail@gmail.com"
PASSWORD = "sua_senha_de_app"  # ou senha normal (menos seguro)

TO_EMAIL = "destinatario@gmail.com"
TRACKING_ID = "teste123"  # esse mesmo ID aparecerá no JSON

# Corpo do e-mail em HTML com pixel
html = f"""
<html>
  <body>
    <h2>Olá!</h2>
    <p>Este é um e-mail com rastreamento de abertura.</p>
    <img src="http://127.0.0.1:8000/track/{TRACKING_ID}.png" width="1" height="1" alt="">
  </body>
</html>
"""

# Cria a mensagem
msg = MIMEMultipart("alternative")
msg["Subject"] = "Teste com rastreamento"
msg["From"] = USERNAME
msg["To"] = TO_EMAIL

part = MIMEText(html, "html")
msg.attach(part)

# Envia o e-mail via SMTP
with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(USERNAME, TO_EMAIL, msg.as_string())

print("📨 E-mail enviado com sucesso!")
