#!/usr/bin/python3

# Script:                   401 Op Challenge Day 44
# Author:                   Courtney Hans
# Date of latest revision:  12/7/20
# Purpose:                  Port scanning   

# Import Libraries
import socket

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 30 
sockmod.settimeout(timeout)

hostip = input("Enter host IP you wish to scan:  ")
portno = input ("Please enter specific port to scan:  ")
portno = int(portno)
def portScanner(hostip, portno):
    result = sockmod.connect_ex((hostip, portno))
    if result ==0: # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port is OPEN")
    else:
        print("Port CLOSED")

portScanner(hostip,portno)

# End