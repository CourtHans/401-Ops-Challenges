#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 37
# Author:                   Courtney Hans
# Date of latest revision:  11/24/20
# Purpose:                  Cookie Capture


########## Ops Challenge - Cookie Capture Capades ##############

# The below Python script shows one possible method to return the cookie from a site that supports cookies.

import requests, os

# targetsite = input("Enter target site:") # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp" # Comment this out if you're using the line above
response = requests.get(targetsite)
cookie = response.cookies

def bringforthcookiemonster(): # Because why not!
    print('''

              .---. .---.
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.
   .'   "   '  "  .    "  . '  "  `.
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.

        ''')

bringforthcookiemonster()
print("Target site is " + targetsite)
print(cookie)

# Add here some code to make this script perform the following:
# - Send the cookie back to the site and receive a HTTP response
# - Generate a .html file to capture the contents of the HTTP response
# - Open it with Firefox

##############################################

html = requests.get(targetsite, cookies=cookie)
content = html.text

with open ('cookiefile.html', 'w') as f:
  f.write(content)

print("Opening website....")

os.system("firefox /home/kali/Desktop/cookiefile.html")

# resource: https://stackoverflow.com/questions/50329050/save-load-html-response-as-object-in-a-file-python