# All about Modules cont...
# From the website: https://edube.org/learn/pe-2/modules-and-packages-31
# cd D:\PythonProject\learnpython\testfolder1
# python .\runmodule2.py

from sys import path
path.append('..\\testfolder2') # go one level up from out of testfolder1 and into testfolder2, please note you need to use double \\ to escape the first \

# the path below will also work as an alternative, please also note the double backslash \
# path.append('D:\\PythonProject\\learnpython\\testfolder2')

import homemademodule2 as hmm2

print(hmm2.counter)