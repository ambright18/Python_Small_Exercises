# a python exercise to get the volume of a sphere

#first, we need to define the value of PI
pi = 3.1415926535897931

# have the user enter the radius of the sphere
radius = float(input("Enter the sphere radius here: "))

#calcualte the volume using the formuala below
volume = 4.0/3.0 * pi * radius**3

print("The volume of the sphere is: ", volume)