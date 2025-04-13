'''
Decorators are just another function which takes a function and returns one (as a new function)
Essentially a way to modify or edit the behavior of a function/class without having to change the actual code

'''

def my_decorator_function(argu):
    def wrapper_func():
        print("Before the function runs")
        argu()
        print("After the function runs")
    return wrapper_func

# Decorators start with the @ symbol
@my_decorator_function
# this is a shorthand line for:
# say_hello = my_decorator_function(say_hello)

def say_hello():
    print("Hello!")

say_hello()
print()

def my_decorator_parameters(func):
    def wrapper_dic(*args, **kwargs):
        print("Calling function with args:", args)
        return func(*args, **kwargs)
    return wrapper_dic

@my_decorator_parameters
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")