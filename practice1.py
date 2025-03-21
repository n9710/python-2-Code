import pandas as pd
import numpy as np

arr=np.arange(1,10).reshape(3,3)
df=pd.DataFrame(arr,index=['a','b','c'],columns=['p','q','r'])
print(df)