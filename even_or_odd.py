# a python exercise that checks if an entered number is even or odd

num = int(input("Enter a number: "))

mod = num % 2

if mod > 0:
    print("This is an odd number.")
else:
    print("This is an even nubmer.")