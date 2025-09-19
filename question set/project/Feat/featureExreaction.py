import pandas as pd 
import numpy as np


df=pd.read_csv(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\anime.csv")
# print(df.head)

# Q1. Make a new column for episode count (hint: check if "episodes" column exists, otherwise extract/clean it).
def extract_episodes (txt) : 
    check = False 
    data = "" 
    for i in txt: 
        if i == ")": 
            check = False 
            return data 
        if check == True: 
            data = data + i 
        if i == '(': 
            check = True

df["Episodes"]=df["Title"].apply(extract_episodes)
df["Episodes"]=df["Episodes"].str.replace("eps","")
df["Episodes"]=df["Episodes"].astype(int)
# print(type(df.loc[0]['Episodes']))

print(df)

# Q2. Make a new column for timestamp (current date-time) for all rows.
# def extraction_time(txt):
#     check = False
#     data = ""
#     for i in range(len(txt)):
#         if txt[i] == ')':
#             for j in range(i+1, i+20):
#                 data += txt[j]
#     return data

# df['Total Time'] = df['Title'].apply(extraction_time)



# def extract_month(txt):
#     # Find the closing parenthesis `)`
#     if ")" in txt:
#         after_bracket = txt.split(")", 1)[1].strip()  # take text after `)`
#         parts = after_bracket.split()  # split by space
#         if len(parts) > 0:
#             return parts[0]   # first part should be the month (e.g. "Oct")
#     return None

# # Apply to dataset
# df["Month"] = df["Title"].apply(extract_month)

# print(df.head())


# Q3. Which anime has the highest score?  (hint: use idxmax on "rating" column)

# print(df["Score"].max())
# print(df[df["Score"] == df["Score"].max()])


# Q4. Display top 5 highest scoring anime.
# print(df["Title"].head())

# Q5. Which anime has the highest episode count?
# print(df[df["Episodes"] == df["Episodes"].max()])

# Q6. Display top 5 anime with the highest episode count.
# top5 = df.sort_values("Episodes", ascending=False).head(5)
# print(top5[["Title", "Episodes"]])

# Q7. Which is the longest running anime? (Hint: if dataset has "aired" start-end dates, find the difference)
# Split 'Aired' column into start and end


