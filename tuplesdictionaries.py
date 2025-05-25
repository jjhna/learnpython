# All about Tuples and Dictionaries 
# From the website: https://edube.org/learn/pe-1/tuples-and-dictionaries-21
# cd D:\PythonProject\learnpython
# python .\tuplesdictionaries.py

# Tuple are immutable data, which cannot be modified in any way, unlike a list 
# Tuples use the syntax parentheses () or just commas , but list use the brackets []

tuple_1 = (1, 2, 4, 8)
tuple_2 = 1., .5, .25, .125
not_a_tuple_3 = (1) # note that tuples need a comma, so this variable is not a tuple, this is an int
tuple_3 = (1,) # this is a tuple

print(tuple_1)
print(tuple_2)
print(not_a_tuple_3)
print("what is the variable", type(not_a_tuple_3))
print(tuple_3)
print("what is the variable", type(tuple_3))

# Dictionary are a key-value pair type of data, unlike tuples they are mutable
# Note that they do not preserve the order of the data, so printed values will look different from their inital assignment

dictionary = {
                "cat": "chat", 
                "horse": "cheval",
                "dog": "chien"
              }
phone_numbers = {
                    'boss': 5551234567, 
                    'Suzy': 22657854310
                 }
empty_dictionary = {}

print(dictionary)
print(dictionary['cat'])
print(phone_numbers)
print(phone_numbers['Suzy'])
print(empty_dictionary)

# To reassign, add or remove values from the dictionary: 
dictionary['cat'] = 'minou' # reassign a value
dictionary['swan'] = 'cygne' # to add a value
dictionary.update({"duck": "canard"}) # also to add a value
del dictionary['dog'] # remove a key which also removes the value

# For loops cannot normally iterate through the dictionaries, however there are methods to circumnavigate this: 

# or have it sorted out before iterating through it
for key in sorted(dictionary.keys()):
    print(key, "->", dictionary[key])

# regular method
for key in dictionary.keys():
    print(key, "->", dictionary[key])
          
# Other methods to return different values from dictionaries 
# items() function performs the same step above but in a single step, and making it more efficient and simple 

for english, french in dictionary.items():
    print(english, "->", french)
    print("this is the english man:", english)
    print("this is the frenchy (disgusting):", french)

# another method is through the values() function but just returns the values and not the key: 
for french in dictionary.values():
    print(french)

#