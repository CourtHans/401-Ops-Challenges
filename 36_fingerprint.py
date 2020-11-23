#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 36
# Author:                   Courtney Hans
# Date of latest revision:  11/23/20
# Purpose:                  Service fingerprinting attack


# Import libraries

import os, sys, socket, time, telnetlib, signal, subprocess

# Declare variables

addr = input("Enter a URL or IP address:  ")
port = input("Port number:  ")
# addr = "10.0.0.120" #test ip
# port = "22" # test port
# port = int(strPort)

# Declare functions

# os.system("nc " + addr + " " + port)

def netcat(addr, port):
    #creatting a socket and a connection
    socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket1.connect((addr, int(port)))
    print("Netcat...")

    # sending the netcat command
    command = "nc " + addr + " " + port
    socket1.sendall(command.encode())
    time.sleep(.5)
    # closing the socket to more outgoing data
    socket1.shutdown(socket.SHUT_WR)

    # placeholder for response
    output = ""

    # convert the data received
    while True:
        data = socket1.recv(1024)
        if (not data):
            break
        output += data.decode()

    # print output to the terminal
    print(output)
    print("\033[A   \033[A")

    # close the connection
    socket1.close
    # print("Netcat connection closed.")


###########

def telnet(addr, port):
    #creatting a socket and a connection
    socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket2.connect((addr, int(port)))
    print("Telnet...")

    # sending the netcat command
    command2 = "telnet " + addr + " " + port
    socket2.sendall(command2.encode())
    time.sleep(.5)
    # closing the socket to more outgoing data
    socket2.shutdown(socket.SHUT_WR)

    # placeholder for response
    telOutput = ""

    # convert the data received
    while True:
        data = socket2.recv(1024)
        if (not data):
            break
        telOutput += data.decode()

    # print output to the terminal
    print(telOutput)
    print("\033[A   \033[A")

    # close the connection
    socket2.close
    # print("Telnet connection closed.")  

def nmap(addr, port):
    print("Nmap...")
    os.system("nmap -Pn -p " + port + " -sV -script=banner " + addr + " | grep banner")


# Main

netcat(addr,port)
telnet(addr,port)
nmap(addr,port)

# resources: https://www.instructables.com/Netcat-in-Python/
# End