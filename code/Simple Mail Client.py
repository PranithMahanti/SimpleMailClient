import smtplib
import ssl

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "pranithmahanti@gmail.com"
receiver_email = "pranithmahanti@gmail.com"

with open("passwd.pd", "r") as file:
    password = file.read()

message = "Hello"

context = ssl.create_default_context()

try:
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_email, message)
    print("Mail has been sent...")

except Exception as e:
    print(e)
