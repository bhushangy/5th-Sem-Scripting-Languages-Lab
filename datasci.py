import numpy as np
import pandas as pd

#diff b/w np and pd
# pd has dataframe which is an in memory data structure which is not available in numpy
# pandas is built on numpy
# data transformation --> making 
# 2 types of attr --> categorical & numerical
# categorical attr --> categories exists within that column i.e in survived column der are 2 cateories dead and survived...there are 2 types ...nominal and ordinal categorical 
# similarly embarked attribute is categorical cause there are specific categories...ex country,Pclass... datasets that have categorical attribute are supervised datasets
# attr like age are not categorical attributes...
# null values or empty cells have Nan 

# travelling with siblings or spouse , parent or children are numerical attr

#first attr in countplot function shud be categorical attrbute




df = pd.read_csv('titanictrain.csv') # url or path or filename here
#print(df.head())  # displays first 5 rows of all columns 
df['Survived'] = df['Survived'].map({       # map --> change the dataframe to map 0 and 1 values to died and survived
    0:'Died',
    1:'Survived'
})
#print(df.head())

# first fill null values before mapping using fill not applicable(fillna) method
df['Embarked'] = df['Embarked'].fillna('S') # fill
df['Embarked'] = df['Embarked'].map({
    "S":"shivaji",
    "C":"cadbury",
    "Q":"Quote"
})
print(df.head())
df.drop(['Parch','PassengerId','Name','Ticket','Embarked'],axis=0,inplace=True) #inplace --> if inplace is true it modifies original dataset..if false it modifies a view of the dataset 
#axis --> if axis=0 then column if 1 then row..here drop column...so use axis = 1
# if axis = 0  then error saying can't find the specifies 'rows'

print(df.head())