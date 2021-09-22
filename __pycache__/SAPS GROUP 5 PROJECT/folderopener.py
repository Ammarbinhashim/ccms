import csv
def UserFolder():
    udopen = open('userdata1.csv','r')
    r = csv.reader(udopen)
    print("Full Name\t\tAge\t\tID Type\t\tID Number\t\tContact Info")
    for i in r:
        for j in r:
            print(j,"\t\t\t",end="")
        print('\n')
    udopen.close()
