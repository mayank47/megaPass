from menu import menu,create,findAccount,find
from getpass import getpass

secret = "password"
passw = getpass('Please Provide Password: ')

if passw == secret:
    print("You're in")
    
else:
    print("Incorrect Password")
    
    
choice = menu()

while choice.upper() != "Q":
    if choice == "1":
        create()
        choice = menu()
    elif choice == "2":
        findAccount()
        choice = menu()
    elif choice == "3":
        find()
        choice = menu()
    else :
        choice = menu()