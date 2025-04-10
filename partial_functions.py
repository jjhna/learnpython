#Partial functions allow the user to re-create a new function that uses less parameters than the older function
#For example, say you have a function that can muliply but you need something similar but only to double an input amount

from functools import partial

def multiply(x, y):
        return x * y

# create a new function that multiplies by 2
dbl = partial(multiply, 2)
print(dbl(4))

'''
An important note: the default values will start replacing variables from the left. The 2 will replace x. y will equal 4 when dbl(4) is called. It does not make a difference in this example, but it does in the example below.
'''

#Following is the exercise, function provided:
def func(u, v, w, x):
    print("u = ", u)
    print("v = ", v)
    print("w = ", w)
    print("x = ", x)
    return u*4 + v*3 + w*2 + x
#Enter your code here to create and print with your partial function
#See how we had to label each argument to which variable
equalsixty = partial(func, v=0, w=0, x=0)
print(equalsixty(15))

#Note here that we don't mark the arguments and by default it will use the right most side of the original func function x = 10
equalsixtyPart2 = partial(0, 0, 0, func)
print(equalsixtyPart2(10))
# so x = 10
