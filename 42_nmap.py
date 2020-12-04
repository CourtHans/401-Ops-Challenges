#!/usr/bin/python3

# Script:                   401 Op Challenge Day 42
# Author:                   Courtney Hans
# Date of latest revision:  12/3/20
# Purpose:                  nmap scanning   

# Import Libraries
import nmap

# Define variables
scanner = nmap.PortScanner()

# Define functions

def syn_ack():
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_addr].state())
    print("protocols: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

def udp_scan():
    print("Nmap Version: ",scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("IP status: ", scanner[ip_addr].state())
    print("protocols: ", scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())

def os_system():
    print("Nmap Version: ",scanner.nmap_version())
    print(scanner.scan(ip_addr, arguments='-O')['scan'][ip_addr]['osmatch'][0])

### Menu of options ###
def menu():
    resp = input("""\nSelect scan to execute (enter number):
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Operating System\n""")
    print("You have selected option: ", resp)

    if (resp == "1"):
        syn_ack()
    elif (resp == "2"):
        udp_scan()
    elif (resp== "3"):
        os_system()
    else:
        print("Invalid selection...")

# Main
print("--------------------")
print("Nmap Automation Tool")
print("--------------------")
ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)
range = input("Enter port range (e.g. 1-50): ")

while True:
    menu()
    y_n = input ("Try again? y/n ")
    if y_n == "n":
        print("Have a nice day!")
        break