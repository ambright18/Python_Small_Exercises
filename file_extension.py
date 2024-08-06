# a short python exercise program that will check the file
# extension of what the user inputs

file = input("Enter the filename here: ")

file_extension = file.split(".")

print("The extension of the file is: " + repr(file_extension[-1]))