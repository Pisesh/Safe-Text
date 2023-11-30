import csv
import KeyGenrator as kg

# create Account class
class Account ():
    def __init__(self):
        
        # definitation login is true or false
        self._isLogin = False
        


    # check user is login or no
    def LoginStatus(self):
        return self._isLogin
    
    # create account for user
    def CreateAccount(self,name,password):

        self.name = name
        self.__password = password

        # create object from key class
        publicKey = kg.Key()

        # call CreatePublickey from Key class
        self.__publicKey = publicKey.CreatePublicKey()

        with open ('accounts.csv',mode='w') as acc :
            account_writer = csv.writer(acc)
            
            account_writer.writerow([self.name,self.__publicKey,self.__password])