# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:41:36 2021

@author: Asus
"""

def maxconsone(arr):
    m=0
    r=0
    for i in arr:
        if i==1:
            r=r+1
        else:
            if r>m:
                m=r
            r=0
    if r>m:
        m=r
    return m

    
array=list(map(int,input().split(",")))
print(maxconsone(array))