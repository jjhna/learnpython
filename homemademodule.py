# All about Modules cont...
# From the website: https://edube.org/learn/pe-2/modules-and-packages-31
# cd D:\PythonProject\learnpython
# python .\homemademodule.py
# Note that for modules, any other imported modules in another module won't be ran twice

# print("I like to be a module.")

counter = 0

if __name__ == "homemademodule":
    print("You got the name of the module")
else:
    print("Sumthin went worng")
