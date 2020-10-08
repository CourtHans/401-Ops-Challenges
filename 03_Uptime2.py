#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 3
# Author:                   Courtney Hans
# Date of latest revision:  10/7/20
# Purpose:                  Uptime Sensor Pt 2 of 2

# Import libraries
import smtplib
import datetime, time, os
from getpass import getpass

# Declare variables

#email = input("Enter your email: ")
email = 'afinch8675309@gmail.com'
ip = '10.0.0.154'
password = getpass()
# reference: https://stackoverflow.com/questions/9202224/getting-command-line-password-input-in-python
up = " Network is ACTIVE"
down = " Network is DOWN"
last = 0
ping_result = 0

# Declare functions


# Send the mail (two options)
def send_upAlert():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    msg1 = "Hello! \nYour system has recovered.\n %s" % timestamp
    server.sendmail('mailbot@myserver.com', email, msg1)
    server.quit()

def send_downAlert():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(email, password)
    msg2 = "Oh dear! \nYour system has gone DOWN.\n %s" % timestamp
    server.sendmail('mailbot@myserver.com', email, msg2)
    server.quit()

# Ping test
def ping():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')

    global ping_result
    global last

    if ((ping_result != last) and (ping_result == up)):
        last = up
        send_upAlert()     
    elif ((ping_result != last) and (ping_result == down)):
        send_downAlert()
        last = down

    response = os.system("ping -c 1 " + ip)
    if response == 0:
        ping_result = up
    else:
        ping_result = down
    print(timestamp + ping_result + " to " + ip)


# Main

while True:
    ping()
    time.sleep( 2 )

# End