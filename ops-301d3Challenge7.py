#!/usr/bin/env python3

# Script Name:      System Information
# Author:           Vincent Bailey
# Last Rev:         9/28/2021
# Purpose:          This script will create directories and subdirectories
#                   for a provided directory path.

# Import libraries

import os

# Declaration of variables
path=input("Enter A Filepath: ")
### Read user input here into a variable

# Declaration of functions

### Declare a function here

def creator():
    for (root, dirs, files) in os.walk("path"):
        ### Add a print command here to print ==root==
        print(root)
        ### Add a print command here to print ==dirs==
        print(dirs)
        dirs[:] = [x for x in dirs if not x.startswith('.')]
        ### Add a print command here to print ==files==
        print(files)
        files[:] = [x for x in files if not x.startswith('.')]

# Main
creator()
### Pass the variable into the function here

# End