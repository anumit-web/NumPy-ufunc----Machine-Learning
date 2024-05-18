#   python3 pandas_Read_CSV.py
"""

python3 NumPy_ufuncs_NumPy_Trigonometric_Functions.py

"""

import pandas as pd
import numpy as np

print("************************************")


print("---------------------------------------------------")

x = np.sin(np.pi/2)

print(x)


print("---------------------------------------------------")

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x = np.sin(arr)

print(x)


print("---------------------------------------------------")

arr = np.array([90, 180, 270, 360])

x = np.deg2rad(arr)

print(x)

print("---------------------------------------------------")

arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])

x = np.rad2deg(arr)

print(x)


print("---------------------------------------------------")

x = np.arcsin(1.0)

print(x)

print("---------------------------------------------------")

arr = np.array([1, -1, 0.1])

x = np.arcsin(arr)

print(x)

print("---------------------------------------------------")

base = 3
perp = 4

x = np.hypot(base, perp)

print(x)


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

