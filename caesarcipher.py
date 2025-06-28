# All about Strings cont.. see python .\caesardecrypt.py for the decryption method
# From the website: https://edube.org/learn/pe-2/four-simple-programs-12
# cd D:\PythonProject\learnpython
# python .\caesarcipher.py

# Caesar cipher.
# Note that this method does NOT take any spaces, because space is not a alphabet character
text = input("Enter your message: ") # takes in an input from the console 
cipher = '' # the variable placeholder for the text that you want to print out to the user
for char in text: # we perform a loop of every character in the text that the user provided to encrypt
    if not char.isalpha(): # if the character is not a alphabet letter 
        continue    # then we continue with the for loop process
    char = char.upper() # make the character in uppercase
    code = ord(char) + 1 # we create a variable to assign the unicode of the character and increase it by one, ord() function converts the character to a unicode number
    if code > ord('Z'): # if the unicode of the character is a higher number than 'Z'...
        code = ord('A') # then we make that character an A because there isn't an alphabet bigger than 'Z'
    cipher += chr(code) # After all the checks and changes, we append or add the character of the unicode into the cipher variable

print(cipher) # print out the new encrypted message 
