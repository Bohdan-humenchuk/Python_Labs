# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random
print("hello world")
print("start of the program\n")
arr = np.array([[random.randint(0, 100) for i in range(0, 207)]for j in range(0, 13)]) 
print(arr, "\n") 

def nearestNum(A, z):
    arr = [] 
    for el in A: 
        arr.append(el[(np.abs(A - z)).argmin()])
    array=np.asarray(arr) 
    
    return array[(np.abs(array - z)).argmin()]
    

print("nearest:", nearestNum(arr, 41))