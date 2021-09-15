# Script Name:                     Python File Handling
# Author:                          Vincent Bailey
# Date of Latest Revision:         9/14/2021
# Purpose:                         This script writes a haiku into a text file, prints the first
#                                  line into the user's terminal and then deletes the text file.


from os import remove

newfile = open("newtextfile.txt", "w")
newfile = open("newtextfile.txt", "a")


newfile.write("A dance of salt and sweet, \n")
newfile.write("Betwixt two mountains of yeast. \n")
newfile.write("The Fountain of Youth.")


print ("A dance of salt and sweet,")

remove("newtextfile.txt")