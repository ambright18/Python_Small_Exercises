# a Python exercise to calculate the distance between the points (x1, y1) and (x2, y2).

#let's import the math module
import math

#create some variables to hold our coordinates
point1 = [5,0]
point2 = [8,9]

#create a variable to hold the formula used to calculate the distance between two points 
distance = math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))
#print the resutls
print(distance)
