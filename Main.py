# import modules
from status import *
import Cryptography as cg

# create object from Account class
userAccount = Account()

def CreateAccount (name,password):
    
    # filter Null values
    if name == "" or password == "":
        return 1
    
    else :
        return userAccount.CreateAccount(name,password)

def LoginAccount (name,password):

    # filter Null values
    if name == "" or password == "" :
        return 1
    
    else :
        return userAccount.LoginAccount(name,password)

def CheckStatus ():
    return userAccount.LoginStatus()