# Script Name:                     Guessing Game: Python Conditions
# Author:                          Vincent Bailey
# Date of Latest Revision:         9/13/2021
# Purpose:                         This script will use variables declared within the script to
#                                  run a short, interactive guessing game.

import time
import sys

a = 246
b = 389

print("Alright, here we go.")
time.sleep(2.5)

if a == b:
    print("These two buddies are equal!")
    time.sleep(2.5)
elif a!= b:
    print("These two buddies aren't seeing eye to eye. They aren't equal.")
    time.sleep(2.5)

if a < b:
    print ("B is the Superior Number.")
    time.sleep(2.5)
elif a <= b:
    print("A is less than or equal to B. Narrowing it down.")
    time.sleep(2.5)

if a > b:
    print ("A is the Superior Number!")
    time.sleep(2.5)
elif a >= b:
    print ("A is greater than or equal to B. Such a mystery....")
    time.sleep(2.5)

else:
    print("And both of these numbers are somewhere between 200 and 300. Such a mystery....")
    time.sleep(2.5)

print("Can you guess what the number is? ")

Guess=input()

if (Guess == '246'):
    print("Holy shit are you serious? Get out of here, you warlock....")
    time.sleep(2.5)
    sys.exit()
    

if (Guess == '389'):
    print("Holy shit are you serious? Get out of here, you warlock....")
    time.sleep(2.5)
    sys.exit()

else:
    print("Nope. Try again.")
    time.sleep(1)