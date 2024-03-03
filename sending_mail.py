import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# sender and receiver Address
sender_email = "shitalparate97@gmail.com"
receiver_email = "shitalparate97@gmail.com"
password = "qdmf lcbj psbl sioz"

#  email subject and body
subject = "Email From Python"
body = "This email send from Python. Isn't that cool"

# Setting up mime
msg = MIMEMultipart()
msg ["from"] = sender_email
msg ["To"] = receiver_email
msg ["subject"] = subject

# Attach email body to the msg
msg.attach(MIMEText(body,"plain"))

# login server to secure context and send email
server = smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login(sender_email,password)
text = msg.as_string()
server.sendmail(sender_email,receiver_email,text)
server.quit()

print("email send successfully.")



