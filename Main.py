# import modules
import status as st
import Cryptography as cg

def CreateAccount (name,password):
    
    # create object from Account class
    userAccount = st.Account()
    return userAccount.CreateAccount(name,password)

    