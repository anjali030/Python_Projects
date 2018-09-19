#!/usr/bin/env python
# coding: utf-8
#import getpass
#password=getpass.getpass('enter your password ')
#print(password)
import os
import smtplib #simple mail transfer protocol
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import getpass
#multipurpose Internet mail extension
ImageFileName="D:\\4.jpg"
img_data=open(ImageFileName, 'rb').read()
msg=MIMEMultipart()
msg['FROM']='anjalimittal097@gmail.com'
password=getpass.getpass('Enter your password')
msg['To']='akanshamaheshawari911@gmail.com'
msg['Subject']='My Mail'
body='''Image attachment text email succesfull.
This program is written in python
I used SMTP,OS and getpass module'''
text=MIMEText(body)
msg.attach(text)
image=MIMEImage(img_data,name=os.path.basename(ImageFileName))
msg.attach(image)
s=smtplib.SMTP('smtp.gmail.com',587)
s.ehlo()
s.starttls()
s.login(msg['From'],password)
s.sendmail(msg['From'],msg['To'],msg.as_string())
s.quit()
print('Email Sent Successfully')


