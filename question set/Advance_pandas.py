import pandas as pd
import numpy as np



df = pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.xlsx") 
print(df)
df1=pd.read_csv(r"Pandas/misssingemp.csv")
print(df1)

# csv_path = r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.csv"
# df1 = pd.read_csv(csv_path)


# ================================
# 📌 ADVANCED PANDAS QUESTION SET
# ================================

# 🔹 1. Modifying DataFrame
# Q1. Create a new column "Bonus" = 10% of "Salary".

# df['Bonus'] = df["Salary"] * 0.10
# print(df)



# Q2. Use .insert() to add a "DepartmentCode" column at the first position.

# df.insert(0, 'Department Code', np.arange(101, 101 + len(df)))
# print(df)


# # Generate codes like D0101, D0102 ...
# codes = [f"D0{str(i).zfill(2)}" for i in range(101, 101 + len(df))]

# df.insert(0, "Department Code", codes)
# print(df)

# Q3. Update the "Salary" of employees where "Age" > 40 → increase by 5000 using .loc[].
# Q3. Update the "Salary" of employees where "Age" > 40 → increase by 5000
# df= df.loc[df['Age'] > 40, 'Salary'] + 5000
# print(df)

# Q4. Multiply the "Age" column by 2 (operate full column at once)
# df['Age']= df['Age'] * 2
# print(df)

# 🔹 2. Removing Columns
# Q5. Remove a single column "Expenditure".
# df.drop(columns=['Expenditure'],inplace=True)
# print(df)

# print(df.columns)


# Q6. Remove multiple columns "Savings" ,"Savings Percentage"
# df.drop(columns=[ "Savings" ,"Savings Percentage"],inplace=True)
# print(df)


# 🔹 3. Handling Missing Data

# Q7. Identify missing values in the dataset using .isnull().

# print(df1.isnull().sum())

# Q8. Drop all rows with missing values using .dropna().
# df1.dropna(axis=0,inplace=True)
# print(df1)

# Q9. Fill missing "Salary" values with the mean salary.
# df1['Salary'] = df1['Salary'].fillna(df1['Salary'].mean())
# print(df1)



# Q10. Use .interpolate() to fill missing "Age" values.

# df.interpolate(method='linear',axis=0,inplace=True)
# print(df)
# 🔹 4. Sorting & Aggregation
# Q11. Sort employees by "First Name" in ascending order.
# df.sort_values(by="First Name", ascending=True,inplace=True)
# print(df)  
# print("\n--- Sorted First Names ---\n")  
# print(df["First Name"].to_string(index=False))


# Q12. Sort by "Salary" (descending) and then "Age" (ascending).
# df.sort_values(by="Salary", ascending=False,inplace=True)
# print(df["Salary"])


# Q13. Find the average salary of all employees.
# Remove INR and commas, convert to float
# df["Salary"] = df["Salary"].replace({'INR': '', ',': ''}, regex=True).astype(float)
# avg_salary = df["Salary"].mean()
# print("Average Salary:", avg_salary)


# Q14. Find the maximum salary by "Department".
# Ensure Salary is numeric
# df["Salary"] = df["Salary"].replace({'INR': '', ',': ''}, regex=True).astype(float)
# max_salary_by_dept = df.groupby("Department Type")["Salary"].max()                           #dep is not present in table so will throw error
# print("Maximum Salary by Department:\n", max_salary_by_dept)

# 🔹 5. GroupBy
# Q15. Group employees by "Department" and count them.
# Q16. Find the average "Age" of employees grouped by "Gender".
avg_age = df.groupby("Gender")["Age"].mean()
print(avg_age)

# Q17. Find the total salary grouped by "EmployeeType".

# 🔹 6. Merging & Joining
# Q18. Merge two DataFrames (employees & departments) on "DeptID" using inner join.


# Q19. Perform left join to get all employees even if no department is assigned.
# Q20. Perform outer join to combine both employee and department data (including unmatched rows).

# 🔹 7. Concatenation
# Q21. Concatenate two DataFrames vertically (stack rows).
# Q22. Concatenate two DataFrames horizontally (add columns).

# ================================
# Now write your code below each question step by step 🚀
# ================================
