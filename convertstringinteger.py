# All about Strings cont...
# From the website: https://edube.org/learn/pe-2/string-methods-58
# cd D:\PythonProject\learnpython
# python .\convertstringinteger.py

# How to convert a string to integer and vice versa an integer to a string
# For example, say below we want to convert integers and floats into a string: 
itg = 7
flt = 1.7
si = str(itg) # note that our str() function will transform the integer and float to a string
sf = str(flt)
print("Here is the integer in a string form: " + si + " and the float form as a string: " + sf)

# Here we will try to do the vice versa, from transforming from a float or intger to a string
# however, this will only work if the value of the string is a number and nothing else ex:

num1 = '7'
float1 = '1.7'
sn1 = int(num1)
sn2 = float(float1)

print("The new integer number (not a string) is: ", sn1, " the new float number (not a string) is: ", sn2)
# please note that + does not work with strings and integers so you need to use a comma ,
