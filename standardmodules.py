# All about Modules cont...
# From the website: https://edube.org/learn/pe-2/useful-modules-6
# cd D:\PythonProject\learnpython
# python .\standardmodules.py

# For standard modules like "math" you can print out all the module functions/entities 
# the only catch is thtat you need to import all the functions/entities and not use the "from" 
import math

for name in dir(math):
    print(name, end="\t")

