from end import encpassword(pass)

import pymysql
import pandas
import sqlalchemy
#import clipboard

engine = sqlalchemy.create_engine('mysql+pymysql://root:A18saiapartment@localhost:3306/passwords')

def create(appname,username,password,email):
    appname = input("Please enter the name of the application: ")
    username = input("Please enter your username for the above site: ")
    password = input("Please enter the password for the above site: ")
    email = input("Enter the email you have registered with: ")
    encpw,key = encpassword(password)
 #   clipboard.copy(password)

    print("Your password has been saved and copied to the clipboard")

    df1 = pandas.read_sql_query('Insert into information values(appname,username,password,email,key)')

def find(appname):
    appname = input("Please enter the name of the app for whose password you are searching: ")
    df2 = pandas.read_sql_query('select*from information where Application > %s %(appname,)')

def find(username):
    username = input("Please enter the username for whose password you are searching: ")
    df3 = pandas.read_sql_query('select*from information where Application > %s %(username,)')

   