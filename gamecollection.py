# Script Name:                     Game Collection
# Author:                          Vincent Bailey
# Date of Latest Revision:         9/13/2021
# Purpose:                         This script will take a list of objects declared in a variable,
#                                  print those objects, and alter the value of one object.

import time

VidjaGames = ['Viewtiful Joe','Sonic the Hedgehog','Devil May Cry','Bayonetta','Pacman','Megaman','The Legend of Zelda','Resident Evil','Sly Cooper', 'Shovel Knight']

print (VidjaGames[3])

print (VidjaGames[5:10])

VidjaGames[7]= 'Onion!'

print(VidjaGames)
time.sleep(2.5)

print ("Something doesn't belong here....")
time.sleep(2.5)