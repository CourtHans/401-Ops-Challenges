#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 6
# Author:                   Courtney Hans
# Date of latest revision:  10/12/20
# Purpose:                  Encryption/decryption menu (file or message)

# Import libraries
from cryptography.fernet import Fernet

# Declare variables

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

def ask_user():
    mode = input("\nWhat would you like to do?\
    \nMode 1 - Encrypt a file\
    \nMode 2 - Decrypt a file\
    \nMode 3 - Encrypt a message\
    \nMode 4 - Decrypt a message\
    \n\
    \nPlease enter a number: ")
    if (mode== "1"):
        encrypt_file()
        print("...file encrypted.")
    elif (mode == "2"):
        decrypt_file()
        print("...file decrypted.")
    elif (mode == "3"):
        encrypt_message()
    elif (mode == "4"):
        decrypt_message()
    else:
        print("Invalid selection...")


# Main

while True:
    ask_user()
    y_n = input ("Try again? y/n ")
    if y_n == "n":
        print("Have a nice day!")
        break

# resource: https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
# resource: https://stackoverflow.com/questions/22362165/i-want-to-have-a-yes-no-loop-in-my-code-but-im-having-trouble-doing-it-python
# End