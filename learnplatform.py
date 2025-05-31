# All about Modules cont...
# From the website: https://edube.org/learn/pe-2/useful-modules-platform-20
# cd D:\PythonProject\learnpython
# python .\learnplatform.py

# Platform modules allows the user to identify the python, OS and hardware that the code is currently running on
from platform import platform, machine, processor, system, version, python_implementation, python_version_tuple

# For example, the code below will print out the OS that the code is currently utilizing
print(platform())
print(platform(1))
print(platform(0, 1))

print(machine())

print(processor())

print(system())

print(version())

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
