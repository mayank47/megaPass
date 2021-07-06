from cryptography.fernet import Fernet

def encPassword(passw):
    key = Fernet.generate_key()
    fernet = Fernet(key)
    return fernet.encrypt(passw.encode()).decode(),key.decode()


def decryptPassword(encpassw,key):
    fernet = Fernet(key)
    return fernet.decrypt(encpassw).decode()