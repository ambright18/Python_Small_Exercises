# a simple python program to print out the calendar for any 
# entered month and year

#first, let us import the calendar module
import calendar

#now, let's have the user enter a month and year

year = int(input("Enter a year here: "))
month = int(input("Enter a month here: "))

#display the results using the calendar module we imported

print(calendar.month(year, month))