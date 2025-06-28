# All about Strings cont... see python .\caesarcipher.py for the encryption method
# From the website: https://edube.org/learn/pe-2/four-simple-programs-13
# cd D:\PythonProject\learnpython
# python .\caesardecrypt.py

# Caesar cipher - decrypting a message.
# Note that this method does NOT take any spaces, because space is not a alphabet character
cipher = input('Enter your cryptogram: ') # takes in an input from the console 
text = '' # the variable placeholder for the text that you want to print out to the user
for char in cipher: # we perform a loop of every character in the text that the user provided to decrypt
    if not char.isalpha(): # if the character is not a alphabet letter 
        continue    # then we continue with the for loop process
    char = char.upper() # make the character in uppercase
    code = ord(char) - 1 # we create a variable to assign the unicode of the character and decrease it by one because we want to decrypt the message, ord() function converts the character to a unicode number
    if code < ord('A'): # if the unicode of the character is a lower number than 'A'...
        code = ord('Z') # then we make that character an 'Z' because there we want to loop the character list back from 'Z' to 'A'
    text += chr(code) # After all the checks and changes, we append or add the character of the unicode into the cipher variable

print(text)
