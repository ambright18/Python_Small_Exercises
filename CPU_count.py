# a python exercise to check the number of CPUs being used

#We'll need to import the module called 'multiprocessing'
import multiprocessing

cpu_count = multiprocessing.cpu_count()
print(cpu_count)