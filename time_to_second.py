# a python exercise to convert units of time to seconds

#let's have the user input their specified time into the prompt
days = int(input("Enter the days: ")) * 3600 * 24
hours = int(input("Enter the hours: ")) * 3600
mins = int(input("Enter the minutes: ")) * 60
secs = int(input("Enter the seconds: "))
# add them all together
time = days + hours + mins + secs

#display the results
print("The amount of seconds: ", time)