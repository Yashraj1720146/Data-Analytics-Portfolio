import pandas as pd
import numpy as np

df=pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.xlsx")
print(df[['First Name', 'Last Name', 'Salary']])


df.loc[0,'Salary'] = 50000
print(df[['First Name', 'Last Name', 'Salary']])