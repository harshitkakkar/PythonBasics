import numpy as np
print(np.__version__)

mylist = [10,20,40,50]
print(mylist*2)

myarr = np.array(mylist)
print(type(myarr))
print(myarr*2)

print(np.append(myarr,100))
print(np.insert(myarr,0,1))

myarr2= np.array((10,20,40,50))
print(myarr2)

print(mylist+mylist)
print(myarr+myarr2)

newarr = np.array([10,20,30,50,40])
print(newarr)

my2darr = np.array([[1,2,39],[58,5,27],[6,57,8]])
print(my2darr)
print(np.max(my2darr))
print(np.min(my2darr))
print(np.sum(my2darr))
print(np.sum(my2darr,axis=0)) 
print(np.sum(my2darr,axis=1))  # axis=0 means rows wise axis=1 means column wise
print(my2darr.T)

for val in my2darr :
    for data in val :
        print(data,end=" ")