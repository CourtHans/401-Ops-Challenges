#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 2
# Author:                   Courtney Hans
# Date of latest revision:  10/6/20
# Purpose:                  Uptime Sensor Pt 1 of 2

# Import libraries
import datetime, time, os

# Declare variables
ip = input("What address would you like to ping? ")

# Declare functions

# resource: stackoverflow.com/questions/26468640/python-function-to-test-ping
def ping_status():
    response = os.system("ping -c 1 " + ip)
    if response == 0:
        status = " Network is ACTIVE"
    else:
        status = " Network is DOWN"
    return status

status = ping_status()

def run_test():
    while True:
        now = datetime.datetime.now()
        # easy to read date/time format
        timestamp = now.strftime('%m-%d-%Y %H:%M:%S %p')
        print(timestamp + status + " to " + ip)
        time.sleep( 2 )
        f = open ('UptimeSensorfile.txt', 'a')
        f.write(timestamp + status + " to " + ip + "\n")
        f.close

# Main

run_test()

# End