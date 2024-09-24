# a python exercise to get the size of an object in bytes

#we need to import the sys module to get the size of the bytes
import sys

# have the user enter three numbered strings. Ex: one, five, seven
print("Enter three strings below. Example: one, five, seven")
string1 = input("Enter string 1 here: ")
string2 = input("Enter string 2 here: ")
string3 = input("Enter string 3 here: ")

x = 0
y = 128
z = 177.21

#print the size of bytes in each variable
print("Size of ", string1, "=", str(sys.getsizeof(string1)) + " bytes")
print("Size of ", string2, "=", str(sys.getsizeof(string2)) + " bytes")
print("Size of ", string3, "=", str(sys.getsizeof(string3)) + " bytes")
print("Size of ", x, "=", str(sys.getsizeof(x)) + " bytes")
print("Size of ", z, "=", str(sys.getsizeof(z)) + " bytes")

#working well so far. Now, let's try a list and tuple next.

lst = [1, 6, 4, 'Blue', 'Green']
print("Size of ", lst, "=", str(sys.getsizeof(lst))," bytes")

tple = ("Blue", [5,7,9], (3,4,1))
print("Size of ", tple, "=", str(sys.getsizeof(tple))," bytes")