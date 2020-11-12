#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 28
# Author:                   Courtney Hans
# Date of latest revision:  11/11/20
# Purpose:                  Adding finesse to my log (and emailing the log file)


# Import libraries

import logging, time, os, sys, ssl, smtplib
from smtplib import SMTP
from logging.handlers import RotatingFileHandler
from logging.handlers import SMTPHandler

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from getpass import getpass

# Declare variables
auth_email = input("To enable email, please enter authenticator email: ")
password = getpass(prompt="Password: ")
dest_email = input("Please DESTINATION email:  ")

user_input = input("Type in the name of a directory located in the home folder:")

# Declare functions

def file_crawler(user_input):
   for (root, dirs, files) in os.walk("/home/osboxes/" + user_input):
        print("==root==")
        print(root)
        print("==dirs==")
        print(dirs)
        print("==files")
        print(files)

###### Function to email log file as an attachment ########
def email_logfile():
    subject = "Log file transmission"
    body = "Logging activity is in the attached file."
    # sender_email = could enter here
    # receiver_email = could enter here
    # password = getpass(prompt="Password:  ")
    print('Emailing log file......')

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = auth_email
    message["To"] = dest_email
    message["Subject"] = subject
    # message["Bcc"] = receiver_email  # Recommended for mass emails

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "infoLog"  # In working directory

    # Open file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(auth_email, password)
        server.sendmail(auth_email, dest_email, text)
    
    print("Log file emailed.")

# Main

logger = logging.getLogger(__name__)

# Creating handlers
w_handler = logging.FileHandler('infoLog') #will appear in working directory
e_handler = logging.StreamHandler()
w_handler.setLevel(logging.WARNING)
e_handler.setLevel(logging.ERROR)

# Creating formatters and adding them to handlers respectively
w_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
e_format = logging.Formatter('%(levelname)s:%(message)s')
w_handler.setFormatter(w_format)
e_handler.setFormatter(e_format)

# SMTPHandler
email_handler = SMTPHandler(
    mailhost=('smtp.gmail.com', 587), # had to chanage to 587
    fromaddr=auth_email,
    toaddrs=dest_email,
    subject='Script Error!',
    credentials=(auth_email, password),
    secure=())

email_handler.setLevel(logging.ERROR)

# adding handlers to the logger
logger.addHandler(email_handler)
logger.addHandler(w_handler)
logger.addHandler(e_handler)

print('Logging started...\n')
time.sleep(.5)

try:
    file_crawler() ## can force intentional error if leave out parameter

except Exception as msg:
   logger.error(msg)
   print("Something went wrong!")

print("\nAny error messages were emailed; all warning AND error messages were logged into a file named infoLog.")
logger.warning("Generic warning message.")
# logger.error("Generic error message.")

print('\nScript completed.')

try:
    email_logfile()
    print("Script complete")

except KeyboardInterrupt: #graceful exit message if user hits CTRL C
    print('\n[*] User requested an interupt, no email sent [*]')
    sys.exit()


# resource: https://realpython.com/python-send-email/
# resource: http://mynthon.net/howto/-/python/python%20-%20logging.SMTPHandler-how-to-use-gmail-smtp-server.txt
# resource: https://www.programcreek.com/python/example/5045/logging.handlers.SMTPHandler
# End