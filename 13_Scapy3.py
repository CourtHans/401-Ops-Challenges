#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 13
# Author:                   Courtney Hans
# Date of latest revision:  10/21/20
# Purpose:                  Scapy scanning tool
#                           ARP the network, scan open hosts for determined ports


# Import libraries
import random
import ipaddress
from scapy.all import ICMP, IP, sr1, TCP, sr
import scapy.all as scapy

# Declare variables
network = input("What network would you like to scan?\n")

# Declare functions

# user input to create a port number list
def port_num():
    port_range = []
    n = int(input("How many ports do you wish to scan?\n"))
    print(f"Which ports? Separated each of your {n} entries with a return:")
    for i in range(0,n):
        ports = int(input())
        port_range.append(ports)
    print("Beginning scan...................")
    return port_range

# TCP port scan
def tcp_port_scan(host, port_range):
    #port_range = [22, 23, 80, 443, 3389] # can provide port range if you don't want user input
    not_open = 0
    for dst_port in port_range: # for each port in defined range...
        src_port = random.randint(1025,65534) # randomize TCP source port
        port_num = str(dst_port)
        response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)
        if response is None:
            not_open+=1
        elif response is not None:
            if response.getlayer(TCP).flags == 0x12: #Port responding and open
                print("Port " + port_num + ": The port is OPEN and responding.")
                # send RST packet to graciously close connection
                send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=2, verbose=0)
            if response.getlayer(TCP).flags == 0x14: #Port closed
                not_open+=1
    if not_open != 1:
        print(f"\n{not_open} of your selected ports are either closed or unresponsive.")
    else:
        print("\nOne of your selected ports is either closed or uresponsive.")


# ARP scan   
def arp_scan(network):
    port_range = port_num()
    request = scapy.ARP()
    request.pdst = network
    broadcast = scapy.Ether()
    broadcast.dst = 'ff:ff:ff:ff:ff:ff'
    request_broadcast = broadcast / request
    answered_clients = scapy.srp(request_broadcast, timeout = 1, verbose=0)[0]
    clients_list = []
    scanned = 0
    for element in answered_clients:
        scan_client = element[1].psrc
        host = scan_client
        print("\n" + element[1].psrc + "      " + element[1].hwsrc)
        print(f"Scanning port(s) {str(port_range).strip('[]')}......")
        tcp_port_scan(host, port_range)
        scanned+=1
    print(f"\n{scanned} hosts scanned for port(s) {str(port_range).strip('[]')}.")

# Main
arp_scan(network)


# resource: https://www.programcreek.com/python/example/103593/scapy.all.srp
# End