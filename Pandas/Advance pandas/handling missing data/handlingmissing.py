import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\misssingemp.csv")
# print(df)
# df.dropna(axis=0,inplace=True)      #for removing misssing valuse

# df.fillna(0,inplace=True)        #updateing missing valuse by 0
# print(df.columns)

#update calculated value

df['Bonus'].fillna(df['Bonus'].mean(),inplace=True) 
print(df)




