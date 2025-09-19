import pandas as pd


#Sample DF

# df1 = pd.DataFrame({
#     "EmpID": [1, 2, 3, 4],
#     "Name": ["Aditi", "Raj", "Sona", "Amit"]
# })

# df2 = pd.DataFrame({
#     "EmpID": [1, 2, 4, 5],
#     "Salary": [50000, 60000, 55000, 70000]
# })

# print("DataFrame 1 (Employees):")
# print(df1, "\n")

# print("DataFrame 2 (Salaries):")
# print(df2, "\n")


# # 1. Inner Join (default)

# inner_merge = pd.merge(df1, df2, on="EmpID", how="inner")
# print("Inner Join:")
# print(inner_merge, "\n")


# # 2. Left Join
# left_merge = pd.merge(df1, df2, on="EmpID", how="left")
# print("Left Join:")
# print(left_merge, "\n")


# # 3. Right Join
# right_merge = pd.merge(df1, df2, on="EmpID", how="right")
# print("Right Join:")
# print(right_merge, "\n")

# # 4. Outer Join
# outer_merge = pd.merge(df1, df2, on="EmpID", how="outer")
# print("Outer Join:")
# print(outer_merge, "\n")


#cross join
import pandas as pd

df1 = pd.DataFrame({
    "EmpID": [1, 2],
    "Name": ["Aditi", "Raj"]
})

df2 = pd.DataFrame({
    "Dept": ["IT", "HR"]
})

print("DataFrame 1:")
print(df1, "\n")

print("DataFrame 2:")
print(df2, "\n")

# Cross Join
cross = df1.merge(df2, how="cross")
print("🔹 Cross Join Result:")
print(cross)
