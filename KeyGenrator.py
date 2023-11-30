import random as rd


class Key ():
    def __init__ (self):
        self.__publicKey = 0
        self.__privateKey = 0

    # create public key
    def CreatePublicKey (self):
        self.__publicKey = rd.randint(100000000000,999999999999)
        return self.__publicKey