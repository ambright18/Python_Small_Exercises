# a simple python exercise to group all the value of a list together

#first, let's create a function to perform the desired effect

def concatenate_list(list):
    result = '' #initialize an empty string called result

    for element in list:
        result += str(element)

    return result

#now, let's call our function and add a few numbers in the parameter

print(concatenate_list([1, 2, 7, 12, 21]))