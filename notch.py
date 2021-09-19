import os
import random
import csv
import time as sameen

fullname = input("Enter Full Name:")
userage = input("Enter Age:")

def convert(list):
    res = sum(d * 10**i for i, d in enumerate(list[::-1]))
    return(res)

"""ID Generator"""

userid=[]
n=5
for j in range(n):
    userid.append(random.randint(1,20))

newid = convert(userid)

print("Hi",fullname,"Your ID is",newid)
idtype = ['Aadhar','Passport','Pancard','Driving License','VoterID']
print(str(idtype))
idpref = input("Select ID Type:")
if idpref in idtype:
    if idpref == idtype[0]:
        print("You've Chosen",str(idtype[0]))
        idinp = input("Enter ID:")
    if idpref == idtype[1]:
        print("You've Chosen",str(idtype[1]))
        idinp = input("Enter ID:")
    if idpref == idtype[2]:
        print("You've Chosen",str(idtype[2]))
        idinp = input("Enter ID:")
    if idpref == idtype[3]:
        print("You've Chosen",str(idtype[3]))
    if idpref == idtype[4]:
        print("You've Chosen",str(idtype[4]))
else:
    print("Wrong Input. Please Try again")

upload = open("userdata.csv",mode = 'w')
w = csv.writer(upload)
w.writerow([fullname,"\t",userage,"\t",idpref,"\t",idinp,"\t",newid])
upload.close()

print("Select Option:")
print("1. Add User")
print("2. Remove User")
sel1 = float(input())
if sel1 == 1:
    x = 0
    print("Modify")
    sname = input("Enter name to search: ")
    udedit = open("userdata.csv","a+")
    r = csv.reader(udedit)
    for i in r:
        if sname in i:
            for j in r:
                print(j,'\t',end=" ")
                x = 1
            print("\n")
    udedit.close()
    if x == 0:
        print("No Search Results. :/")
    else:
        udopen = open("userdata.csv","r")
        udclose = open("notammar.csv","r+",newline="")
        w = csv.writer(udclose,delimiter=",")
        r = csv.reader(udclose)
        for i in r:
            if i[0] == sname:
                fullname = input("Enter Full Name:")
                userage = input("Enter Age:")
                idtype = ['Aadhar','Passport','Pancard','Driving License','VoterID']
                print(str(idtype))
                idpref = input("Select ID Type:")
                if idpref in idtype:
                    if idpref == idtype[0]:
                        print("You've Chosen",str(idtype[0]))
                        idinp = input("Enter ID:")
                if idpref == idtype[1]:
                        print("You've Chosen",str(idtype[1]))
                        idinp = input("Enter ID:")
                if idpref == idtype[2]:
                        print("You've Chosen",str(idtype[2]))
                        idinp = input("Enter ID:")
                if idpref == idtype[3]:
                        print("You've Chosen",str(idtype[3]))
                if idpref == idtype[4]:
                        print("You've Chosen",str(idtype[4]))
                else:
                    print("Wrong Input. Please Try again")
            else:
                w.writerow(i)
        udopen.close()
        udclose.close()
        os.remove("userdata.csv")
        os.rename("notammar.csv","userdata.csv")
        print("\n File Updated")

elif sel1 == 2:
    x = 0
    print("Deletion")
    sname = input("Enter Name to search: ")
    udopen = open('userdata.csv',"r+",newline="")
    r = csv.reader(udopen)
    print("NAME","\t","AGE","\t","ID TYPE","\t","ID NUMBER","\t","SYSTEMID")
    for i in r:
        if sname in i:
            for j in i:
                print(j,"\t",end="")
        print("\n")
    udopen.close()
    if x == 0:
        print("No search Results. :/")
    else:
        udopen = open('userdata.csv','r')
        udclose = open('notammar.csv','w',newline=" ")
        w = csv.writer(udopen,delimiter=",")
        r = csv.reader(udopen)
        for i in r:
            if i[0]==sname:
                pass
            else:
                w.writerow(i)
        udopen.close()
        udclose.close()
        os.remove('userdata.csv')
        os.rename('notammar.csv','userdata.csv')
        print("Loading.......")
        sameen.sleep(5)
        print("\n Deleted")
