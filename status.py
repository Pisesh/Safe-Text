import csv
import KeyGenrator as kg

# create Account class
class Account ():
    def __init__(self):
        
        # definitation login is true or false
        self.__isLogin = False
        
    # check user is login or no
    def LoginStatus(self):
        return self.__isLogin
    
    # create account for user
    def CreateAccount(self,username,password):

        self.username = username
        self.__password = password

        # create object from key class
        publicKey = kg.Key()

        # call CreatePublickey from Key class
        self.__publicKey = publicKey.CreatePublicKey()

        return self.SaveAccount()


     # save account   
    def SaveAccount(self):    
    
        with open ('accounts.csv',mode='w') as account_file :
            account_writer = csv.writer(account_file)
            
            account_writer.writerow([self.username,self.__publicKey,self.__password])
            return True
    
    def LoginAccount(self,username,password):
        
        # import csv file
        account_file = csv.reader(open='accounts.csv')

        # extract csv row
        for row in account_file:
            extractList = row

        # extract usrname and password from csv list
        self.__realUsername = extractList[0]
        self.__realPassword = extractList[2]

        # put parameters into variable
        self.parameterUsename = username
        self.parameterPassword = password

        # set login true
        self.__isLogin = True
        return AccountValidation()

    def AccountValidation (self):        
        
        # check user name and password
        if self.__realUsername == self.parameterUsename:
        
            if self.__realPassword == self.parameterPassword:
                return True

        else:
            return False


