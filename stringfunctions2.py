# All about Strings cont...
# From the website: https://edube.org/learn/pe-2/string-methods-58
# cd D:\PythonProject\learnpython
# python .\stringfunctions2.py

# Learning more additional built in string functions

# lstrip() function returns a new single string by removing all LEADING whitespaces (and combination of characters based off the parameters) in the string
print("[" + " tau ".lstrip() + "]") # this will return [tau ] because " tau " has a leading whitespace
print("www.cisco.com".lstrip("w.")) # will remove all "w's" and "." periods from the provided string until it hits a string not in the combo
print("pythoninstitute.org".lstrip(".org")) # same as it removes only the leading characters so "p" from python isn't in .org so nothing is removed

# rstrip() function does the same as above but from the right side
print("[" + " upsilon ".rstrip() + "]") # returns [ upsilon] because it removes the trailing whitespaces from the right side
print("cisco.com".rstrip(".com")) # returns cis because any combination of . c o m is removed from the right side to the left

# replace() function returns a string with the replacement of the other string provided by the two parameters
# the first parameter is the string that needs to be replaced, the second parameter is the string that will replace the first parameter
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org")) # 2nd arg repalces 1st
print("This is it!".replace("is", "are")) # This are it!
print("Apple juice".replace("juice", "")) # Apple

# rfind() similar to the find() function where it finds the provided argument character in the string, it does the same thing but starts from the right side, returns -1 if not found
print("tau tau tau".rfind("ta")) # returns position 8 because 8 is the first "ta" entry from the right

# split() function splits the provided string into multiple strings in a list, the opposite of the join() functon
print("phi       chi\npsi".split()) # will return ['phi', 'chi', 'psi'] because new lines aren't impacted and all of it to be considered as a single string

# startswith() function is the oppsoite of the endswith() function, checking to see if the string starts with the argument substring
print("omega".startswith("om")) # returns true

# strip() function removes all leading and trailing whitespaces
print("[" + "   alpha   ".strip() + "]") # returns [alpha]

# swapcase() function swaps all characters from lowercase to upeprcase and uppercase to lowercase, vice versa
print("I know that I know nothing.".swapcase()) # returns i KNOW THAT i KNOW NOTHING.

# title() function changes all first charcter in every other word to uppercase like a movie title
print("I know that I know nothing. Part 1.".title()) # returns I Know That I Know Nothing. Part 1.

# upper() function, unlike the capitalize() function, this function will return a string with all the characters being in uppercase format
print("I know that I know nothing. Part 2.".upper()) # returns I KNOW THAT I KNOW NOTHING. PART 2.
