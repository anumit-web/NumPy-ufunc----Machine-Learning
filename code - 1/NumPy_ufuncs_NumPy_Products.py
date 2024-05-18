#   python3 pandas_Read_CSV.py
"""

python3 NumPy_ufuncs_NumPy_Products.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.array([1, 2, 3, 4])

x = np.prod(arr)

print(x)


print("---------------------------------------------------")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

x = np.prod([arr1, arr2])

print(x)

print("---------------------------------------------------")

arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])

newarr = np.prod([arr1, arr2], axis=1)

print(newarr)

print("---------------------------------------------------")

arr = np.array([5, 6, 7, 8])

newarr = np.cumprod(arr)

print(newarr)


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

