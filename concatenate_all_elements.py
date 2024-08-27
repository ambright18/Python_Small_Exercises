# a python exercise to concatenate all elements in a list into a string

#first, let's create a function

def concatenate_list_data(list):
    result = '' #initialize an empty string

    #iterate through the elements in the list
    for element in list:
        result += str(element) #convert elements into a string and concatenate results

    return result

print(concatenate_list_data([8, 6, 14, 5]))