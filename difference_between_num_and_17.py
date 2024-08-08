# A short, python exercise to calculate the difference between a given number and 17.



#first, let's define a function called 'difference' that 
#takes an integer parameter "n"

def difference(n):
    if n <= 17:
        # If n is less than or equal to 17, return the absolute difference
        return 17 - n
    else:
        # If n is greater than 17, return the absolute difference multiplied by 2
        return (n - 17) * 2

print(difference(22))
print(difference(14))