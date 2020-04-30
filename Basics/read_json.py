import json
emp = '{"101":"Max","102":"Sam","103":"Ravi"}'

ans=json.loads(emp)
print(type(ans))
print(ans)

fp = open("sample.json")
ans1= json.load(fp)  # loads when you pass values are string , load while opening a file
print(ans1)