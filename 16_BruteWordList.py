#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 16
# Author:                   Courtney Hans
# Date of latest revision:  10/26/20
# Purpose:                  Automated Brute Force Wordlist Attack Tool (1 of 3)

# Import libraries
import time, getpass

# Declare variables

# Declare functions

def iterator ():
    filepath = input("Enter your dictionary filepath:\n")
    #filepath = '/home/osboxes/Desktop/rockyou2.txt' #test filepath
    
    file = open(filepath)
    line = file.readline()
    while line:
        line = line.rstrip()
        word = line
        print(word)
        time.sleep(1)
        line = file.readline()
    file.close()


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
1 - Offensive, Dictionary Iterator
2 - Defensive, Password Recognized
3 - Exit
    Please enter a number: 
""")
        if (mode == "1"):
            iterator()
        elif (mode == "2"):
            check_password()
        elif (mode == '3'):
            break
        else:
            print("Invalid selection...") 


# resource: https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/Python_FileText.html
# resource: https://stackoverflow.com/questions/16709638/checking-the-strength-of-a-password-how-to-check-conditions
# resource: https://pypi.org/project/password-strength/
# resource: https://stackoverflow.com/questions/19699367/for-line-in-results-in-unicodedecodeerror-utf-8-codec-cant-decode-byte

# End