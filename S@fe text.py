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


# this function premission to user to continu
def repeat_choice ():
    prev = input("Do you want to continu?(yes = y / no = n)")
    if prev.lower() == "y":
        choice = True
    else :
        choice = False
    return choice

# this function manage all procces
def Main_p():
    
    # set variable for while
    counter = 0
    
    # while for choice
    while counter < 1 :

        # insert user values
        raw_text = catch_values()


        # identify user text want to encrupt or decrypt
        if raw_text.startswith("ST") and raw_text.endswith("ST"):
            final_text = Main_decryptor(raw_text)


        else :
            # call encryptor function
            final_text = Main_encryptor(raw_text)  

            # show final text
            print(f"\nyour encrypted text is :\n{final_text}")
    
        # call choice function
        choice = repeat_choice()
        if choice == False :
            counter = counter + 1        


# this function manage all procces about encryptying 
def Main_encryptor (text):
    
    # set variables
    temp_text = ""
    final_letter = ""
    letter_1 = 0
    letter_4 = 0
    # navigation into the raw text
    for letter in text:
        
        # inform letter position (correct)
        letter_position = str(np.where(Source_matrix == letter))
        letter_position_x = int(letter_position[8])
        letter_position_y = int(letter_position[33])

        # set randomize number for crypted letter position(letter5) (correct)
        enc_position_x = rd.randint(0,10)
        enc_position_y = rd.randint(0,8)
        enc_letter = Source_matrix[enc_position_x,enc_position_y]

        
        # gain diffrence beetwen original letter and encrypted letter (indexes) (correct)
        # this is for specification changes
        diff_position_x = letter_position_x - enc_position_x
        diff_position_y = letter_position_y - enc_position_y
        
        # this is for final letters (letter 7 , 9)
        diff_position_final_x = int(math.fabs(letter_position_x - enc_position_x))
        diff_position_final_y = int(math.fabs(letter_position_y - enc_position_y))

        # specification the changes is positive , nagative or not changed in x and y indexes 
        # this is for x (letter 1) (correct)
        if diff_position_x < 0 :
            letter_1 = rd.choice(odd)

        if diff_position_x > 0 :
            letter_1 = rd.choice(even)
        
        if diff_position_x == 0 :
            letter_1 = 0
        
        # this is for y (letter 4) (correct)
        if diff_position_y < 0 :
            letter_4 = rd.choice(odd)

        if diff_position_y > 0 :
            letter_4 = rd.choice(even)
        
        if diff_position_y == 0 :
            letter_4 = 0

        
        # merge all of the encrypted letter and add 5 random letter to the final letter (correct)
        final_letter = str(rd.randint(0,9)) + str(letter_1) + str(rd.randint(0,9)) + str(rd.randint(0,9)) + str(letter_4) + str(enc_letter) + str(rd.randint(0,9)) + str(diff_position_final_x) + str(rd.randint(0,9)) + str(diff_position_final_y)

        # merge all letters together (correct)
        temp_text = temp_text + final_letter

    # add st mark into final text
    temp_text = "ST" + temp_text + "ST"

    return temp_text


# this function manage all procces about decrypting
def Main_decryptor (input_text):
    
    # remove St marks
    input_text = input_text[2:-2]
    
    count = 1
    final_text = ""
    
    # this variable for temp strings
    temp = ""
    
    for letter in input_text:
        
        # add encrypted letter into the temp
        temp = temp + letter
        count = count + 1
        
        # split 10 encrypted letter
        if count == 10 :
            
            # split encrypted letters from random letters 
            # random indexes : 0 , 2 , 3 , 6 , 8
            # true indexes : 1 , 4 , 5 , 7 , 9
            
            normal_encrypt_letters = temp[1] + temp[4] + temp[5] + temp[7] + temp[9]

            # explain indexes : 
            # 1 = diffrence change row is positive or negative 
            # 4 = diffrence change coulmn is positive or negative 
            # 5 = encrypted character
            # 7 = diffrence value for row
            # 9 = diffrence value for coulmn

            # diffrence change is positive or negative
            # for x
            diff_change_x = int(normal_encrypt_letters[0])

            # for y
            diff_change_y = int(normal_encrypt_letters[1])

            
            # find encrypte letter from text
            # find encrypt letter position in Source_matrix , and insert position into the variables
            encrypted_letter = normal_encrypt_letters[2]
            encrypted_letter_position_raw = str(np.where(Source_matrix == encrypted_letter))
            encrypted_letter_position_x = int(encrypted_letter_position_raw[8])
            encrypted_letter_position_y = int(encrypted_letter_position_raw[33])


            
            # diffrence position values
            # for x
            diff_position_x = int(normal_encrypt_letters[3])

            # for y
            diff_position_y = int(normal_encrypt_letters[4])

            
            # identify position is positive or negative
            # for x
            if diff_change_x == 0 :
                original_letter_position_x = encrypted_letter_position_x
            
            elif diff_change_x % 2 == 0 :
                original_letter_position_x = encrypted_letter_position_x + diff_position_x

            else :
                original_letter_position_x = encrypted_letter_position_x - diff_position_x


            # for y
            if diff_change_y == 0 :
                original_letter_position_y = encrypted_letter_position_y
            
            elif diff_change_y % 2 == 0 :
                original_letter_position_y = encrypted_letter_position_y + diff_position_x

            else :
                original_letter_position_y = encrypted_letter_position_y - diff_position_y

            # find original character
            original_letter = Source_matrix[original_letter_position_x , original_letter_position_y]

            final_text = final_text + original_letter
            
            temp = ""
            count = 0


# call Main function
Main_p()