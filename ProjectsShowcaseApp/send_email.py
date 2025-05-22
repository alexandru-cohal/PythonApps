import smtplib
import ssl
import os

HOST = "smtp.gmail.com"
PORT = 465
SENDER_AND_RECEIVER_EMAIL = os.getenv("EMAIL_AUTOMATION")
PASSWORD_SENDER_EMAIL = os.getenv("PASS_EMAIL_AUTOMATION")

def send_email(message):
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
        server.login(SENDER_AND_RECEIVER_EMAIL, PASSWORD_SENDER_EMAIL)
        server.sendmail(SENDER_AND_RECEIVER_EMAIL, SENDER_AND_RECEIVER_EMAIL, message)