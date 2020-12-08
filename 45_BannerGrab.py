#!/usr/bin/python3

# Script:                   401 Op Challenge Day 45
# Author:                   Courtney Hans
# Date of latest revision:  12/8/20
# Purpose:                  Enumeration tool 

# Import Libraries
import nmap, socket

# Define variables

scanner = nmap.PortScanner()

# Define functions

# nmap 'stealth' TCP SYN scan
def syn_ack():
    range = input("Enter port range (e.g. 1-50): ")
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(host, range, '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[host].state())
    print("protocols: ", scanner[host].all_protocols())
    print("Open Ports: ", scanner[host]['tcp'].keys())

# namp UDP scan
def udp_scan():
    range = input("Enter port range (e.g. 1-50): ")
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(host, range, '-v -sU')
    print(scanner.scaninfo())
    print("IP status: ", scanner[host].state())
    print("protocols: ", scanner[host].all_protocols())
    print("Open Ports: ", scanner[host]['udp'].keys())

# nmap OS scan
def os_system():
    print("Nmap Version: ",scanner.nmap_version())
    print(scanner.scan(host, arguments='-O')['scan'][host]['osmatch'][0])

# Is specific port up or down?
def portScanner(host):
    port = input("Please specify port:  ")
    port = int(port)
    sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = 30 
    sockmod.settimeout(timeout)
    result = sockmod.connect_ex((host, port))
    if result ==0:
        print("Port is OPEN")
    else:
        print("Port CLOSED")

# Grab banner for specific port
def bannergrab(host):
    port = input("Please specify port:  ")
    port = int(port)
    sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    timeout = 30 
    sockmod.settimeout(timeout)
    sockmod.connect((host,port))
    print(sockmod.recv(1024))
    sockmod.close()

### Menu of options ###
def menu():
    resp = input("""\nSelect scan to execute (enter number):
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Operating System
                    4) Port Scanner
                    5) Banner Grabber\n""")
    print("You have selected option: ", resp)

    if (resp == "1"):
        syn_ack()
    elif (resp == "2"):
        udp_scan()
    elif (resp== "3"):
        os_system()
    elif (resp== "4"):
        portScanner(host)
    elif (resp== "5"):
        bannergrab(host)
    else:
        print("Invalid selection...")

# Main

print("--------------------")
print("Enumeration Station")
print("--------------------")
host = input("IP address to scan: ")
type(host)

# Loop through menu of options until user decides to quit
while True:
    menu()
    y_n = input ("Try again? y/n ")
    if y_n == "n":
        print("Have a nice day!")
        break

# End