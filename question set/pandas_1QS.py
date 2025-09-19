import pandas as pd

# Load dataset

df = pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.xlsx") 
print(df)


# csv_path = r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\basic pandas\archive\employee_data.csv"
# df1 = pd.read_csv(csv_path)

# print(df1.head())
# print(df1)
# print(df.columns)
# ------------------------------
# 📌 SERIES & DATAFRAME BASICS
# ------------------------------

# Q1. Create a Pandas Series using the "FirstName" column.
# nameSeries=df["First Name"]
# print(nameSeries)

# Q2. Create a DataFrame with only "FirstName", "LastName", and "Age".
# subset_df=df[["First Name","Last Name","Age"]]
# print(subset_df)

# Q3. Display the first 5 rows and the last 5 rows of the dataset.
# print(df.head())
# print(df.tail())

# ------------------------------
# 📌 READING & SAVING DATA
# ------------------------------

# Q4. Read the dataset using read_excel (convert CSV to Excel first).

# df_csv = pd.read_csv("employee_data.csv")
# df_csv.to_excel("employee_data.xlsx", index=False)  

# Q5. Save only "EmpID, FirstName, LastName, age" into a new CSV file.
# subset_df.to_csv("emp.csv",index=False)

# Q6. Save the entire dataset to a JSON file.
# df.to_json("empj.json",index=False)

# ------------------------------
# 📌 EXPLORING & UNDERSTANDING DATA
# ------------------------------

# Q7. Find number of rows and columns in the dataset.
# print(df.info())

# Q8. Print column names of the dataset.
# print(df.columns)

# Q9. Display datatypes of each column.
# print(df.dtypes)


# Q10. Use head() and tail() to explore first and last 10 rows.
# print(df.head())
# print(df.tail())

# Q11. Use info() to understand the dataset.
# print(df.info())

# Q12. Use describe() to summarize numerical columns.
# print(df.describe())

# ------------------------------
# 📌 DATA QUALITY CHECKS
# ------------------------------

# Q13. Find number of missing values in each column.
# print(df1.isnull().sum())


# Q14. Check for duplicate rows and count them.
# duplicates = df1[df1.duplicated()]
# print(duplicates)

# Q15. Convert "StartDate" and "ExitDate" to datetime type.


# df1['StartDate'] = pd.to_datetime(df1['StartDate'])
# df1['ExitDate']= pd.to_datetime(df1['ExitDate'])
# print(df1.dtypes)

# Q16. Identify rows where "ExitDate" is missing (means still employed).
# missingExitDate=pd.isnull(df1['ExitDate'])
# print(missingExitDate)

# ------------------------------
# 📌 SHAPE & COLUMN SELECTION
# ------------------------------

# Q17. Display shape (rows × columns).
# print(df1.shape)

# Q18. Select the column "Performance Score".

# pef_score=df1['Performance Score']
# print(pef_score)


# Q19. Select multiple columns: ["FirstName", "LastName", "Title", "Performance Score"].

# mul_col=df1[['FirstName','LastName','Title','Performance Score']]
# print(mul_col)

# Q20. Select the first 50 rows of the dataset.
# print(df1.head(50))

# ------------------------------
# 📌 FILTERING ROWS
# ------------------------------

# Q21. Select all employees with Performance Score = "Exceeds".
# PerformanceScoreExceeds=df1[(df1["Performance Score"] == 'Exceeds')]
# print(PerformanceScoreExceeds)

# Q22. Select employees who are Active (EmployeeStatus).
# emp_status=df1[(df1["EmployeeStatus"] == 'Active')]
# print(emp_status)
# OR
# emp_status = df1[df1["EmployeeStatus"] == 'Active']
# print(emp_status[["EmpID", "FirstName", "LastName", "EmployeeStatus"]])

# Q23. Select employees from the "Finance & Accounting" division.

# Div = df1[df1["Division"] == 'Finance & Accounting']
# print(Div[["EmpID", "FirstName", "LastName", "Division"]])

# Q24. Select employees with Current Employee Rating > 3.

# Employee_Rating=df1[(df1['Current Employee Rating'] > 3)]
# print(Employee_Rating[["EmpID", "FirstName", "LastName", "Current Employee Rating"]])

# Q25. Select employees with Salary Zone = "A" (PayZone).
# salary_zone_employees = df1[df1["PayZone"] == "Zone A"]
# print(salary_zone_employees[["EmpID", "FirstName", "LastName", "PayZone"]])


# ------------------------------
# 📌 MULTIPLE CONDITIONS
# ------------------------------

# Q26. Select employees who are "Active" AND in "Florida (FL)".
# activeInFl = df1[(df1['EmployeeStatus'] == 'Active') & (df1['State'] == 'FL' )]
# print(activeInFl[["EmpID", "FirstName", "LastName", "EmployeeStatus","State"]])


# Q27. Select employees who are "Terminated" OR have Performance Score = "Active"
# print(df1.columns)
# terminated_Score = df1[(df1["EmployeeStatus"]=='Active') &  (df1["Performance Score"]=='Needs Improvement') ] 
# print(terminated_Score)



# Q28. Select employees who joined after 2020 AND are still Active.
# active_after_2020 = df1[(df1['StartDate'] > '2020-12-31') & (df1['EmployeeStatus'] == 'Active')]
# print(active_after_2020)


# Q29. Select employees with EmployeeType = "Full-Time" AND Rating >= 4.
# Emptype_Rating = df1[(df1['EmployeeType'] == 'Full-Time') &  (df1['Current Employee Rating'] >= 4) ]
# print(Emptype_Rating)

# ------------------------------
# 📌 EXTRA EXPLORATION
# ------------------------------

# Q30. Count number of employees in each DepartmentType.

# department_counts = df1['DepartmentType'].value_counts()
# print(department_counts)

# print(df1.columns)

# Q31. Find average employee rating by Division.
# avg_rating_by_division = df1.groupby('Division')['Current Employee Rating'].mean()
# print(avg_rating_by_division)


# Q32. Which State has the highest number of employees?

# State_count = df1['State'].value_counts()
# # State with the maximum employees
# print(State_count.idxmax())   # prints the state
# print(State_count.max())     # prints the number of employees in that state


# Q33. Group employees by GenderCode and count them.
# gender_count = df1.groupby('GenderCode').size()
# print(gender_count)

# Q34. Find the earliest and latest StartDate in the dataset.

# df1['StartDate'] = pd.to_datetime(df1['StartDate'])

# # Earliest StartDate
# earliest = df1['StartDate'].min()

# # Latest StartDate
# latest = df1['StartDate'].max()

# print("Earliest StartDate:", earliest)
# print("Latest StartDate:", latest)
