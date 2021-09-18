import csv
import os
from os import *
import time as t

def UserReg():
    try:
        udopen = open("ccmd.csv",'r')
        print("\n File Exist")
        udopen.close()
        pass
    except IOError:
        print("The File doesn't exist")
        udopen = open("userdata.csv",'w',newline='')
        top = ["Full Name","Age","ID Type",'ID Number','Contact Info']
        adddata = csv.writer(udopen,delimiter='|')
        adddata.writerow(top)
        udopen.close()
    fullname = input("Enter FullName: ")
    userage = input("Enter Age:")
    print("Select ID Type:")
    print("1. Aadhar")
    print("2. Pancard")
    print("3. Driving License")
    print("4. Passport")
    print("5. Voter ID")
    seld = input()
    if seld == 1:
        print("You have chosen Aadhar")
        idask = input("Enter ID Number:")
    elif seld == 2:
        print("You have chosen Pancard")
        idask = input("Enter ID Number: ")
    elif seld == 3:
        print("You have chosen Driving License")
        idask = input("Enter ID Number: ")
    elif seld == 4:
        print("You have chosen Passport")
        idask = input("Enter ID Number: ")
    elif seld == 5:
        print("You have chosen Voter ID")
        idask = input("Enter ID Number: ")
    else:
        print("Please Choose the Right Option.")


    contact = input("Enter Contact Info: ")
    udopen = open("userdata.csv",'a',newline=" ")
    adddata = csv.writer(udopen,delimiter=',')
    adddata.writerow([fullname,userage,seld,contact])
    udopen.close()

def Modify():
    x = 0
    print("Modify")
    sname = input("Enter name to search: ")
    udedit = open("userdata.csv","r+")
    r = csv.reader(udedit)
    print("Full Name\t\tAge\t\tID Type\t\tID Number\t\tContact Info")
    for i in r:
        if sname in i:
            for j in r:
                print(j,"\t\t\t",end="")
                x = 1
        print("\n")
    udedit.close()
    if(x==0):
        print("No Search Results. :/")
    else:
        udopen = open("userdata.csv",'r')
        udclose = open("notammar.csv",'w',newline='')
        w = csv.writer(udclose,delimiter=',')
        r = csv.reader(udclose)
        for i in r:
            if i[0] == sname:
                fullname = input("Enter Full Name:")
                userage = input("Enter Age:")
                print("Select ID Type:")
                print("1. Aadhar")
                print("2. Pancard")
                print("3. Driving License")
                print("4. Passport")
                print("5. Voter ID")
                seld = input()
                if seld == 1:
                    print("You have chosen Aadhar")
                    idask = input("Enter ID Number:")
                elif seld == 2:
                    print("You have chosen Pancard")
                    idask = input("Enter ID Number: ")
                elif seld == 3:
                    print("You have chosen Driving License")
                    idask = input("Enter ID Number: ")
                elif seld == 4:
                    print("You have chosen Passport")
                    idask = input("Enter ID Number: ")
                elif seld == 5:
                    print("You have chosen Voter ID")
                    idask = input("Enter ID Number: ")
                else:
                    print("Please Choose the Right Option.")
            else:
                w.writerow(i)
        udopen.close()
        udclose.close()
        os.remove('userdata.csv')
        os.rename('notammar.csv','userdata.csv')
        print('\n File Updated')

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

def UserFolder():
    udopen = open('userdata.csv','r')
    r = csv.reader(udopen)
    print("Full Name\t\tAge\t\tID Type\t\tID Number\t\tContact Info")
    for i in r:
        for j in r:
            print(j,"\t\t\t",end="")
        print('\n')
    udopen.close()

def clear():
    system(clear)
