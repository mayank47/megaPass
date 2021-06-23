from menu import menu,create,findAccount
secret = "password"
passw = input('Please Provide Password: ')

if passw == secret:
    print("You're in")

else: 
    print("Incorrect Pasword")
    
    
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
        
