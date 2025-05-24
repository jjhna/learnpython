# All about functions
# From the website: https://edube.org/learn/pe-1/how-functions-communicate-with-their-environment-25
# cd D:\PythonProject\learnpython
# python .\functions.py

# You may know the normal method of creating a function in Python: 
def testfunc1(menie, mini, moe):
    print("minie:", menie, "mini:", mini, "moe:", moe)

testfunc1("mista1", "mista2", "mista3")

# but you can also specify which argument you want to set: 
testfunc1(moe = "mista1", mini = "mista2", menie = "mista3")

# positioning comes before setting the keyword arguments
# testfunc1(moe = "mista1", "mista2", mini = "mista3") this won't run and return an  error
testfunc1("mista1", moe = "mista2", mini = "mista3")

# here is a regular function that returns a variable from 3 inputs, it returns the largest value in the list
def testfunc2(menie, mini, moe): 
    if(mini > menie):
        menie, mini = mini, menie
        if(menie > moe): 
            return menie
        else:
            return moe
        
    else:
        if(menie > moe):
            return menie
        else:
            return moe

temp1 = testfunc2(1,6,2)
print("the beggest numba is", temp1)

# In certain situations the function can be allowed to return None in two special situations: 
# When you compare it with a variable or value that has nothing in it or when yhou assign a variable with None, as shown below: 
value = None
if value is None:
    print("Sorry, you don't carry any value")

def strange_function(n):
    if(n % 2 == 0):
        return True

print(strange_function(2))
print(strange_function(1))

# NOTE, apparently your also not supposed to iterate through a list with just 1 value since for loops need to be a range of 2 or more

# Global variables are not evil and are necessary in speicifc situations, such as threadded programming or parallel programming
# However, they should be avoided as they are potentially a security risk and may cause some confusion in the future due to other variables or functions with the same name, ex: 
globalvar = "hallo"

def my_function():
    global globalvar
    globalvar = 2
    print("Do I know that variable?", globalvar)


globalvar = 1
my_function()
print(globalvar)

def testfunc3(globalvar):
    globalvar = "SDF"
    print("testfunc3 globalvar", globalvar)

testfunc3("hi")
print("outside the testfunc3 globalvar", globalvar)


