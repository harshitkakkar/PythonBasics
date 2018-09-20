import pandas as pd
import sqlite3

df = pd.read_csv("nwedemo.csv")
df["esal"]=pd.Series([1000,1200,1300,900,200],dtype="float")

print(df)
print("------------------")
print(df.sum())
print("------------------")
print(df["Pid"].max())
print("------------------")
print(df["esal"].min())
print("------------------")
print(df.sort_index(ascending=False))
print("------------------")
df.sort_values(by="Age", inplace=True)
print(df)
print("------------------")
print(df.isnull()) 
print("------------------")     
print(df["Age"].notnull())
print("------------------")
print(df.dropna(axis=1,how="all"))
print("------------------")
print(df.dropna(axis=0,how="all"))
print("------------------")
print(df.drop_duplicates())
print("------------------")
print(df.drop_duplicates("Pid"))
# how= any drop full row(since axis =0) if any value is null 
#and all = if whole row is null then only drop it

###############################################
print("------------------")
print(df.replace({"Genny":"Surabhi", "Kanu":"Kanika", 21:25}))
print("------------------")
print(df.fillna(0.0))
print("------------------")






