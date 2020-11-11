#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 27
# Author:                   Courtney Hans
# Date of latest revision:  11/10/20
# Purpose:                  Adding log rotation capabilities


# Import libraries

import logging, time, os
from logging.handlers import RotatingFileHandler

# Declare variables

user_input = input("Type in the name of a directory located in the home folder:")

# Declare functions

def file_crawler(user_input):
    for (root, dirs, files) in os.walk("/home/osboxes/" + user_input):
        print("==root==")
        print(root)
        print("==dirs==")
        print(dirs)
        print("==files")
        print(files)

# Main

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('my_log', maxBytes=500, backupCount=3) 
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
print('Logging started')


for i in range(200): 
    logmsg = "Warning Message "
    logmsg += str(i)
    logger.warning(logmsg)
    logger.info('This is purely informational, script is running.')
    logger.critical('Critical issue!')
    logger.error('An error has occured...')

try:
    file_crawler() ##intentional error (left out parameter)

except Exception as msg:
   logger.error(msg)
   print("Something went wrong!")

print('Logging completed')

# End