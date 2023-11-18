import numpy as np
import random as rd
import datetime as dt
import math
import os


# Create source matrix
# 11 row and 9 coulmn (index_x = 0 - 10 , index_y = 0 - 8)
# Decryptor and encryptor both of them use this matrix

Source_matrix = np.array([["a","b","c","d","e","f","g","h","i"],
                          ["j","k","l","m","n","o","p","q","r"],
                          ["s","t","u","v","w","x","y","z","A"],
                          ["B","C","D","E","F","G","H","I","J"],
                          ["K","L","M","N","O","P","Q","R","S"],
                          ["T","U","V","W","X","Y","Z","0","1"],
                          ["2","3","4","5","6","7","8","9","_"],
                          [".","?"," ","!","@","#","$","%","^"],
                          ["&","*","(",")","/","\\","|","~","`"],
                          ["+","-","=","<",">","{","}","[","]"],
                          [":",";","\"","'",",","","","",""],])


# set odd & even numbers
odd = [1,3,5,7,9]
even = [2,4,6,8]


# Welcome message
print("Welcome to the S@fe text encryptor\nThis program encrypt your message")


# this function catch raw text from user and return it
def catch_values ():
    raw_text = input("Enter your message : \t")
    return raw_text


# this function manage all procces
def Main ():
    
    # insert user values
    raw_text = catch_values()
    
    
    # identify user text want to encrupt or decrypt
    if raw_text.startswith("ST") and raw_text.endswith("ST"):
        Main_decryptor()
    
    
    else :
        Main_encryptor(raw_text)
        


# this function manage all procces about encryptying 
def Main_encryptor (text):
    
    # set variables
    final_text = ""

    # navigation into the raw text
    for letter in text:
        
        # inform letter position
        letter_position = str(np.where(Source_matrix == letter))
        letter_position_x = letter_position[8]
        letter_position_y = letter_position[33]

        # set randomize number for crypted letter position
        enc_position_x = rd.randint(0,10)
        enc_position_y = rd.randint(0,8)
        enc_letter = Source_matrix[x,y]







# this function manage all procces about decrypting
def Main_decryptor ():
    pass

