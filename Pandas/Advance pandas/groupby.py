import pandas as pd
# import numpy as np

df=pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.xlsx")

# grouped=df.groupby("Age")["Salary"].sum()  #for single columns
# print(grouped)


grouped=df.groupby(["Age","First Name"])["Salary"].sum()  #for single columns
print(grouped)
