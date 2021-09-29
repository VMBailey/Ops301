#!/usr/bin/env python3

# Script Name:      Requests Library
# Author:           Vincent Bailey
# Last Rev:         9/28/2021
# Purpose:          This script will look up HTTP GET requests that a user
#                   will specify.

# Import libraries

import requests
import time

print("Alright, let's check out some websites!")
time.sleep(2.5)

website = input("Please enter a website address: ")
print ("GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS")
method = input("Please enter an HTTP Method of the following options: ")

print ("You are about to send a",(method),"request to",(website))

answer = input("Are you ready for this? y/n: ")

if answer == "y":
 print (requests.get(website))

response = requests.get(website)

if response:
  print ('Congratulations!')
else:
  print ("404: It ain't here, whatever you're looking for.")