""" 
a Python exercise to get a newly-generated 
string from a given string where "Is" has been added to the front. 
Return the string unchanged if the given string already begins with "Is"
"""

#first, let's create a new function that takes the parameter called text
def new_string(text):
    #now, let's check if the length of text is greater than or equal to 2
    if len(text) >= 2 and text[:2] == "Is":
        return text
    else:
        return "Is" + text
    
print(new_string("Great"))

print(new_string("IsFun"))