#a python exercise to convert the bytes of a string to integers

#let's define a variable sentence to convert

sentence = "Sally sells seashells by the seashore."

#let's print the original message for clarification
print("Original String: ")
print(sentence)

#now, let's create an empty list
numbers = []

#we'll print a message to convert the bytes to a list of integers

print("\nConvert bytes of string to list of integers: ")

#iterate through each character (byte) in the string and append its ASCII value to the nubmer list
for chr in sentence:
    numbers.append(ord(chr))

#display the results
print(numbers)