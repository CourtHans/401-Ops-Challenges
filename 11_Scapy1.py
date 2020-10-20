#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 11
# Author:                   Courtney Hans
# Date of latest revision:  10/19/20
# Purpose:                  Scapy scanning tool (1 of 3)

# Import libraries

from scapy.all import ICMP, IP, sr1, TCP, sr
import random

# Declare variables
host = "scanme.nmap.org" # definining host IP
port_range = [21, 22, 23] # providing a port range

# Declare functions

# Main
for dst_port in port_range: # for each port in defined range...
    src_port = random.randint(1025,65534) # randomize TCP source port
    port_num = str(dst_port)
    response = sr1(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,verbose=0)

    if response is None:
        print ("Port " + port_num + ": The packet was filtered.")
        print (response)
    elif response.haslayer(TCP):
        if response.getlayer(TCP).flags == 0x12: #Port responding and open
            print("Port " + port_num + ": The port is OPEN and responding.")
            # send RST packet to graciously close connection
            send_rst = sr(IP(dst=host)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)
            print(response)
        if response.getlayer(TCP).flags == 0x14: #Port closed
            print("Port " + port_num + ": The port is CLOSED.")
            print(response)
     

# resource: https://resources.infosecinstitute.com/port-scanning-using-scapy/
# resource: https://stackoverflow.com/questions/20429674/get-tcp-flags-with-scapy
# End