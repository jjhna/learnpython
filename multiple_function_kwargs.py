# **kwargs = keyword arguments

def foo2(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo2(1, 2, 3, 4, 5)


# edit the functions prototype and implementation

# foo needs to recieve 3 > arguments
# must return extra arguments recieved so anything more than 3
def foo(a, b, c, *args):
    return len(args)


# bar needs to recieve 3 > arguments
# must return "true" if the arguments magicnumber = 7 and otherwise "False"
def bar(a, b, c, **kwargs):
    if kwargs.get("magicnumber") == 7:
        return True
    else:
        return False


# test code
if foo(1, 2, 3, 4) == 1:
    print("Good.")
if foo(1, 2, 3, 4, 5) == 2:
    print("Better.")

if bar(1, 2, 3, magicnumber=6) == False:
    print("Great.")
if bar(1, 2, 3, magicnumber=7) == True:
    print("Awesome!")