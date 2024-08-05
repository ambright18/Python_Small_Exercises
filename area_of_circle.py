# a small program exercise to calculate the area of a circle
# based on the radius which is user entered

from math import pi #import the 'pi' constant from the 'math' module

#have the user input the radius of the circle and store it in a variable

radius = float(input("Enter the radius of the circle here: "))

# Calculate the area of the circle using the formula: area = π * r^2
area = pi * radius ** 2

#display the results
print("The area of the circle with a radius of " + str(radius) + " is: " + str(area)) 