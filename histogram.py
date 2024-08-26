# a python exercise to create a histogram from a given list of nubmers

#first, let's create a function for our histogram

def histogram(items):
    #iterate through the items in our list
    for n in items:
        output = '' 
        times = n
        #A while loop to append '*' to the output string 'times' number of times
        while times > 0:
            output += '*'
            times = times - 1 #decrament variable by 1

        print(output)
#call our function with our preferred list
histogram([5,2,7,1])