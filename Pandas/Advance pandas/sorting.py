import pandas as pd
import numpy as np

df=pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.xlsx")


# df.sort_values(by='First Name' ,ascending=True,inplace=True) # single column
# print(df[['First Name', 'Last Name', 'Salary']])



# df.sort_values(by=['First Name', 'Age' ],ascending=True,inplace=True) # single column
# print(df[['First Name', 'Last Name', 'Age']])


df.sort_values(by=['Salary', 'Age' ],ascending=False,inplace=True) # single column
print(df[['First Name', 'Salary', 'Age']])

# This means:

# Sort the entire DataFrame by Salary (descending, high → low).

# If two or more people have the exact same Salary, then use Age (descending) to decide among them.