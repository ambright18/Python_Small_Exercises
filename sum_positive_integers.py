# a python exercise to get the sum of the first n positive integers

#let's have a user enter a num into a prompt

num  = int(input("Enter a number here: "))

#now, let's use a formula to calculate the first positive number of the integer

sum = (num * (num + 1)) / 2

#time to display the results
print("Sum of the first ", num , "positive integers is " , sum)