#a python exercise that displays a name, age and address on three different lines

#first, let's create a function that holds the personal details

def personal_details():
    name, age = "Alex", 28
    address = "Nashville, Tennessee"

    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))


#call our function that holds said details

personal_details()