# a python exercise to swap two variables

#let's create our two variables and give them numeric values

a = 55
b = 27

#display the initial values of our variables first
print("Initial Value of a =", a)
print("Initial Value of b =", b)

#now let's swap them using a temporary variable
temp = a
a = b

b = temp

#now, display our results
print("\nAfter swapping value of a =", a)
print("After swapping value of b =", b)