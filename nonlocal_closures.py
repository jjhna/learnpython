'''
The nonlocal keyword is a special variable that allows the inner loops to utilize the outer loop variables or arguments for the inner func

You can see below that the inner function variable num is 5 but 4 on the outside due to not using the nonlocal keyword
On the other hand you can see the inner function variable number to be 3 in both the inside and outside using the nonlocal keyhword

Example:
'''

num = 4
def print_msg(number):
    def printer():
        nonlocal number
        number=3
        num = 5
        print("inner func number is: ", number)
        print("inner func num is ", num)
    printer()
    print("outter func number is: ", number)
    print("outter func num is ", num)

print_msg(9)

'''
Closures - A function that is defined inside another function and remembers the variables from the enclosing function scope
They are created when a nested function refers to the variable defined in the enclosing (outer) function. 
Essentially they are outer functions that return an inner function
ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.(Eg. When there are few methods in a class, use closures instead).

Think of it as a variable with a function calling another function

When you call make_multiplier(2), it returns multiplier but with x=2 baked into it.
Example: 
'''

def make_multiplier(x):
    def multiplier(n):
        return x * n
    return multiplier
# Important note when returning a function do not call it with its arguments or enclosures, ie ()

double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))  # 10
print(triple(5))  # 15


# your code goes here
def multiplier_of(num):
    def multiply(numba):
        number = num * numba
        return print(number)
    return multiply
# Important note when returning a function do not call it with its arguments or enclosures, ie ()

multiplywith5 = multiplier_of(5)
multiplywith5(9)
