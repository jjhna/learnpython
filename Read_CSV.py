'''
CSV = comma seperated values, a data format file that is delimited with commas ,

csvsample.csv

['Name', 'Age', 'Sex']
['Goku', '40', 'M']
['Chichi', '40', 'F']
['Gohan', '25', '']
'''

import csv

'''
To open any type of file in python, you will need to utilize the "with" statement - used for context managers
it's mainly used for working with files or network connections 
mostly used with the open() function 
It's then assigned to another variable as an iterable object 
'''

# Please note that "r" mode is only to be in read mode
with open("csvsample.csv", 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)

'''
You can also use DictReader for Ditionary objects: 

import csv
with open('info.csv') as csvfile:
reader = csv.DictReader(csvfile)
for row in reader:
    print(row['firstname'], row['lastname'])

'''