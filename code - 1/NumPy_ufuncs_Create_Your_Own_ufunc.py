#   python3 pandas_Read_CSV.py
"""

python3 NumPy_ufuncs_Create_Your_Own_ufunc.py

"""

import pandas as pd
import numpy as np

print("************************************")

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


print("---------------------------------------------------")

print(type(np.add))

print("---------------------------------------------------")

print(type(np.concatenate))

print("---------------------------------------------------")

print(type(np.blahblah))


print("---------------------------------------------------")

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')

print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")


print("---------------------------------------------------")



"""
x = ["apple", "banana", "cherry"] 	list 	
x = ("apple", "banana", "cherry") 	tuple
x = {"name" : "John", "age" : 36} 	dict 	
x = {"apple", "banana", "cherry"} 	set
"""

"""
x = list(("apple", "banana", "cherry")) 	list 	
x = tuple(("apple", "banana", "cherry")) 	tuple
x = dict(name="John", age=36) 	dict 	
x = set(("apple", "banana", "cherry")) 	set
"""

