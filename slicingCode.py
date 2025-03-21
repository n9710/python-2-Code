import pandas as pd
import numpy as np

data=np.arange(1,17).reshape(4,4)
df=pd.DataFrame(data,index=['a','b','c','d'],columns=['p','q','r','s'])
print(df)
print(df.loc['a':'c'])
print(df.loc['a':'d','p':'s'])     #slicing base on rows or columns name
print(df.loc['b':'c','q':'r'])

print(df.iloc[1,3])
print(df.iloc[0:3,0:3])   #slicing base on index

# print(df[df['a']%2==0])