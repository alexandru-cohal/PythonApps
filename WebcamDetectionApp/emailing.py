import os
from email.message import EmailMessage
import smtplib
import imghdr

HOST = "smtp.gmail.com"
PORT = 587
SENDER_AND_RECEIVER_EMAIL = os.getenv("EMAIL_AUTOMATION")
PASSWORD_SENDER_EMAIL = os.getenv("PASS_EMAIL_AUTOMATION")

def send_email(image_path):
    email_message = EmailMessage()
    email_message["Subject"] = "A new object / person just appeared!"
    email_message.set_content("A new object / person just appeared! Here it is:")
    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(image_path))

    gmail = smtplib.SMTP(HOST, PORT)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER_AND_RECEIVER_EMAIL, PASSWORD_SENDER_EMAIL)
    gmail.sendmail(SENDER_AND_RECEIVER_EMAIL, SENDER_AND_RECEIVER_EMAIL, email_message.as_string())
    gmail.quit()