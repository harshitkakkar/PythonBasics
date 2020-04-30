"""
fp = open("C:/Users\harshit.kacker\eclipse-workspace\python_first\sample.txt")
print(fp.read())
fp.seek(0)   # goes back to first character of the line
mylist =fp.readlines()

for val in mylist :
    print(val)
fw = open("sample_output.txt",'w')
fw.write("Learning python is very interesting")
fw.write("\npython can be used in Analytics also")
fw.write("\nspark code can also written in python")
fw.close()
print("data Written")
"""

"""fw = open("sample_output.txt",'a+')
fw.write("\nlast Line")
fw.seek(0)
print(fw.readlines())
print(fw) """

fp1 = open("demo.csv","r")
print(fp1.read())

fp = open("nwedemo.csv",'w')
fp.write("\nPid,name")
fp.write("\n101,Food")
fp.write("\n102,Coffee")
fp.close()
print("data written")