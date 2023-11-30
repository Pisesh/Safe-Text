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
    def CreateAccount(self,username,password):

        self.username = username
        self.__password = password

        # create object from key class
        publicKey = kg.Key()

        # call CreatePublickey from Key class
        self.__publicKey = publicKey.CreatePublicKey()

        self.SaveAccount()

     # save account   
    def SaveAccount(self):    
    
        with open ('accounts.csv',mode='w') as account_file :
            account_writer = csv.writer(account_file)
            
            account_writer.writerow([self.username,self.__publicKey,self.__password])
    
    def LoginAccount(self,username,password):
        
        # import csv file
        account_file = csv.reader(open='accounts.csv')

        # extract csv row
        for row in account_file:
            extractList = row

        # extract usrname and password from csv list
        realUsername = extractList[0]
        realPassword = extractList[2]

        # put parameters into variable
        parameterUsename = username
        parameterPassword = password

        


