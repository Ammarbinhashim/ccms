import csv
import os
from email_validator import validate_email, EmailNotValidError
def Userinit():
    try:
        writefile = open("userdetails.csv","r")
        print("File Exist")
        writefile.close()
        pass
    except IOError:
        print("File Doesn't Exist")
        writefile = open("userdetails.csv","w",newline="")
        tophead = ["SR NO:","NAME","AGE","EMAIL","PHONE No:"]
        addrow = csv.writer(writefile)
        addrow.writerow(tophead)
        writefile.close()
    u_name = input("Enter UserName:")
    u_age = input("Enter Age:")
    u_email = input("Enter Email Adress:")
    def email():
        try:
            valid = validate_email(u_email)
            email = valid.email
        except EmailNotValidError as e:
            print(str(e))

    validate_email(u_email)
    u_phone = input("Enter Phone Number:")
    pt1 = tuple(u_phone)
    if len(pt1) != 10:
        print("Error: Please enter the right number")
        u_phone = input("Enter Phone Number:")
    writefile = open("userdetails.csv","w",newline="")
    tophead = ["SR NO:","NAME","AGE","EMAIL","PHONE No:"]
    addrow = csv.writer(writefile)
    addrow.writerow(tophead)
    addrow.writerow(["1.",u_name,u_age,u_email,u_phone])
    writefile.close()

Userinit()

def Add_User():
    x = int(input("Enter number of Users to be added:"))
    for i in range(0,x):
        u_name = input("Enter UserName:")
        u_age = input("Enter Age:")
        u_email = input("Enter Email Adress:")
        def email():
            try:
                valid = validate_email(u_email)
                email = valid.email
            except EmailNotValidError as e:
                print(str(e))

        validate_email(u_email)
        u_phone = input("Enter Phone Number:")
        pt1 = tuple(u_phone)
        if len(pt1) != 10:
            print("Error: Please enter the right number")
            u_phone = input("Enter Phone Number:")
            writefile = open("userdetails.csv","w",newline="")
            tophead = ["SR NO:","NAME","AGE","EMAIL","PHONE No:"]
            addrow = csv.writer(writefile)
            addrow.writerow(tophead)
            addrow.writerow(["1.",u_name,u_age,u_email,u_phone])
            writefile.close()


    with open("userdetails.csv","w",newline="") as writefile:
        writerow  = csv.writer(writefile)
        writerow.writerow(["1.",u_name,u_age,u_email,u_phone])
        writefile.close()
    return



ask = input("Would you like to add a user? (y/n)")
if ask == "y":
    Add_User()
elif ask == "N":
    x = 0
else:
    pass
