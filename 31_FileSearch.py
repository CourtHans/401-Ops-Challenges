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
    # count and print number of files searched
    os.system("ls " + str(directory) + " | echo \"Searched $(wc -l) files.\"")
    # count and print number of files found
    os.system("find " + str(directory) + ' -name ' + str(whichFile) + " -print | echo \"Found $(grep -c /) files that matched:\"")
    print("")
    os.system("find " + str(directory) + ' -name ' + str(whichFile))
    print("")

# search a windows os
def windowsSearch():
    whichFile = input("What file are you looking for?  ")
    directory = input("Which directory would you like to search?  ")
    # count number of files searched, store in variable
    searchCount = os.popen("dir /a:-d /s /b " + str(directory) + " | find /c \":\\\"").read()
    print("Files searched: " + searchCount)
    # count number of files found, store in variable
    foundCount = os.popen("dir /b/s " + str(directory) + "\\" + str(whichFile) + " | find /c \":\\\"").read()
    print("Files found: " + foundCount)
    os.system("dir /b/s " + str(directory) + "\\" + str(whichFile))

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