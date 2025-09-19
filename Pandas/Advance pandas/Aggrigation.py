import pandas as pd
# import numpy as np

df=pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.xlsx")


df.sort_values(by='First Name' ,ascending=True,inplace=True) # single column
print(df['Salary'].mean())
print(df['Salary'].max())
print(df['Salary'].min())
print(df['Salary'].count())
print(df['Salary'].std())
