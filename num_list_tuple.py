# A python program that accepts a sequence of comma-seperated numbers from the user and 
# generates a list and tuple of the inputted numbers

# have the user input a series of numbers seperated by a comma.
numbers = input("Enter comma-seperated numbers here: ")

list = numbers.split(",")

#converst list to tuple
tuple = tuple(list)

#display the results
print("List : ", list)
print("Tuple : ", tuple)