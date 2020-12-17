import smtplib
import secret
def send(message):
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()
    server.login(secret.email, secret.password)
    server.sendmail( secret.recipent, secret.email, message)
    print('Send E-Mail')