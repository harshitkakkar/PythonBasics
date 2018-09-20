import matplotlib.pyplot as mt
import pandas as pd

df =pd.read_csv("nwedemo.csv")
#df["Age"].plot(kind="bar")
#df.plot(kind="bar")
df["Age"].plot(kind="pie")
mt.ylabel("Age")
mt.xlabel("Row numbers")
mt.show()


"""size = [40,30,30]
lab=["india","USA","UK"]
exp =[0,0,0.5]

mt.pie(x=size , labels=lab, colors=["red","Orange","Brown"], explode=exp)
mt.title("Country")
mt.show()"""

""""y=[90,80,60,93,68,40,50]
x=["Harry","sam","Rohan","Neha","Shruti","Surabhi","Kanu"]
mt.bar(x,y,width=0.3 , color=["red","Green"])
mt.ylabel("percentages")
mt.xlabel("Names")
mt.show()"""

