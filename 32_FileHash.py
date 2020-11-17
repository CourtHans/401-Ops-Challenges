#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 32
# Author:                   Courtney Hans
# Date of latest revision:  11/17/20
# Purpose:                  File Hasher for Windows and Linux


# Import libraries
from sys import platform
import os, time, datetime, math
import hashlib

# Declare functions

# create a dynamic timestamp
def create_timestamp():
    now = datetime.datetime.now()
    timestamp = now.strftime('%m-%d-%Y %H:%M:%S:%f')
    return str(timestamp)

# hashing function
def hash_it(filename):
    # filename = input("Enter the file name: ")
    md5_hash = hashlib.md5()
    with open(filename,"rb") as f:
        # Read and update hash in chunks of 4K
        for byte_block in iter(lambda: f.read(4096),b""):
            md5_hash.update(byte_block)
        return md5_hash.hexdigest()

# use os.walk to crawl through directories and perform the hash
def dirContents_hash():
    dir_count = 0
    file_count = 0
    start_path = input("Please enter the absolute path to the directory you want to scan: ")
    # start_path = "/home/osboxes/Desktop/lab32_dir" # linux test path
    # start_path = "C:\Users\cornt\OneDrive\Desktop\lab32folder" # windows test path
    for (path,dirs,files) in os.walk(start_path):
        print('DIRECTORY: {:s}'.format(path))
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

            file_count += 1
            filename = os.path.join(path,file)
            the_hash = hash_it(filename)
            timestamp = create_timestamp()
            print(timestamp)
            print(f"FILENAME: {file}\tSIZE: {str(fsize) + unit}\tPATH: {filename}")
            print("HASH: " + the_hash + "\n")

           
    # Print total files and directory count
    print('Summary: hashed {} files in {} directories'.format(file_count,dir_count))
    dir_count = 0
    file_count = 0   

dirContents_hash()