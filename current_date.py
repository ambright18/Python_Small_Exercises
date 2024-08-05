# a small program exercise that tells you the current time and date

import datetime #import this module to work with the date and time

#a variable to hold the current date and time
now = datetime.datetime.now()

print("Current date and time is: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))