# a python exercsie to hash a word

#create a list that maps characters to their soundex codes
soundex = [0, 1, 2, 3, 0, 1, 2, 0, 0, 2, 2, 4, 5, 5, 0, 1, 2, 6, 2, 3, 0, 1, 0, 2, 0, 2]

#prompt the user to input the desired word to be hashed
word = input("Enter the word to hash: ")

word = word.upper() #this will convert it to uppercase
#initialize the coded word with the first character of the entered word
coded = word[0]

#iterate over the remaining charactersin the word
for a in word[1:len(word)]:
    #calculate the index for Soundex list based on the character's ASCII code.
    i = 65 - ord(a)
    coded = coded + str(soundex[i])

print() #print a line break

#display the results
print("The coded word is: " + coded)
print()
