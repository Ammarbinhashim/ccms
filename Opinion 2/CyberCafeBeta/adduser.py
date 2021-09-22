import csv
def add_user(tuple):
    print("<<<Adding User>>>")
    writefile = open("userdetails.csv","w",newline="")
    tophead = ["SR NO:","NAME","AGE","EMAIL ID","PHONE NO:"]
    w = csv.writer(writefile)
    w.writerow(["",tuple[0],tuple[1],tuple[2],tuple[3]])
    w.writerow(tophead)
    writefile.close()
    return
