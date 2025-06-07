# All about Modules cont...
# From the website: https://edube.org/learn/pe-2/modules-and-packages-31
# cd D:\PythonProject\learnpython\packages
# python .\runpackage.py

# Packages in a sense, is a clump of modules in a heirarchy of folders/files to make your life easier with built in files 
# Normally one would utilize the pip install "packages" command but in this example we will build our own package (just like the previous home made module from last time)

from sys import path
# From here we go one level up out of our packages and enter back into packages folder
path.append('..\\packages')

# Note, that our package isn't the packages folder but is from the extra folder due to the __init__.py file inside the extra folder
# importing from the extra package and from the iota module from the FunI() function
import extra.iota
print(extra.iota.FunI())

# This also works
from extra.iota import FunI
print(FunI())

import extra.good.best.sigma
from extra.good.best.tau import FunT

print(extra.good.best.sigma.FunS())
print(FunT())

# or even easier: 

import extra.good.best.sigma as sig
import extra.good.alpha as alp

print(sig.FunS())
print(alp.FunA())
