import pandas as pd
import sqlite3


df=pd.read_csv("new_data.txt",sep=",", header=None, names=["EID","EName","EAge"], skiprows=1 ,nrows=5) 
# by default it is comma
print(df)
"""print("------------------")

con=sqlite3.connect("C:\\Users\harshit.kacker\harshit.db")
df2=pd.read_sql_query("Select * from emp",con)
print(df2)
print("------------------")

df3= pd.read_csv("nwedemo.csv")
print(df3)
print("------------------")
print(df3.head())
print("------------------")
print(df3.tail())
print("------------------")
print(df3.columns)
print("------------------")
print(df3.axes)
print("------------------")
print(df.size)
print("------------------")
print(df3.values)
print("------------------")
print(df3.dtypes)
print("------------------")
print(df3.info())
print("------------------")
print(df["EID"])
print("------------------")
print(df.EName)
print("------------------")
print(df[["EID","EName"]])
print("------------------")
print(df.loc[0:2])
print("------------------")

for k,v in df.iterrows():
    print(k)
    print(v)  """

df["esal"]=pd.Series([1000,1200,1300,900,200],dtype="float")
print(df)

con= sqlite3.connect("C:\\Users\harshit.kacker\harshit.db")
df.to_sql("newemp",con)





















