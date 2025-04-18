'''
Filter() function is similar to map but it filters only true conditions
It accepts a function that "can" produce true or false (if it can't then the filter just simply returns the iterable)
and then it accepts one iterable that gets passed into the function
'''

scores = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]

def is_A_student(score):
    return score > 75

over_75 = list(filter(is_A_student, scores))

print(over_75)

# Another example:

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

'''
Remember lambda is just a temp function for a one time use
word[::-1] is a version of slicing, in this case it will reverse the wording of a string
sequence[start:stop:step] - since we have no start or stop variable we will start from beginning to end
in this case the function word() is taking the variable word and checking to see if it reverses it with the slicing, will it still be the same after the slicing? 
'''
palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)
