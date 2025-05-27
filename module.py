# All about Modules 
# From the website: https://edube.org/learn/pe-2/modules-3
# cd D:\PythonProject\learnpython
# python .\module.py

# Modules are similar to packages from java, in fact packages in Python are a clump of modules 
# Unlike classes - which are a template of an object, modules are a tad similar to classes but instead of being a blueprint to an object, its just a python file with those contents 
# modules allow you to reuse the file contents in multiple other python scripts without the need to create the object/classes, ex: 
# note math is a built in module of python
import math

# note that the pi uses the namespace math. to avoid the confusion of the variable pi below
print(math.pi)

pi = 3.14
print(pi)
