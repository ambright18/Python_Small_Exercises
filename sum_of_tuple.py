# a python exercise to calculate the sum of a tuple container

#first, we create our tuple list
numbers = (5, 7, 9, 3, 4, 1)

#print a message showing the original tuple list below
print("The original tuple container list")
print(numbers)

print(type(numbers))

sum_tuple = sum(numbers)

#display the results of the calculation
print("Sum of all items in tuple container is ", str(sum_tuple))