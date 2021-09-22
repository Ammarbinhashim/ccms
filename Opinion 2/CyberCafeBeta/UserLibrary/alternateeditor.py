import mainmenu
from mainmenu import *
def runmenu(username,userage,email,phone):
    username = input("Enter FullName:")
    userage = input("Enter age:")
    emailid = input("Enter Email ID:")
    print("format: (localpart)@(domain).com",end=" ")
    localpart = input("Enter Local Part:")
    domain = input("Enter a valid domain:")
    email = localpart+"@"+domain+".com"
    phone = input("Enter phone number:")
    phonedigit = range(11)
    if phone not in phonedigit:
        print("Please enter a valid Phone Number:")
    else:
        print(phone)
        return

runmenu()
