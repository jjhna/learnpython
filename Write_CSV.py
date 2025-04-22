'''
CSV = comma seperated values, a data format file that is delimited with commas ,
'''

import csv

'''
As you can see below, f2 is in "w" write mode for the open function,
NOTE: please note that with "w" mode if the file doesn't exist in the directory with that name then a new file with that name will be created 
f2 will create and open a new file called newfilename.csv which will be utilized with the reader() function
f1 will read only a file name called mycsvfile.csv which will be utilized with the writer() function 

We need the headers of the files to be stored first so it will be stored into the header variable using the next() function
Then we write the header into the file using writerow and then we will iterate through the entire list using a for loop

open newfilename.csv and you should see the file with the contents from the mycsvfile.csv file
'''

with open('newfilename.csv', 'w') as f2:
    with open('mycsvfile.csv', mode='r') as f1:
        reader = csv.reader(f1)
        csvwriter = csv.writer(f2)
        header = next(reader)  # store the headers and advance reader pointer
        csvwriter.writerow(header) #writes the header into new file
        for row in reader:
            csvwriter.writerow(row)

'''
Another example below but with adding content from the python script into the csv file record: 

rows = [["foo", "bar", "spam"],
       ["oof", "rab", "maps"],
       ["writerow", "isn't", "writerows"]]

filename = "university_records.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

'''

'''
You can also use DictWriter for Dictionary objects: 

import csv
f = open('info.csv', 'w')
with f:

    fnames = ['firstname', 'lastname']
    writer = csv.DictWriter(f, fieldnames=fnames)

    writer.writeheader()
    writer.writerow({'firstname' : 'Rob', 'last_name': 'Scott'})
    writer.writerow({'firstname' : 'Tom', 'last_name': 'Brown'})
    writer.writerow({'firstname' : 'Henry', 'last_name': 'Smith'})

'''