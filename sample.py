import csv
from os import read
userdata = open("userccm.csv",mode='w',newline='')
writer = csv.writer(userdata)
writer.writerow(['NAME OF THE USER','AGE','ID TYPE','ID NUMBER','CONTACT INFO'])
writer.writerow(['SAMEEN SARDAR.S','69','AADHAR','6969696969','919446969954'])
writer.writerow(['AMMAR BIN HASHIM','17','AADHAR','3998593865','919292939443'])
userdata.close()

useropen = open("userccm.csv",mode='r')
read_file = csv.reader(useropen)
for w in read_file:
    print(w)
