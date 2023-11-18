import numpy as np
import random as rd
import datetime as dt
import os


# Create source matrix
# 11 row and 9 coulmn
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

print("Welcome to the S@fe text encryptor\nThis program encrypt your message")

# this function catch raw text from user and return it
def catch_values ():
    raw_text = input("Enter your message : \t")
    return raw_text

