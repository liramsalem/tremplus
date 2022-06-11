import smtplib, ssl
from email.message import EmailMessage

def sendEmail(fName,lName,email,body):
    msg = EmailMessage()
    msg.set_content(f" שלום {fName} {lName} , \n\n {body} ")
    msg["Subject"] = "Tremplus"
    msg["From"] = "tremplus@outlook.com"
    msg["To"] = email

    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.outlook.com", port=587) as smtp:
        smtp.starttls(context=context)
        smtp.login(msg["From"], "Tt123456789")
        smtp.send_message(msg)
    print(f"one message send to {fName} {lName}")

#
# def send(fName, lName, email, body):
#     msg = EmailMessage()
#     msg.set_content(f" שלום {fName} {lName} , \n\n {body} ")
#     msg["Subject"] = "Tremplus"
#     msg["From"] = "tremplus12@mail.com"
#     msg["To"] = email
#
#     context = ssl.create_default_context()
#
#     with smtplib.SMTP("smtp.mail.com", port=587) as smtp:
#         smtp.starttls(context=context)
#         print("k")
#         smtp.login("tremplus12@mail.com", "SUCZB76PPJQCE4ADMQ2K")
#         print("lir")
#         smtp.send_message(msg)
#     print(f"one message send to {fName} {lName}")
#     send('fName', 'lName', 'liramsalem@gmail.com', "ffffff");

# def send(fName, lName, email, body):
#     msg = EmailMessage()
#     msg.set_content(f" שלום {fName} {lName} , \n\n {body} ")
#     msg["Subject"] = "Tremplus"
#     msg["From"] = "tremplus@walla.co.il"
#     msg["To"] = email
#
#     context = ssl.create_default_context()
#
#     with smtplib.SMTP("out.walla.co.il", port=587) as smtp:
#         smtp.starttls(context=context)
#         smtp.login(msg["From"], "Tremp12345678")
#         smtp.send_message(msg)
#     print(f"one message send to {fName} {lName}")

