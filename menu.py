from getpass import getpass
import clipboard
from end import encPassword,decryptPassword
from db_manager import insertPassword,findPassword

def menu():
    print("-"*30)
    print(("-"*13) +"Menu"+ ("-" *13))
    print("1. Create new password")
    print("2. Find all sites and apps connected to an email")
    print("3. Find a password for a site or app")
    print("Q. Exit")
    print("-"*30)
    return input(": ")


def create():
    print("Please proivide the name of the site you want to generate a password for")
    appName = input()
    print("")
    passw = getpass("Please provide a password for this site: ")
    print("")
    encPass,key = encPassword(passw)
    clipboard.copy(passw)
    print("-"*30)
    print("")
    print("Your password has now been created and copied to your clipboard")
    print("")
    print("-" *30)
    userEmail = input("Please provide a user email for this app or site: ")
    userName = input("Please provide a username for this app or site : ")
    if userName == None:
        userName = ""
    url = input("Please paste the url to the site that you are creating the password for: ")
    insertPassword(appName,encPass,key,userEmail,userName,url)
    

def findAccount(): #sql select userEmail,appName,userName,url from accounts where userEmail = "xyz";
    print("Please provide the email that you want to find account for:  ")
    userEmail = input()
   


def find():
    print("Please proivide the name of the site or app you want to find the password for")
    appName = input()
    encPass,key = findPassword(appName)
    clipboard.copy(decryptPassword(encPass,key))
    print("-"*30)
    print("")
    print("Your password is copied to your clipboard")
    print("")
    print("-" *30)
    print("")
    
    
    
    
    
    
    
    
    
    
    
    