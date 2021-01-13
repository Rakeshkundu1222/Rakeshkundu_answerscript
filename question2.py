# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:39:40 2021

@author: Asus
"""

def sol(dict2):
    p=0
    
    for i in dict2:
        if dict2[i]>p:
            p=dict2[i]
            q=i
    return [p,q]
dict1={"1":"name 1","2":"name 2","3":"name 3"}
dict2={"1":50,"2":60,"3":70}
print('"'+sol(dict2)[1]+'"'+':',sol(dict2)[0])