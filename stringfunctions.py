# All about Strings cont...
# From the website: https://edube.org/learn/pe-2/string-methods-49
# cd D:\PythonProject\learnpython
# python .\stringfunctions.py

# Learning about the built in string functions

# capitalize() only the first letter in the string and leaves everything else lower case, note that numbers and spaces are considered the first letter but won't be impacted
print('aBcD'.capitalize()) # will print out "Abcd"

# center() centers the string as much as possible into the center of 10 characters, the beginning and ends of the strings will be filled with whitespaces
print('[' + 'alpha'.center(9) + ']') # will print out "  alpha  "
print('[' + 'albha'.center(8) + ']') # will print out " alpha  "

# endswith() function will return a true or false by checking if the arguments in endswith() is in the end of the provided string
t = "zeta"
print(t.endswith("a")) # will print true, because "zeta" ends with an "a"
print(t.endswith("A")) # will print false, because "zeta" ends without an "A"

# find() the fund function will look for the substring if it exists in the provided string, however it returns a 1 for true and -1 for false, index() retruns true or false or error for non-strings
print("Eta".find("ta")) # returns a 1
print("Eta".find("m2a")) # returns a -1

# isalnum() function checks if the provided string contains numbers or characters, so special characters will return a false and numbers and characters return a true
print('lambda'.isalnum()) # returns true
print('30'.isalnum()) # returns true
print('@'.isalnum()) # returns false

# isalpha() function, similar to isalnum() but only for characters
print("Moooo".isalpha()) # true
print('Mu40'.isalpha()) # false because 40

# isdigit() function, similar to isalnum() but only for numbers
print('2018'.isdigit()) # true
print("Year2019".isdigit()) # false because of Year

# islower() will onlly accept lowercase characters
print("Moooo".islower())
print('moooo'.islower()) # true


# isspace() will only accept whitespaces
print(' \n '.isspace()) # true
print(" ".isspace()) # true
print("mooo mooo mooo".isspace())

# isupper() will only accept uppercase characters
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper()) # true

# join() will combine multiple characters into a single string however each characters in the list will be separated by whatever variable you enter as the provider
# note that it only accpets lists as the argument
print(",".join(["omicron", "pi", "rho"])) # returns omicron,pi,rho
print(" ".join(["omicron", "pi", "rho"])) # returns omicron pi rho

# lower() function similar capitlize() but will return the entire string as lowercase, of course the source string remains untouched
print("SiGmA=60Aa".lower()) # this will return sigma=60aa
