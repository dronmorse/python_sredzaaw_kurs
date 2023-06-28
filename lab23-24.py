#!/usr/bin/env python3

import smtplib

mailFrom = "Your Automation System"
mailTo = ['dronmorse@gmail.com']
mailSubject = 'Hello bud'
mailBody = 'This is my first automated email'

message = '''From = {}
Subject = {}

{}
'''.format(mailFrom, mailSubject, mailBody)

user = "dronmorse@gmail.com"
password = "Dronmorse20*"

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user, mailTo, message)
    server.close()
    print('mail sent')
except:
    print('error sending email')
