# a python exercise to convert height(in feet to inches) to centimeters

#first, let's have the user input what they wish to convert
print("Input your height below... ")

#this will read the feet part of the height
height_ft = int(input("Feet: "))
#this will read the incehs part
height_inch = int(input("Inches: "))

#now, let's use the formula below to convert the entered height to centimeters
height_inch += height_ft * 12 # this will convert the entire input height to inches

height_centimeters = round(height_inch * 2.54, 1) #this will turn it into centimeters

print("Your height is : %d cm." % height_centimeters)

