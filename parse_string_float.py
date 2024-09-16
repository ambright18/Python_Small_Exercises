#this is a python exercsie program to parse a string to an integer or float

#first, define a string in a num variable

num = '5431.671'

#now, converst the string to a floating-point number and print it out
print(float(num))

#lastly, convert the floating-point number to an integer, removing the decimal part and print it out
print(int(float(num)))