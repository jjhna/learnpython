# All about Modules cont...
# From the website: https://edube.org/learn/pe-2/importing-a-module-math-14
# cd D:\PythonProject\learnpython
# python .\module2.py

# now say you wanted only pi function and nothing else then you would use this syntax: 
from math import pi

# note that you don't require the math namespace due to the import syntax
print(pi)

# However, please note by doing this you'll overwrite the pi import and it will no longer contain the original value
pi = 3.14

# Note you can also import all the functions and entities from the module, this is an unsafe practice
# from math import *
