import pandas as pd

df = pd.read_csv("nwedemo.csv")
print(df)
print("------------------")
ans = df["Pid"] > 105
print(df[ans])
print("------------------")
print(df[df["Age"]>30])
print("------------------")
print(df[df["Pid"]==102])
print("------------------")
print(df[(df["Pid"].isin([104,111]))])
print("------------------")
print(df[(df["Pid"]<110) & (df["Age"]<30)])
print("------------------")
print(df[(df["Pid"]<110) | (df["Age"]<30)])
print("------------------")
print(df.loc[df["name"]=="Sam"])
