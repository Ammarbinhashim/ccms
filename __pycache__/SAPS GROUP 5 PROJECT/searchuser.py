import csv

def search_user():
    x = 0
    print("Modify")
    sname = input("Enter name to search: ")
    udedit = open("userdata1.csv","r+")
    r = csv.reader(udedit)
    print("Full Name\t\tAge\t\tID Type\t\tID Number")
    for i in r:
        if sname in i:
            for j in r:
                print(j,"\t\t\t",end="")
                x = 1
        print("\n")
    udedit.close()
    if(x==0):
        print("No Search Results. :/")
