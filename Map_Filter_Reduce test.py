# Please note that you have to import the reduce() function
from functools import reduce

# Use map to print the square of each numbers rounded
# to three decimal places
my_floats = [4.3545, 6.09, 3.25, 9.7712, 2.16, 8.883, 4.59]

# Use filter to print only the names that are less than
# or equal to seven letters
my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

# Use reduce to print the product of these numbers
my_numbers = [4, 6, 9, 23, 5]

# Fix all three respectively.

# we simply have to use the built-in function round to round it by 2 digits and iterate through the my_floats list
# map_result = list(map(lambda x: x, my_floats))
map_result = list(map(lambda x: round(x,2), my_floats))
# this is wrong because the current lambda is only taking one argument not 2, then we get the length of name and ask if it's less than 7, if true then it gets returned back
# filter_result = list(filter(lambda name: name, my_names, my_names))
filter_result = list(filter(lambda name: len(name) < 7, my_names))
# thsi is wrong because the first element is 0 and anything multiplied by 0 will return a 0 so we simply have to remove the 0
# reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers, 0)
reduce_result = reduce(lambda num1, num2: num1 * num2, my_numbers)

print(map_result)
print(filter_result)
print(reduce_result)