# a python exercise to find the built-in and available modules of Python

#first, let's import the sys module to help us
import sys

#now, import the textwrap to format the list of module names
import textwrap

#get a sorted lisst of module names in system
module_name = ', '.join(sorted(sys.builtin_module_names))

#let's use textwrap to format the list and then print it
print(textwrap.fill(module_name, width=70))