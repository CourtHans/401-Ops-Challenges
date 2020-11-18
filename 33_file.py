#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 33
# Author:                   Courtney Hans
# Date of latest revision:  11/18/20
# Purpose:                  Signature-based Malware Detection file crawler


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

# function to check hash against virustotal
def malware_check(the_hash):
    apikey = os.getenv('API_KEY_VIRUSTOTAL') # Set your environment variable before proceeding. You'll need a free API key from virustotal.com so get signed up there first.
    # hash = '099f4bbdaef65e980748a544faffd9a7' # Set your hash here.

    # This concatenates everything into a working shell statement that gets passed into virustotal-search.py
    query = 'python3 virustotal-search.py -k ' + apikey + ' -m ' + the_hash

    os.system(query)

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
    # start_path = "/home/osboxes/Desktop/lab32_dir/lab32folder" # linux test path
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
            print(f"Virus scan against hash:")
            malware_check(the_hash)
            print("")

    # Print total files and directory count
    print('[*]Summary[*] Files hashed: {}, Directories crawled: {}'.format(file_count,dir_count))
    dir_count = 0
    file_count = 0   

# Main
dirContents_hash()

# End