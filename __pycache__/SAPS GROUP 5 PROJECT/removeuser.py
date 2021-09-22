import os
import csv
import time as t

def kickhimout():
    x = 0
    print("Deletion")
    sname = input("Enter Name to search: ")
    udopen = open('userdata.csv','r+')
    r = csv.reader(udopen)
    print("Full Name\t\tAge\t\tID Type\t\tID Number\t\tContact Info")
    for i in r:
        if sname in i:
            for j in i:
                print(j,"\t\t\t",end=" ")
                found = 1
        print("\n")
    udopen.close()
    if x == 0:
        print("No Search Results. :/")
    else:
        udopen = open('userdata.csv','r')
        udclose = open('notammar','w',newline=" ")
        w = csv.writer(udopen,delimeter=",")
        r = csv.reader(udopen)
        for i in r:
            if i[0]==sname:
                pass
            else:
                w.writerow(i)
        udopen.close()
        udclose.close()
        os.remove("userdata.csv")
        os.rename('notammar.csv','userdata.csv')
        print("Loading....")
        t.sleep(5)
        print('\n Deleted')
