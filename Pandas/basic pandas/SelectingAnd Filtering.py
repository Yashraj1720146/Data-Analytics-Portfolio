import pandas as pd


df = pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\data\Sample - Superstore.xls") 
# print(df["Profit"])   #selected profit column
subset=df[["Profit","Discount"]]
print(subset)
# print(subset.to_string(index=False)) # to ignore index in output

# filtered_rows= df[(df["Profit"] > 50) & (df["Profit"] < 53)]
# print(filtered_rows)


