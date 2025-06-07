# All about Modules cont...
# From the website: https://edube.org/learn/pe-2/the-nature-of-strings-in-python-41
# cd D:\PythonProject\learnpython
# python .\strings.py

# Note below the first like or row 7 is listed as 7 characters and line 2 or row 8 is listed as 7 characters as well
# But the print statement comes out to 15, this is because line 1 or row 8 comes with the \n which is counted as one additional character due to the whitespace
multiline = '''Line #1
Line #2'''

print(len(multiline))

str1 = 'a'
str2 = 'b'

# + is concatenated
# * is replicated

print(str1 + str2) # a + b = ab
print(str2 + str1) # b + a = ba
print(5 * 'a') # aaaaa
print('b' * 4) # bbbb

# Say if you need the ASCII or UNICODE value of only 1 character
print(ord(str1)) # a is ASCII 97

# Likewise with the ASCII number you can print out characters
print(chr(97))

# returns true or flase if the character is or isn't in the multiline
print ("e" in multiline)
print ("f" not in multiline)

# Since strings are immutable
# You cannot use del multiline[0]
# Nor can you append such as multiline.append("a")
# Nor can you insert such as multiline.insert(0, "a")

# The string below will print out the minum element of the sequence or A, which is first in the ASCII table will be printed and returned, does not accept empty strings or nulls
print(min("aAbByYzZ"))

# The opposite below will find the maximum element of the sequence, so z
print(max("aAbByYzZ"))

# The index() method, not a function, will find what position or index the character exists in the string
print("aAbByYzZaA".index("b")) # should return 2, because b is in position 2 from 0

# The list() function will seperate every character entry in a list, so it takes a string as an argument and returns it as a list
print(list("abcabc")) # this will return the list: ['a', 'b', 'c', 'a', 'b', 'c']

# The count() method will count all similar values to the character provided in the argument
print("abcabc".count("b")) # this should return 2, because there are only 2 b characters in the string
