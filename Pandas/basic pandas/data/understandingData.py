import pandas as pd

#Rows (understaing the way dat is stored)

# df = pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\data\Sample - Superstore.xls") 
# print(df.head(5))


# df = pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\data\Sample - Superstore.xls") 
# print(df.tail(10))


#understanding data

#info() Method
# df = pd.read_excel(r"C:\Users\yashr\OneDrive\Desktop\code\data analyticts\Pandas\data\Sample - Superstore.xls") 
# print(df.info())

data= {

    "Name":['Ram','Shyam','Raj'],
    "Age":[10,20,30],
    "City":['Pune','Mumbai','nagpur']
}

df=pd.DataFrame(data)
print(df.info())

