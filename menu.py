from getpass import getpass
import clipboard
from end import encPassword,decryptPassword
from db_manager import insertPassword,fetchDetails,findPassword

def menu():
    print("-"*30)
    print(("-"*13) +"Menu"+ ("-" *13))
    print("1. Create new password")
    print("2. Find apps connected to an email")
    print("3. Find a password for an app")
    print("Q. Exit")
    print("-"*30)
    return input(": ")


def create():
    print("Please proivide the name of the app:")
    appName = input()
    print("")
    passw = getpass("Please provide a password for this app: ")
    print("")
    encPass,key = encPassword(passw)
    clipboard.copy(passw)
    print("-"*30)
    print("")
    print("Your password has now been created")
    print("")
    print("-" *30)
    userEmail = input("Please provide an email for this app: ")
    userName = input("Please provide an username for this app: ")
    url = input("Please paste the url to the app: ")
    insertPassword(appName,encPass,key,userEmail,userName,url)
    

def findAccount():
    print("Please provide the email that you want to find apps for: ")
    userEmail = input()
    fetchDetails(userEmail)
    



def find():
    print("Please proivide the name of the app:")
    appName = input()
    encPass,key = findPassword(appName)
    clipboard.copy(decryptPassword(encPass,key))
    print("")
    print("-"*41)
    print("")
    print("Your password is copied to your clipboard")
    print("")
    print("-" *41)
    print("")
    
    
    
    
    
    
    
    
    
    
    
    