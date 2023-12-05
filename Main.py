# import modules
import AccountManager as am
import CryptographyManager as cm
from status import *
import Cryptography as cg

# Create an account from Account class
def CreateAccount (name,password):
    return am.CreateAccount(name,password)

# Login into an account from Account class
def LoginAccount (name,password):
    return am.LoginAccount(name,password)

# check login is True or False
def CheckStatus ():
    return am.CheckStatus()

def Encryptor (text,key):
    return cm.Encryptor(text, key)

def Decryptor (text,key):
    #if userAccount.LoginStatus == True:
    return cm.Decryptor(text, key)
