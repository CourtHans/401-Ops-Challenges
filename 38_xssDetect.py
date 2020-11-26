#!/usr/bin/env python3

# Script:                   401 Op Challenge Day 38
# Author:                   Courtney Hans
# Date of latest revision:  11/25/20
# Purpose:                  XSS detection   

### Install requests bs4 before executing this in Python3

# Import libraries

import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###

# This function will comb through your designated page ('url') and grab all the forms from the HTML content of a page (searching for the designate "form." We'll need this in prep for filling out any/all forms we encounter.) #
def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###

# The function below creates soup 'objects' out of the forms and puts them in a list (details = {}) and continues on to gather details of each form (action, method) and attributes (input/input type).
def get_form_details(form):
    details = {}
    action = form.attrs.get("action").lower()
    method = form.attrs.get("method", "get").lower()
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###

# This function submits the forms from the dictionary containing form details created by the function above (get_form_details) and populates the input fields with the strings contained in the variable 'value'. It constructs to full url if only a relative path is given. The form is submitted via get or post (dependant upon the form method). #
def submit_form(form_details, url, value):
    target_url = urljoin(url, form_details["action"])
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        return requests.get(target_url, params=data)

### In your own words, describe the purpose of this function as it relates to the overall objectives of the script ###

# Once given a url, this function grabs all the HTML forms and prints out the number of forms detected. It moves through each form, submitting with an insertion of Javascript (js_script)). If the Javascript is successfully passed and executed, the variable is_vulnerable is deemed True. The function will then return the vale of is_vulnerable to indicate whether or not the web page in question is, in fact, susceptible and vulnerable to XSS attacks. #
def scan_xss(url):
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('Dude. This site is vulnerable.')</scripT>"#Added HTTP and JS code here to cause a XSS-vulnerable field to create an alert.
    is_vulnerable = False
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
    return is_vulnerable

# Main

### In your own words, describe the purpose of this main as it relates to the overall objectives of the script ###

# "__name__" evaluates to the name of the current module; if being run in the terminal, it is automatically set to "__main__". So this is essentially directing the script to execute the commands beneath it when running in the terminal - in this case, askin the user to input a URL to test, and then running that URL through the scan_xss function and printing out the results. #
if __name__ == "__main__":
    url = input("Enter a URL to test for XSS:") 
    print(scan_xss(url))

### DONE: When you have finished annotating this script with your own comments, copy it to Web Security Dojo
### DONE: Test this script against one XSS-positive target and one XSS-negative target
### DONE: Paste the outputs here as comments in this script, clearling indicating which is positive detection and negative detection

# DVWA Login page
# dojo@dojo-VirtualBox:~/Desktop$ python3 pythonfile.py
# Enter a URL to test for XSS:http://dvwa.local/login.php
# [+] Detected 1 forms on http://dvwa.local/index.php.
# False

# DVWA Reflected Cross Site Scripting page - I thought this would show up as vulnerable, but it did not...
# dojo@dojo-VirtualBox:~/Desktop$ python3 pythonfile.py
# Enter a URL to test for XSS:http://dvwa.local/vulnerabilities/xss_r/
# [+] Detected 1 forms on http://dvwa.local/vulnerabilities/xss_r/.
# False

# Pointed at the same website as in the tutorial - FourOrFour at xss-game.appspot.com/level1/frame
# dojo@dojo-VirtualBox:~/Desktop$ python3 pythonfile.py
# Enter a URL to test for XSS:https://xss-game.appspot.com/level1/frame
# [+] Detected 1 forms on https://xss-game.appspot.com/level1/frame.
# [+] XSS Detected on https://xss-game.appspot.com/level1/frame
# [*] Form details:
# {'action': '',
#  'inputs': [{'name': 'query',
#              'type': 'text',
#              'value': "<script>alert('Dude - vulnerable.')</script>"},
#             {'name': None, 'type': 'submit'}],
#  'method': 'get'}
# True