import CoreCode
import csv
import os

def add_user():
    print("<<<Adding User>>>")
    CoreCode.username()
    CoreCode.userage()
    CoreCode.email()
    CoreCode.phone()
    writefile = open("userdetails.csv","w",newline="")
    tophead = ["SR NO:","NAME","AGE","EMAIL ID","PHONE NO:"]
    w = csv.writer(writefile)
    w.writerow(["",CoreCode.username,CoreCode.userage,CoreCode.email,CoreCode.phone])
    w.writerow(tophead)
    writefile.close()
