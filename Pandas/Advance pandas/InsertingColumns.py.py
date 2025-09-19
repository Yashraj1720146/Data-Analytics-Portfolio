import pandas as pd
import numpy as np

df=pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.xlsx")
# print(df.columns)

#adding columns direct method

# df["Bonus"] = df['Salary'] * 0.1    
# print(df)


#adding columns insert method

df.insert(0,"Emp_id", np.arange(1,len(df)+1))
print(df) 