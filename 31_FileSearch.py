#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 31
# Author:                   Courtney Hans
# Date of latest revision:  11/16/20
# Purpose:                  File Searcher for Windows and Linux


# Import libraries
from sys import platform
import os, time


# Declare functions

# search a linux os
def linuxSearch():
    whichFile = input("What file are you looking for?  ")
    directory = input("Which directory would you like to search?  ")
    print("Here's what I found: \n")
    os.system("find " + str(directory) + ' -name ' + str(whichFile))
    print("")

# search a windows os
def windowsSearch():
    whichFile = input("What file are you looking for?  ")
    answer = input("Are you in the directory you wish to search? Enter y or n:  ").lower()
    if answer == "y":
        print("Here's what I found: \n")
        os.system("dir /b/s " + str(whichFile))
    elif answer == "n":
        print("Okay, just a moment...")
        os.system("dir \"\\" + str(whichFile) + "\" /s")
    else:
        print("I'm sorry, that was not a valid input. You'll have to run the script again.")

# Main

# determine OS and run appropriate function
if platform == "linux" or platform == "linux2":
    print("This is a Linux machine!")
    linuxSearch()
elif platform == "win32":
    print("This is a Windows machine!")
    windowsSearch()

# resource: https://stackoverflow.com/questions/8220108/how-do-i-check-the-operating-system-in-python/8220141

# End