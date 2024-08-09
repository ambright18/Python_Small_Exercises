# A python exercise program to find the sum of 3 given numbers
# if the values are equal, it should return 3 times their sum

#first, let's create a function that takes 3 integer parameters
def sum_three(x, y, z):
    sum = x + y + z

    #Now, let's use an if statement to check if all 3 are euqal
    if x == y == z:
        sum = sum * 3
        #return the sum
    return sum

#Now, let's call on our function and enter 3 numbers for the parameters

print(sum_three(5, 10, 7))

print(sum_three(5,5,5))
