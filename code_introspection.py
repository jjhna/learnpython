'''
Code Introspection

Help users find more details and info of functions to help debugging or docummentation

Some common introspection functions:

type(obj)	            Returns the type of the object
id(obj)	                Returns the “identity” of the object (memory address)
dir(obj)	            Lists all the attributes and methods of the object
help(obj)	            Shows the help/documentation of the object
getattr(obj, name)  	Returns the value of a named attribute
hasattr(obj, name)	    Checks if an object has a specific attribute
callable(obj)	        Checks if the object can be called like a function
isinstance(obj, cls)	Checks if object is an instance of a class
issubclass(sub, super)	Checks if a class is a subclass of another class

Examples below:
'''

# Use the help function to see what each function does.
# Delete this when you are done.
help(dir)
help(hasattr)
help(id)

# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

# Print a list of all attributes of the Vehicle class.
# Your code goes here, returns true or false if the variable or function name exist in the class or object
print(hasattr(Vehicle, "name"))
print(hasattr(Vehicle, "kind"))
print(hasattr(Vehicle, "car"))
print(hasattr(Vehicle, "description"))
print()


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return "Woof!"

d = Dog("Buddy")

print("type (d) is: ", type(d))        # <class '__main__.Dog'>
print(dir(d))         # List of attributes and methods
print(hasattr(d, 'bark'))  # True
print(getattr(d, 'name'))  # "Buddy"
print(callable(d.bark))    # True
