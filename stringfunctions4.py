# All about Strings cont...
# From the website: https://edube.org/learn/pe-2/string-methods-58
# cd D:\PythonProject\learnpython
# python .\stringfunctions4.py

# When it comes to sorting lists in python, there are only 2 methods: 
# sorted() which will return a new sorted list and sort() which returns the same list but as sorted

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek) # sorted() will return a new list

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort() # Note that we are utilizing the same variable that holds the list and re-printing it after the sort() functjion is used
print(second_greek)
