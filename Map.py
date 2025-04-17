'''
In python there are built in functions that help reduce working and length for simple functions - Pythonic

For example say you needed to iterate through an "entire" list, instead of making a function just for that part you could use the built-in map function to reduce that task

Please note:
str.upper = string.upper - make a string element or object to upper case
lambda - anonymous function

For example below:
'''

my_pets1 = ['alfred', 'tabitha', 'william', 'arla']
uppered_pets1 = []

# Notice how long this task is? lets break it down to one list and one line
for pet in my_pets1:
    pet_ = pet.upper()
    uppered_pets1.append(pet_)

print(uppered_pets1)

my_pets2 = ['Balfred', 'tabitha', 'william', 'arla']

'''
Here we've reduced it to one line and only one list
The map() function will apply a function to every item in an iterable (list olr tuple) and returns a map object (pointer), 
note that it does this in parallel across the iterables
Note that for every argument a function accepts, it requires one iterable to it!!!
If there isn't enough iterables for each argument then it will either fail or truncate the list or tuple that's being iterated over

For example, this will truncate it: 
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
result = list(map(round, circle_areas, range(1, 3)))
print(result)

For example this will fail: 
mike1 = list(map(lambda x, y: x + y, [1, 2, 3]))
print(mike1)
TypeError: <lambda>() missing 1 required positional argument: 'y'
'''

uppered_pets2 = list(map(str.upper, my_pets2))

print(uppered_pets2)

my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [1, 2, 3, 4, 5]

# As noted before lambda is an anonymous function, used mainly for maps() and filter()
# Below, the x elements from my_strings and y elements from my_numbers are paired together in a tuple
results = list(map(lambda x, y: (x, y), my_strings, my_numbers))

print(results)