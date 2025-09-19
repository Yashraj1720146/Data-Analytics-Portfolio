import pandas as pd

df1 = pd.DataFrame({
    "EmpID": [1, 2],
    "Name": ["Aditi", "Raj"]
})

df2 = pd.DataFrame({
    "EmpID": [3, 4],
    "Name": ["Sona", "Amit"]
})

# Vertical Concatenation
vertical = pd.concat([df1, df2], axis=0)
print("Vertical Concatenation:")
print(vertical)

# Horizontal Concatenation
df3 = pd.DataFrame({
    "Dept": ["IT", "HR"],
    "Salary": [50000, 60000]
})

# horizontal = pd.concat([df1, df3], axis=1)
# print("Horizontal Concatenation:")
# print(horizontal)
