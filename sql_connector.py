import sqlite3

con = sqlite3.connect("C:\\Users\harshit.kacker\harshit.db")
cr=con.cursor()
#cr.execute("SELECT * from emp")
#cr.execute("INSERT into emp values (?,?)",(int(input("Enter,id")), input("Enter,name")))
#print("value added")
#cr.execute("UPDATE emp set  name=? where id=?",(input("Enter new name"),int(input("Enter id to change"))))
#print("value updated")
cr.execute("DELETE from emp where id=?",(int(input("enter the id")),))
print("value deleted")
con.commit();

"""print(cr.fetchall())
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())"""

"""mylist = cr.fetchmany(3)
for val in mylist :
    for data in val :
        print(data) 
        
for val in mylist :
    print(val[0],"    ",val[1]) """