# Script Name:                     System Information
# Author:                          Vincent Bailey
# Date of Latest Revision:         9/9/2021
# Purpose:                         This script will create a new user and then store that user within AD.

Import-Module ActiveDirectory

New-ADUser -Name "Franz Ferdinand" -GivenName "Franz" -Surname "Ferdinand" -SamAccountName "FFerdinand" -UserPrincipalName "ferdi@globexpower.local" -Email "ferdi@globexpower.com" -Title "TPS Reporting Lead" -Department "TPS" -Company "GlobeX USA" -City "Springfield" -State "OR" -Enabled $true -AccountPassword(Read-Host -AsSecureString "Enter Your New Password, Bub!")