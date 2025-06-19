# All about Strings cont...
# From the website: https://edube.org/learn/pe-2/string-methods-58
# cd D:\PythonProject\learnpython
# python .\stringfunctions3.py

'''
Python strings can also use the logic operators, such as: 
==
!=
>
>=
<
<=
Keep in mind that python is not a linguistic language and does not know that Alpha and alpha are the same theing but with a character difference
'''

if('alpha' < 'alphabet'): # this will print true because alphabet is longer than alpha
    print("its a tru")
else:
    print("itsa false")
    
if('beta' > 'Beta'):
    print("beta is bigga because Beta is uppercase, uppercase people are lesser valued characeters")
else:
    print("whatda?")

if('alpha' == 'Alpha'): # nothing will be printed because alpha does not equal to Alpha
    print('no')

# Since Python only comapares the value of the character or strings as ASCII values, any comparisons between strings and digits/integers won't work
# For example, '10' == '010' or '10' == 10, will both return false
if('10' == '010'):
    print("its a tru")
else:
    print("itsa false")

if('10' > '010'): 
    print("its a tru")
else:
    print("itsa false")

if('10' == 10): 
    print("its a tru")
else:
    print("itsa false")