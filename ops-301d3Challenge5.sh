#!/bin/bash

# Script Name: Clearing Logs
# Author: Vincent Bailey
# Last Revision: 9/28/2021
# A script that clears important system logs. 

clearlogs(){
    cat /dev/null > syslog
    cat /dev/null > wtmp
    cat /dev/null > auth.log
    cat /dev/null > kern.log
    cat /dev/null > pureftp.log
    cat /dev/null > faillog
    cat /dev/null > daemon.log
    cat /dev/null > kern.log
}

# Change to /var/log directory
cd $dir

# Prints syslog and wtmp's current state to the terminal.
cat syslog
cat wtmp

# Clear chosen logs
clearlogs
echo "Clear Successful"

# Print syslog and wtmp to terminal again
cat syslog
cat wtmp


# syslog: This is a data log that keeps track of everything that happens on a system.

# auth.log: This keeps track of successful or failed authentication logs.

# kern.log: This keeps track of logs from the kernel. Warning information is tracked here as well.

# wtmp: This keeps track of login and logout logs.

# pureftp.log: This monitors the system for FTP connections using the pureftp process.

# daemon.log: This keeps track of background services.

# faillog: This keeps track of failed login attempts. This is a big one to keep an eye on.