# a python exercise to count the number of occurances of a specific character in a sentence.


#we'll use a loop for this exercise, let's start by creating a sentence variable

#have the user input a sentence
sentence = ("Sally sells seashells by the seashore.")

print("Original string: ")
print(sentence) #display the user's sentence to make sure it's displaying as the original

#for this sentence, we'll count then number of 's' in the string
print("Number of of occurances of 's' in the said string")

count = 0

for c in sentence:
    if c == 's':
        count = count + 1

print(count)

