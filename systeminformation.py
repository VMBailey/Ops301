#!/bin/bash
# Script Name:      System Information
# Author:           Vincent Bailey
# Last Rev:         20210907
# Purpose:          This script will return the user's hostname, IP information, and their 
#                   system information.

import subprocess

print("Hostname")
host=subprocess.run(["whoami"])

print("IP Information")
user=subprocess.run(["ip a"])

print("System Information")
cpu=subprocess.run(["lshw", "-c",])




# The IP information line is not working properly. Going to fix this tomorrow.