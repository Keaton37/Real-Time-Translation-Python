# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:45:38 2026

@author: keato
"""
 
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])
 
blank_arr = np.zeros((3,3))
 

print(blank_arr)

for index, x in np.ndenumerate(arr):
    print(index, x) 
    blank_arr[index] = arr[index]
    
    

    
print(blank_arr)

