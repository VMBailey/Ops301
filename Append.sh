#!/bin/bash

# Script Name: Append
# Author: Vincent Bailey
# Last Revision: 8/30/2021

date=$(date + "%T")

echo "Alright, I'll start copying the Syslog for ya! One sec..."
cp -r /var/log/syslog C:\Users\Vincent\Documents
sleep 1.8

echo "Moving over to the Documents folder really quick..."
cd C:\Users\Vincent\Documents
sleep 1.8

echo "Thanks for being so patient, by the way."
sleep 1.8

echo "Just adding the date and time to the filename now..."
mv syslog syslog "$(date + "%Y%m%d_%T")"
sleep 1.8

echo "All done!".