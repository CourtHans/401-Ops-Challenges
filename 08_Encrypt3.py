#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 8
# Author:                   Courtney Hans
# Date of latest revision:  10/14/20
# Purpose:                  

#import pdb; pdb.set_trace()

# Import libraries

from cryptography.fernet import Fernet
import os, math, time, datetime, getpass, os.path
import urllib.request
import ctypes
import pyautogui
import win32ui
import win32con


# Declare variables
dir_count = 0
file_count = 0
user_name = os.path.expanduser("~")
ab_path = f"{user_name}/OneDrive/Desktop/"


# Declare functions
def change_desktop_background():
    global ab_path
    imageUrl = 'https://www.wweek.com/resizer/86tt-U3ytIrtb7bBYXAIg7XWz7A=/1200x0/filters:quality(100)/s3.amazonaws.com/arc-wordpress-client-uploads/wweek/wp-content/uploads/2019/08/30145212/Nicolas-Cage.jpg'
    # Go to specif url and download+save image using absolute path
    path = f'{ab_path}malware_pic.jpg'
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    # Access windows dlls for funcionality eg, changing dekstop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

def restore_background():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, 'C:\Windows\Web\Wallpaper\Windows\img0.jpg', 0)




# Main

#change_desktop_background()
#restore_background()



# resource: geeksforgeeks.org/python-os-path-expanduser-method/
# HUGE thanks to Jin Kim https://github.com/jinwoov
# End