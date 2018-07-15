# I was having some difficulties connecting a Django app to smtp.gmail.com when running example code from tdd-book (see repo).

# This piece of code at this stage is just a hacky-test. Mainly to help diagnose the issue with Django's send_mail functionality. Turns out the built-in doens't do SSL to well. and Gmail prefers SSL over TLS..

# Django's send_mail is just a light wrapper for SMTPLib. This code doesn't require Django, only Python3.6 which has SMTPlib built in

# We're trying to get this working with smtp.gmail.com as of Mid 2018. Of course, their services may change and break this. 

# It might be worth refactoring this into our own little wrapper or a django package later if the code becomes useful. 

# Instructions:
# - First set environment variables EMAIL_HOST_USER and EMAIL_PASSWORD in your OS. eg I'm on Ubuntu, so I use $ export EMAIL_PASSWORD=*insert your password here*
# - This code is for Gmail, you must first set up your gmail account to allow less secure apps - https://support.google.com/accounts/answer/6010255
# - The code below is configured to use SSL, and runs a smtplib.login() first. gmail is happy with this approach. Have not been able to get this working on TLS 
# - Run this with $ python smtp_gmail_emails.py email@emailaddress.com to test this.

import os, sys
import smtplib
from email.message import EmailMessage

EMAIL_HOST = "smtp.gmail.com"
EMAIL_SERVER_PORT = 465          # standard SMTP over SSL port
EMAIL_SERVER_USE_SSL = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_FROM = EMAIL_HOST_USER       
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = sys.argv[1]          # run script - smtp_gmail_email.py *Insert email to send to*

# First set up the email server object
try:
    email_server = smtplib.SMTP_SSL(host=EMAIL_HOST, port=EMAIL_SERVER_PORT)
    print(f'Success! Connected email_server to {EMAIL_HOST}')
except:
    print("  Could not connect to email host")
    exit()

# Then Ehlo as a quick test. Ehlo is short for Extended Helo. It's about communicating to the SMTP server to identify youself - http://www.samlogic.net/articles/smtp-commands-reference.htm
try:
    email_server.ehlo()
    print('Successfully ehlo\'d')
except:
    print("  Could not ehlo")
    exit()

# A login method which exchanges tokens
try: 
    email_server.login(EMAIL_HOST_USER, EMAIL_PASSWORD)
    print(f'Successfully logged in to {EMAIL_HOST}')
except:
    print('  Count not log into email host')


# Set up the email string and send email
try:
    email_content = EmailMessage()
    email_content.set_content("This is the body of the email")
    email_content['Subject'] = "Subject Line"
    email_content['From'] = EMAIL_FROM
    email_content['To'] = TO_EMAIL

    print ("about to send: ")
    print (email_content)

    #email_server.sendmail(EMAIL_FROM, TO_EMAIL, email_content)
    email_server.send_message(email_content)
    print("Successfully sent email message")
except:
    print("  Could not send email message")


# Close the email_server object when you are done with it (log out)
try:
    email_server.close()
    print("Successfully closed email_server")
except:
    print("  Could not closed email_server")
    exit()