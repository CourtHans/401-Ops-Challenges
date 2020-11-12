!/usr/bin/env python3

# import libraries
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
import os
import sys
import ssl
import smtplib
from smtplib import SMTP

#####

def trigger_email():
    EmailAddress = 'afinch8675309@gmail.com'
    EmailPassword = 'codefellow'

    # EmailAddress = 'cyops123@gmail.com'
    # EmailPassword = 'Codefellow!'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

        smtp.login(EmailAddress, EmailPassword)
        subject = 'Network Notification'
        body = 'There has been detection of file modification or movement!'

        msg = 'Subject: ' + subject + '\n\n' + body

        smtp.sendmail(EmailAddress, 'afinch8675309@gmail.com' , msg)

def alert(event):
    trigger_email()

#####


# creating monitoring data and time stamps
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    
    # choosing the path of the directory to observe                     
    path = "/home/kali/Desktop"
    #path = "C:/Users/IEUser/Desktop"

    # creating log for the events
    event_handler = LoggingEventHandler()
    event_handler.on_any_event = alert

    # initiallizing the observer function
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # starting the observer function
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

    # Developed in conjunction with Domonic Moore
    # resource: http://brunorocha.org/python/watching-a-directory-for-file-changes-with-python.html