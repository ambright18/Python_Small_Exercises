#An exercise program to see whether a number is within 100 of 1000 or 2000

#first, let's define a function with the necessary calculations
#so we can simple call on it later for ease of use

def near_thousand(n):
    # Check if the absolute difference between 1000 and n is less than or equal to 100
    # OR check if the absolute difference between 2000 and n is less than or equal to 100
    return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

#now, let's call our function and enter our desired number arugments to see if it's true or false

print(near_thousand(750))
print(near_thousand(1000))
print(near_thousand(2567))
print(near_thousand(1547))