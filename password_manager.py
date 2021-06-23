from menu import menu,create,findAccount
secret = "password"
passw = input('Please Provide Password: ')

if passw == secret:
    print("You're in")

else: 
    print("Incorrect Pasword")
    
    
choice = menu() 

while choice != "Q":
    if choice == "1":
        create()
    elif choice == "2":
        findAccount()
    elif choice == "3":
        find()
    else :
        choice = menu()
        
