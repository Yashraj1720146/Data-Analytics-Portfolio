import pandas as pd
import numpy as np

df=pd.read_csv(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\misssingemp.csv")
print(df.isnull().sum())
