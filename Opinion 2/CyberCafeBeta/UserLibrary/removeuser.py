import csv
import os

def remove_user():
    x = 0
    print("<<<<DELETE USER>>>>")
    sname = input("Enter name to search:")
    writefile = open("userdetails.csv","r+",newline="")
    tophead = ["SR NO:","NAME","AGE","EMAIL ID","PHONE NO:"]
    r = csv.reader(writefile)
    print(tophead)
    for i in r:
        if sname in i:
            for j in i:
                print(j,"",end="")
                x = 1
        print("\n")
    writefile.close()
    if x == 0:
        print("User not found.")
    else:
        writefile = open("userdetails.csv",'r')
        writefile_init = open("changer.csv","w",newline="")
        w = csv.writer(writefile,newline="")
        r = csv.reader(writefile)
        for i in r:
            if i[0] == sname:
                pass
            else:
                w.writerow(i)
        writefile.close()
        writefile_init.close()
        os.remove("userdetails.csv")
        os.rename("changer.csv","userdetails.csv")
        print("Loading....")
        print("\nDeleted")
        print("\nFile has been updated.")
