#   python3 pandas_Read_CSV.py
"""

python3 NumPy_ufuncs_NumPy_LCM_Lowest_Common_Multiple.py

"""

import pandas as pd
import numpy as np

print("************************************")

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

print("---------------------------------------------------")

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)

print("---------------------------------------------------")

arr = np.arange(1, 11)

x = np.lcm.reduce(arr)

print(x)

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

