#!/usr/bin/env python
'''
@title: CRIPTOGRAFÍA. TAREA 9. RC4S
@authors: Luis Gerardo López S. Jiménez, Marco A. Moreno Guerra
@date_creation: 27/03/2020
@date_last_update: 27/03/2020
@comments: 
    RC4 code implementation
	This code requires python 3 to be execute.
'''

class RC4():
    def __init__(self, key, message, action):
        self.key = self.text_to_bytes(key)
        self.message = message
        self.action = action

    # Key-Scheduling Algorithm
    def KSA(self, key):
        keylength = len(key)
        S = [x for x in range(256)]
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % keylength]) % 256
            S[i], S[j] = S[j], S[i]  # swap
        return S

    # Pseudo random generation algorithm (Stream Generation):
    def PRGA(self, S):
        i = 0
        j = 0
        while True:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]  # swap
            K = S[(S[i] + S[j]) % 256]
            yield K

    def hex_to_bytes(self, hexStr):
        nums_lst = hexStr.split("0x")
        nums_lst.pop(0)

        return nums_lst

    def text_to_bytes(self,s):
        return [ord(c) for c in s]
    

    def run(self):
        result = ""
        S = self.KSA(self.key)
        keystream =  self.PRGA(S)

        # ENCRIPTAR
        if(self.action == 1):
            in_hex = list()
            for c in self.message:
                value = int(ord(c) ^ next(keystream))
                in_hex.append(value)
                result += str(hex(value))
            return result

        # DESENCRIPTAR
        elif(self.action == 0):
            in_hex = list()
            self.message = self.hex_to_bytes(self.message)
            #print("DES",self.message)
            for item in self.message:
                in_hex.append(int(item,16))
                value = int(int(item,16) ^ next(keystream))
                result += chr(value)
            return result




    # if __name__ == '__main__':
    #     # test vectors are from http://en.wikipedia.org/wiki/RC4

    #     # ciphertext should be BBF316E8D940AF0AD3
    #     key = 'Key'
    #     plaintext = 'Plaintext'

    #     # ciphertext should be 1021BF0420
    #     #key = 'Wiki'
    #     #plaintext = 'pedia'

    #     # ciphertext should be 45A01F645FC35B383552544B9BF5
    #     #key = 'Secret'
    #     #plaintext = 'Attack at dawn'


def hex_mask(text):
    new_str = text.replace("0x","")
    return new_str.upper()


if __name__ == '__main__':
    ENCRYPT=1
    DECRYPT=0
    #key = 'Wiki'
    #message = 'pedia'
    message = "POR MI RAZA HABLARA EL ESPIRITU"
    key = "EFCDAB8967543201"
    print("\nMensaje a cifrar: " + message)
    encrypt = RC4(key,message,ENCRYPT)
    ciphered = encrypt.run()

    decrypt = RC4(key,ciphered,DECRYPT)
    deciphered = decrypt.run()
    
    print("\nCIFRADO: " + hex_mask(ciphered))
    print("\nDESCIFRADO: " + deciphered)
    print("")
