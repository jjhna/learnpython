def do_stuff_with_number(n):
    print(n)

def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError: # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)

catch_this()

actor = {"name": "John Cleese", "rank": "awesome"}

def get_last_name():
    '''
    How this works:
    The list actor with the index name will be returned
    The value inside this list "John Cleese" will be split into a list: "John", "Cleese"
    Then the value from that list [1] which is "Cleese" will be returned from the function
    '''
    return actor["name"].split()[1]

get_last_name()
print("All exceptions caught! Good job!")
print("The actor's last name is %s" % get_last_name())

#Better example
actor2 = {"name": "Mike Cheese", "rank": "awesome"}

def get_last_name(thelist):
    #Remember that "in" can be specifically used for finding values in a list, and we're only trying to get the word "name" from the keys
    try:
        if "name" in thelist:
            return thelist["name"].split()[1]
        else:
            #Note that you don't return exceptions/errors instead you need to raise them
            raise TypeError
    except KeyError:
        return "There are no names in that list"
    except IndexError:
        return "There isn't a name in that list"
    except TypeError:
        return "The wrong type of value (non-string) is in the list"

get_last_name(actor2)
print("All exceptions caught! Good job2!")
print("The actor's last name is %s" % get_last_name(actor2))