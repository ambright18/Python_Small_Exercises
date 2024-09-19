# a python exercise to assess if all the numbers in a list are greater than a specific number

def check_list(nums, n):
    return(all(x > n for x in nums))

#create a list with the variable 'nums' containing some values
nums = [10,15,20,25,30,35,60,65,80,85,100]

#let's display the list first
print("Original list numbers: ")
print(nums)

#let's have the user input a the specific number to check against
n = int(input("Enter a number here: "))

print("\nCheck whether all numbers of list are greater than", n)
#let's use the 'check-list' function to see if it is.
print(check_list(nums, n))