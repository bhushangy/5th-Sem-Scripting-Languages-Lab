# here whenever u modify a string... the changes do not appear in the original string...
# thus u gotta append chages to a new string char by char newstr+=' ' 

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def cs(s):
    lis1=[]
    for i in s:
        if i.isalpha():
            lis1.append(ord(i))
        else:
            lis1.append(i)
    
    ns=''
    for i in lis1:
        try:
            i+=1
            ns+=chr(i)
        except:
            ns+=i
    lis2=[]        
    for i in ns:
        if i == '{':
            lis2.append('a')
        elif i == '[':
            lis2.append('A')
            
        else:
            lis2.append(i)
        
    
    nns=''
    lis3=[]
    for i in lis2:
        if i.lower() in ['a','e','i','o','u']:
            lis3.append(i.upper())
        else:
            lis3.append(i)
            
    for i in lis3:
        nns+=i
        
        
        
   
        
    print(nns)
  
        
        
cs('zAbhud')
        
            
            
     
            
            
            
            
            