#an easy peasy exercise to check if a file exists in python

#first, import the os.path module
import os.path
#this print line should return false
print(os.path.isfile("file_exists.txt"))

#this print line should return true
print(os.path.isfile("file_exists.py"))