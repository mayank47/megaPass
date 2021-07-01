import pymysql as sqltor
from getpass import getpass

def insertPassword(appName,encPass,key,userEmail,userName,url):
    try:
        dbPass = getpass("Enter Password for connecting to the database: ")
        db = sqltor.connect(host="localhost", user="root", password=dbPass, database='megapass')
        cursor = db.cursor()
        insertQuery = "INSERT INTO accounts(appName,encPass,dkey,userEmail,userName,url) VALUES('{}','{}','{}','{}','{}','{}')".format(appName,encPass,key,userEmail,userName,url)
        cursor.execute(insertQuery)
        db.commit()
        print("Added")
        
    except:
        print("Error")


def findPassword(appName):
    try:
        dbPass = getpass("Enter Password for connecting to the database: ")
        db = sqltor.connect(host="localhost", user="root", password=dbPass, database='megapass')
        cursor = db.cursor()
        selectQuery = "SELECT encPass,dkey from accounts WHERE appName = '{}'".format(appName)
        cursor.execute(selectQuery)
        data = cursor.fetchall() #((encpass,key,))
        return data[0][0].encode(),data[0][1].encode()
        db.close()
        
    except:
        print("Error")