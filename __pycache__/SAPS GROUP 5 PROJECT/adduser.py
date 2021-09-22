import csv
import os

def add_user():
    sname = input("Enter Name to Search: ")
    udopen = open("userdata1.csv",'r')
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

            w.writerow(i)
            udopen.close()
            udclose.close()
            os.remove('userdata1.csv')
            os.rename('notammar.csv','userdata1.csv')
            print('\n File Updated')