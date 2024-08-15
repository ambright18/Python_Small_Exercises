# a simple pyton exercise to count how many 4's are in a given list

#first, let's create a function to perform the count

def count_4(number):
    #let's set the count to 0 
    count = 0

    for num in number:
        if num == 4:
            count = count + 1
    return count

print(count_4([1, 4, 9, 10, 11, 4]))
print(count_4([4, 4, 17, 21, 39, 4]))