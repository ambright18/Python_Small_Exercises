# a python exercise program to check if a letter is a vowel or not

#first, let's create a function to perform our operation to simplify things
def is_vowel(char):
    all_vowels = 'aeiou'

    return char in all_vowels

#let's print our result using our function to check if our letters are True or False
print(is_vowel('f'))
print(is_vowel('i'))