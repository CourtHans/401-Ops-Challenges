#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 26
# Author:                   Courtney Hans
# Date of latest revision:  11/9/20
# Purpose:                  Add a log handler to existing code


# Import libraries

import logging
import os

# Declare variables
user_input = input("Type in the name of a directory located in the home folder:")

# Declare functions

def verification(user_input):
    # Check whether the specified path is an existing file  
    isFile = os.path.isfile(user_input)
    if isFile is False:
        print("Directory not found.")
    else: 
        file_crawler(user_input)

def file_crawler(dir_name):
    for (root, dirs, files) in os.walk("/home/osboxes/" + dir_name):
        ### Add a print command here to print ==root==
        print("==root==")
        print(root)
        ### Add a print command here to print ==dirs==
        print("==dirs==")
        print(dirs)
        ### Add a print command here to print ==files==
        print("==files")
        print(files)

# Main

logging.basicConfig(filename='/home/osboxes/test_log.txt', level=logging.ERROR, format='%(asctime)s:%(levelname)s:%(message)s')
print('Logging started')
logging.debug('Something to debug...')
logging.info('This is purely informational')
logging.warning('Warning! Warning!')
# logging.error('An error has occured...')
logging.critical('There is a critical issue here')

try:
    verification() ##intentional error

except Exception as msg:
   print(msg)
   logging.exception(msg)

print('Logging completed')
# End