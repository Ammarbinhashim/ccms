fullname = input("Enter Fullname: ")
age = input("Enter Age: ")
print("Please Enter ID Type: ")
id_cat = ["Aadhar",
         "Voter ID",
         "Pancard",
         "Driving License",
         "Passport"]
print(str(id_cat))
print("For Aadhar, PRESS 1\nFor Voter ID, PRESS 2\nFor Pancard, PRESS 3 \nFor Driving License,PRESS 4\nFor Passport, PRESS 5",end="\n")
selx = input()
sel1 = id_cat[0]
sel2 = id_cat[1]
sel3 = id_cat[2]
sel4 = id_cat[3]
sel5 = id_cat[4]
if selx == 1:
    print("You've Chosen",sel1)
elif selx == 2:
    print("You've Chosen",sel2)
elif selx == 3:
    print("You've Chosen",sel3)
elif selx == 4:
    print("You've Chosen",sel4)
elif selx == 5:
    print("You've Chosen",sel5)
