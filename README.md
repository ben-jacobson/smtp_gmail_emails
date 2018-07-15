I was having some difficulties connecting a Django app to smtp.gmail.com when running example code from tdd-book (see repo).

This piece of code at this stage is just a hacky-test. Mainly to help diagnose the issue with Django's send_mail functionality. Turns out the built-in doens't do SSL to well. and Gmail prefers SSL over TLS..

Django's send_mail is just a light wrapper for SMTPLib. This code doesn't require Django, only Python3.6 which has SMTPlib built in

We're trying to get this working with smtp.gmail.com as of Mid 2018. Of course, their services may change and break this.

It might be worth refactoring this into our own little wrapper or a django package later if the code becomes useful.

Instructions:

    First set environment variables EMAIL_HOST_USER and EMAIL_PASSWORD in your OS. eg I'm on Ubuntu, so I use $ export EMAIL_PASSWORD=insert your password here
    This code is for Gmail, you must first set up your gmail account to allow less secure apps - https://support.google.com/accounts/answer/6010255
    The code below is configured to use SSL, and runs a smtplib.login() first. gmail is happy with this approach. Have not been able to get this working on TLS
    Run this with $ python smtp_gmail_emails.py email@emailaddress.com to test this.


