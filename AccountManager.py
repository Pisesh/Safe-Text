from status import *

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