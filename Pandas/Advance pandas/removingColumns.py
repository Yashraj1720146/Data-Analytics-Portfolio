import pandas as pd
import numpy as np

df=pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.xlsx")
# print(df[['First Name', 'Last Name', 'Salary']])

#For singele col
# df.drop(columns=['Expenditure'], inplace=True)

#for Multiple Columns
df.drop(columns=['Expenditure','Age'], inplace=True)

print(df)
