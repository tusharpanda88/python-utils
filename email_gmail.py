# Code : Send attachment "capture.jpg" using gmail

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import os

send_user = "YOUR_GMAIL_ID@gmail.com"		#sender_email
send_pwd = "YOUR_GMAIL_PASSWORD"		#sender_password
recv_user = "YOUR_GMAIL_ID@gmail.com"		#receiver_email
subject = "Test Email !!!!"

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = send_user
   msg['To'] = recv_user
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition','attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(send_user, send_pwd)
   mailServer.sendmail(send_user, to, msg.as_string())
   mailServer.close()

mail(recv_user,	subject,"imaeg snapshot !!!","capture.jpg")
