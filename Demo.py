""" This is my first python code
 
age= int(input("Enter the age"))
if age > 18 and age < 60:
    print("can vote")
elif age < 18 and age > 1:
    print("not allowed")
else :
    print("invalid age") """
###################################
info = r"My name is \n 'harshit'"
print(info)
####################################
print("'harshit'" in info)
print(info.count("i"))
print(info.index("'harshit'"))
for char in info:
    print(char , end = " ")
print(info[0:10])
print(info.split(sep=" "))
########################################
mylist =list([10,20,30,10,40,50,"harshit"])
print(type(mylist))
print(mylist[0:4])
########################################
mylist.append("newly added")
mylist.insert(0, "first")
print(mylist)
print(30 in mylist)
print(mylist.count(10))
#########################################
print(len(mylist))
print(mylist.reverse())
print(mylist)
print(mylist.pop(0))
#########################################
mytupple = (10,20,30,"harshit")
print(type(mytupple))
#print(mytupple.append("newly added"))
print(3 in mytupple)
for val in mytupple :
    print(val)
print(mytupple[0:3])
##########################################
mylist1=[10,90,20]
mytupple2=tuple(mylist1)
print(type(mytupple2))
##########################################
mytupple3 =("harshit")
mytupple4 =tuple("66")
print(type(mytupple3))
print(type(mytupple4))
#########################################
myset={10,3,4,6,20}
myset2={30,7,90,8}
print(type(myset))
print(3 in myset)
print(myset.add(69))
print(myset)
for val in myset:
    print(val)
##########################################
print(myset.union(myset2))
print(myset.difference(myset2))
print(myset.issuperset(myset2)) 
##########################################

