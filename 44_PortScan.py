#!/usr/bin/python3

# Script:                   401 Op Challenge Day 44
# Author:                   Courtney Hans
# Date of latest revision:  12/7/20
# Purpose:                  Port scanning   

# Import Libraries
import socket

# Define variables

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = 30 
sockmod.settimeout(timeout)

hostip = input("Enter host IP you wish to scan:  ")
portno = input ("Please enter specific port to scan:  ")
portno = int(portno)

# Define functions

def portScanner(hostip, portno):
    result = sockmod.connect_ex((hostip, portno))
    if result ==0: # TODO: Replace "FUNCTION" with the appropriate socket.function call as found in the [socket docs](https://docs.python.org/3/library/socket.html)
        print("Port is OPEN")
    else:
        print("Port CLOSED")

# Main

portScanner(hostip,portno)

#resource: https://www.kite.com/python/answers/how-to-check-if-a-network-port-is-open-in-python#:~:text=To%20check%20if%20a%20network%20port%20is%20open%2C%20call%20socket,connect_ex()%20returns%200%20
# End