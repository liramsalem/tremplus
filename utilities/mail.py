import smtplib, ssl
from email.message import EmailMessage

def sendEmail(fName,lName,email,body):
    msg = EmailMessage()
    msg.set_content(f" שלום {fName} {lName} , \n\n {body} ")
    msg["Subject"] = "Tremplus"
    msg["From"] = "tremplus6@gmail.com"
    msg["To"] = email

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com", port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], "ffpfspjjkqkistii")
        smtp.send_message(msg)
    print(f"one message send to {fName} {lName}")


