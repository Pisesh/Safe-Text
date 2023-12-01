# import modules
from status import *
import Cryptography as cg

# create object from Account class
userAccount = Account()

# Create an account from Account class
def CreateAccount (name,password):
    
    # filter Null values
    if name == "" or password == "":
        return 1
    
    else :
        return userAccount.CreateAccount(name,password)

# Login into an account from Account class
def LoginAccount (name,password):

    # filter Null values
    if name == "" or password == "" :
        return 1
    
    else :
        return userAccount.LoginAccount(name,password)

# check login is True or False
def CheckStatus ():
    return userAccount.LoginStatus()

def Encryptor (text,key):
    if userAccount.LoginStatus() == True:
        encrypt = cg.Cryptography()
        return encrypt.MainEncryptor(text,key)
    
    else:
        return None

def Decryptor (text,key):
    if userAccount.LoginStatus == True:
        decrypt = cg.Cryptography()
        return decrypt.MainDecryptor(text,key)
    
    else:
        return None