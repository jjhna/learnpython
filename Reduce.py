'''
Reduce is another built-in function that reduces a sequence of elements to a single value.
So it grabs an iterable list of numbers and uses the first argument (a func()) to iterate through each element while keeping the previous results as the first element
Please note that reduce() can have 3 arguments, if the 3rd argument is used, then its utilized as the first element otherwise the first element from the iterable list is used
Please also note that you have to import the reduce() function

For example:
'''

from functools import reduce

numbers = [3, 4, 6, 9, 24, 12]

def custom_sum(first, second):
    return first + second

'''
As in the example below you can see that the custom_sum function will iterate through the numbers list. 
However, since a 3rd argument is utilized the first element will be 11 
so in the custom_sum() the first = 11 and then second = 3 which comes out to 14
then we go through the list with the next first = 14 and second = 4 which comes out to 18 and then so on
we go through the entire list until we hit the end which will come out toe a result of 69
'''
result = reduce(custom_sum, numbers, 11)
print(result)

