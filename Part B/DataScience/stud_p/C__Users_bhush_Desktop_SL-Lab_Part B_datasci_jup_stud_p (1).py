#!/usr/bin/env python
# coding: utf-8

# In[70]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


stu_p = pd.read_csv('studentperformance.csv');

# # 1)
# print(stu_p.head(3))

# # 2)
# print(stu_p.describe())
# stu_p.mathscore.count()
# stu_p.mathscore.max()

# # 3)

# print(stu_p.info())
# print(stu_p.shape)


# refer pandas cheat sheet for explanations for these coomands
#https://www.dataquest.io/blog/pandas-cheat-sheet/

# 4)
#axis --> if axis=1 then column, if 0 then row

stu_p_d = stu_p.drop(['lunch','test preparation course'],axis=1,inplace=False)


# When inplace=True is passed, the data is renamed in place (it returns nothing) i.e modifies the original memory frame, so you'd use:

# df.an_operation(inplace=True)

# When inplace=False is passed (this is the default value, so isn't necessary), performs the operation and returns a copy of the object i.e 
# it is not modified in the memory frame which u loaded in the beginning..the particular column u dropped still exixts in that first df, so you'd use:

# df = df.an_operation(inplace=False) 
# So: here only in df dataframe it is dropped....

# if inplace == False:
#     Assign your result to a new variable
# else
#     No need to assign


#print(stu_p_d.head())
#print(stu_p.head())

# NOTICE THE DIFF HERE...


# 5)

stu_p_d['parental level of education'] = stu_p_d['parental level of education'].fillna('BE')
#print(stu_p_d)


# 6)

stu_p_d['race/ethnicity'] = stu_p_d['race/ethnicity'].map({
    
    'group A':'Asian',
    'group B':'African',
    'group C':'Afro-Asian',
    'group D':'American'
    
})

# #print(stu_p_d.head())


# # 7) 

stu_p_d = stu_p_d.rename(columns = {"reading score": "R Score", "writing score":"W Score"  }, inplace = False)
print(stu_p_d.head())

# #print(stu_p.head())
                                 
#   # see as of now...the original df wrt to stu_p_d is stu_p_d and not stu_p...     


# 8)

stu_p_d['R Score'].mean()


# 9)

gb = stu_p_d.groupby('parental level of education')
# Let's print the first entries 
# in all the groups formed. 

#print(gb.first())

gb = stu_p_d.groupby(['parental level of education']).mean()
print(gb)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




