import json
import pickle

#dumps is a method that takes an object and returns back a string
json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)

pickled_string = pickle.dumps([4, 5, 6, "d", "e", "f"])

#Note important the loads functions converts the string back into a dictionary
print(pickle.loads(pickled_string))



import json

# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here:
    # Here we are loading the string that we received from the salaries variable below, note that it's a string not a dictionary due to the ''
    old_salary = json.loads(salaries_json)
    # Add the key value pair name: salary to the dictionary to old_salary
    old_salary[name] = salary
    # then we convert the old_salary dictionary back into a string using the dumps method
    salaries_json = json.dumps(old_salary)
    # so it should return a string: '{"Alfred" : 300, "Jane" : 400, "Me": 800 }' from the additions marked below:
    return salaries_json

# test code
salaries = '{"Alfred" : 300, "Jane" : 400 }'
new_salaries = add_employee(salaries, "Me", 800)
decoded_salaries = json.loads(new_salaries)
print(decoded_salaries["Alfred"])
print(decoded_salaries["Jane"])
print(decoded_salaries["Me"])