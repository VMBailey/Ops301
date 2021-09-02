#!/bin/bash

# Script Name: File Permissions
# Author: Vincent Bailey
# Last Revision: 9/1/2021
# A script that changes permissions in a directory designated by the user. BE CAREFUL!!

directorypermissions(){
    cd $filepath
    chmod -r $per $rwx
    ls -l
}


read -p "Hey there! Please enter a directory path: " -r filepath
sleep 1.8

read -p "Cool! I can set permissions in this directory for you. What would you like?" rwx
sleep 1.8

echo "Well alright! Give me a sec..."
sleep 1.8

directorypermissions