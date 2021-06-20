import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "pranithmahanti@gmail.com"
receiver_email = "pranithmahanti@gmail.com"

with open("passwd.pd", "r") as file:
    password = file.read()

message = MIMEMultipart()
message["Subject"] = "SECRET TEST"
message["From"] = sender_email
message["To"] = receiver_email

context = ssl.create_default_context()

msg = """
    Hello!! This is a plain text message!!
"""

message.attach(MIMEText(msg, 'plain'))

msg = """
    <html>
    <body>
        <p>Hi,<br>
            How are you?<br>
            <a href="https://www.youtube.com/channel/UCiPBjHukuEFSwVdsA1KQy8A">My Channel</a> 
            has many great tutorials.
        </p>
    </body>
    </html>
"""
message.attach(MIMEText(msg, 'html'))

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message.as_string())
    print("Mail has been sent...")

except Exception as e:
    print(e)
