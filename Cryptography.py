import numpy as np
import random as rd
from math import fabs

# difination source array
# this array has 19 row and 5 column
# as a result 0-18 row and 0-4 column
Source_array = np.array([["a","b","c","d","e"],
                         ["f","g","h","i","j"],
                         ["k","l","m","n","o"],
                         ["p","q","r","s","t"],
                         ["u","v","w","x","y"],
                         ["z","A","B","C","D"],
                         ["E","F","G","H","I"],
                         ["J","K","L","M","N"],
                         ["O","P","Q","R","S"],
                         ["T","U","V","W","X"],
                         ["Y","Z","0","1","2"],
                         ["3","4","5","6","7"],
                         ["8","9","_",".","?"],
                         [" ","!","@","#","$"],
                         ["%","^","&","*","("],
                         [")","/","\\","|","~"],
                         ["`","+","-","=","<"],
                         [">","{","}","[","]"],
                         [":",";","\"","'",","]])

odd_x = [1,3,5,7,9,11,13,15,17]
even_x = [2,4,6,8,10,12,14,16,18]

odd_y = [1,3]
even_y = [2,4]


class Cryptography ():
    
    def __init__(self):
        pass

    # find character position in array 
    def PositionFinder(self,character):
        
        position = []
        position.append(np.where(Source_array == character)[0])
        position.append(np.where(Source_array == character)[1])
        
        # return list of x an y position
        return position 

    
    
    # find character by x an y in source array
    def CharacterFinder(self,x,y):
        return Source_array[x,y]
    
    
    
    # ------------------------------------------------------
    # encrypt
    # chice random row and column 
    # return [x,y]
    def RandomSelector(self): 
        
        # choice random row and column
        randomPosition_x = rd.randint(0,18)
        randomPosition_y = rd.randint(0,4)

        return randomPosition_x , randomPosition_y
    
    def Encryptor(self,letter):
        
        # call letter position
        letterPosition = self.PositionFinder(letter)

        # call Random selector
        encCharacterPosition_x , encCharacterPosition_y = self.RandomSelector()
        # create 2nd encrypted letter
        encCharacter = self.CharacterFinder(encCharacterPosition_x,encCharacterPosition_y)

        # find diffrent beetwen letter position and encrypted position
        diffrent_x = letterPosition[0] - encCharacterPosition_x
        diffrent_y = letterPosition[1] - encCharacterPosition_y

        # understand diffrents is possitive , negitive or zero
        if diffrent_x > 0 :
            changeCharacter_x = rd.choice(even_x)
        
        elif diffrent_x < 0 :
            changeCharacter_x = rd.choice(odd_x)
        
        elif diffrent_x == 0 :
            changeCharacter_x = 0
        
        if diffrent_y > 0 :
            changeCharacter_y = rd.choice(even_y)
        
        elif diffrent_y < 0 :
            changeCharacter_y = rd.choice(odd_y)
        
        elif diffrent_y == 0 :
            changeCharacter_y = 0
        
        # call character finder
        # create 1nd encrypted letter
        changeCharacter = self.CharacterFinder(changeCharacter_x,changeCharacter_y)
            
        # fabs to clear negitive values
        distanceCharacter_x = int(fabs(diffrent_x))
        distanceCharacter_y = int(fabs(diffrent_y))
        
        # create 3nd encrypted letter
        distanceCharacter = self.CharacterFinder(distanceCharacter_x,distanceCharacter_y)

        # create final word
        finalWord = str(changeCharacter) + encCharacter + distanceCharacter

        return finalWord
    
    def EncryptPrivateKey (self,private_key):
        
        finalkey = ""
        for letter in private_key :
            finalkey = finalkey + self.Encryptor(letter)
        
        return finalkey
    
    def MainEncryptor(self,message,private_key):

        lenPrivateKey = len(private_key)
        lenMessage = len(message)
        finalText = ""

        finalText = self.EncryptPrivateKey(private_key)
                
        # loop in message by letters
        for letter in message :
            finalText = finalText + self.Encryptor(letter)
        
        return finalText


    # -----------------------------------------------------------
    # decryptor
    
    def Decryptor(self,letter):
        
        # find 1nd , 2nd and 3nd position
        changeCharacter = self.PositionFinder(letter[0])
        encCharacter = self.PositionFinder(letter[1])
        distanceCharacter = self.PositionFinder(letter[2])

        # apply negitive or positive changes on final letter
        if changeCharacter[0] % 2 == 0:
            originCharacter_x = encCharacter[0] + distanceCharacter[0]
        
        elif changeCharacter[0] % 2 != 0:
            originCharacter_x = encCharacter[0] - distanceCharacter[0]

        if changeCharacter[1] % 2 == 0:
            originCharacter_y = encCharacter[1] + distanceCharacter[1]

        elif changeCharacter[1] % 2 != 0:
            originCharacter_y = encCharacter[1] - distanceCharacter[1]
        
        # find origin Character
        originCharacter = self.CharacterFinder(originCharacter_x,originCharacter_y)

        return originCharacter[0]


    def MainDecryptor(self,encryptedText,privateKey):

        # find key len
        lenKey = int(len(privateKey))
        lenKey = lenKey * 3
        
        lenCounter = 0
        counter = 0
        phrase = ""
        finalText = ""
        originalKey = ""

        if len(privateKey) > (len(encryptedText)-3) :
            return False

        # extract original key from text            
        for letter in encryptedText:

            if lenCounter == lenKey:  
                
                break
            
            # put encrypted letter into phrase
            phrase = phrase + letter
            lenCounter = lenCounter + 1
            counter = counter + 1
            
            if counter == 3:
            
                # call Decryptor 
                originalKey = originalKey + self.Decryptor(phrase)

                # clear key from text
                encryptedText = encryptedText[3:]

                # clear variable
                phrase = ""
                counter = 0
        
        if originalKey == privateKey :
            
            for letter in encryptedText:
            
                # put encrypted letter into phrase
                phrase = phrase + letter
                counter = counter + 1

                if counter == 3:

                    # call Decryptor 
                    finalText = finalText + self.Decryptor(phrase)

                    # clear variable
                    phrase = ""
                    counter = 0
        
            return finalText
        
        else:
            return False

        