import logbook
import os
from os import *
from logbook import *
import csv


print("PRESS 1 FOR CUSTOMER SERVICE")
s = open("userdata.csv",'w')
w = csv.writer(s,newline=" ")
w.writerow(["Ammar"])
s.close()

k = open("userdata.csv",'r')
r = csv.reader(k)
for i in r:
    print(i)