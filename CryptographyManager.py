import Cryptography as cg

def Encryptor (text,key):

        if text != "" and key != "":
            encrypt = cg.Cryptography()
            return encrypt.MainEncryptor(text,key)
        
        else:
            return None

def Decryptor (text,key):

        if text != "" and key != "":
            decrypt = cg.Cryptography()
            return decrypt.MainDecryptor(text,key)
    
        else:
            return None
            