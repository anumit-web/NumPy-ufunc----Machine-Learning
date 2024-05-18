#   python3 pandas_Read_CSV.py
"""

python3 NumPy_ufuncs_NumPy_Logs.py

"""

import pandas as pd
import numpy as np

print("************************************")

arr = np.arange(1, 10)

log2Array = np.log2(arr)

print(log2Array)

print("---------------------------------------------------")

arr = np.arange(1, 10)

log10Array = np.log10(arr)

print(log10Array)

print("---------------------------------------------------")

arr = np.arange(1, 10)

logeArray = np.log(arr)

print(logeArray)


print("---------------------------------------------------")

from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))

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

