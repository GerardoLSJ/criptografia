#!/usr/bin/env python
'''
@title: CRIPTOGRAFÍA. TAREA 9. RC4S
@authors: Luis Gerardo López S. Jiménez
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
        print("key:", [ hex(x) for x in self.key ])
        
    # Key-Scheduling Algorithm
    def KSA(self, key):
        keylength = len(key)
        # print("keylength",keylength, "veces", 256/keylength)
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
        k = []
        for i in range(0 ,len(s), 2):
            k.append(int(s[i]+s[i+1], 16))
        # print(k)
        return k

    #     return [ord(c) for c in s]
    #     key_in_hex = int(key,16)
    # for

    def run(self):
        result = ""
        S = self.KSA(self.key)
        S_hex = [ hex(x) for x in S ]
        print("S_HEX:",S_hex)
        keystream =  self.PRGA(S)

        # ENCRIPTAR
        if(self.action == 1):
            tmp_states = list()
            for c in self.message:
                current_state = next(keystream)
                tmp_states.append(current_state)  # CODE REQUIREMENT NOT FOR THE ALGORITHM 
                value = int(ord(c) ^ current_state)
                result += str(hex(value))
            # print("\nCIFRANDO")
            # print("ESTADO INICIAL: ", tmp_states[0])
            print("ESTADO FINAL: ", hex(tmp_states[len(tmp_states)-1]))
            return result

        # DESENCRIPTAR
        elif(self.action == 0):
            tmp_states = list()
            self.message = self.hex_to_bytes(self.message)
            for item in self.message:
                current_state = next(keystream)
                tmp_states.append(current_state)  # CODE REQUIREMENT NOT FOR THE ALGORITHM 
                value = int(int(item,16) ^ current_state)
                result += chr(value)
            print("\nDESCIFRANDO")
            # print("ESTADO INICIAL: ", tmp_states[0])
            # print("ESTADO FINAL: ", tmp_states[len(tmp_states)-1])
            # print("TODOS LOS ESTADOS: ", tmp_states)
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
    message = "Redes y Seguridad, Criptografía Aplicada a sistemas empotrados de la Facultad de Ingeniería"

    #key="EFDCAB8976452311"
    key="EFCDAB8967543201"
    
    print("-------------")
    print("\nMensaje a cifrar: " + message)
    encrypt = RC4(key, message,ENCRYPT)
    ciphered = encrypt.run()

    decrypt = RC4(key, ciphered,DECRYPT)
    deciphered = decrypt.run()
    
    print("\nCIFRADO: " + hex_mask(ciphered))
    print("\nDESCIFRADO: " + deciphered)
    print("-------------\n")

# import numpy as np
# import pandas as pd 

# print("TO EXCEL TABLE")
# x = np.array(
#     [13, 29, 106, 99, 253, 199, 240, 207, 254, 227, 97, 22, 27, 54, 94, 81, 80, 62, 250, 79, 151, 134, 179, 98, 45, 91, 83, 111, 200, 193, 35, 181, 168, 31, 37, 43, 58, 180, 84, 206, 137, 191, 148, 72, 201, 76, 140, 1, 217, 145, 178, 110, 204, 90, 96, 210, 104, 88, 17, 243, 75, 164, 133, 14, 223, 252, 71, 170, 100, 109, 87, 56, 11, 69, 9, 183, 92, 132, 16, 36, 23, 198, 135, 159, 105, 5, 78, 173, 251, 187, 123, 129, 50, 138, 49, 126, 205, 70, 242, 108, 157, 154, 101, 234, 68, 237, 53, 177, 18, 238, 146, 64, 21, 139, 42, 162, 112, 221, 30, 7, 103, 93, 95, 216, 212, 246, 115, 38, 192, 215, 244, 51, 142, 247, 12, 195, 197, 186, 214, 188, 122, 203, 44, 219, 196, 63, 73, 85, 48, 74, 147, 60, 202, 225, 113, 34, 150, 245, 182, 156, 169, 107, 144, 0, 184, 190, 59, 128, 232, 189, 175, 121, 120, 211, 40, 249, 167, 231, 131, 57, 20, 218, 224, 33, 220, 230, 15, 235, 3, 67, 32, 209, 119, 52, 65, 86, 185, 241, 208, 116, 55, 39, 239, 41, 213, 149, 163, 8, 46, 236, 66, 152, 10, 47, 194, 114, 171, 89, 102, 124, 26, 118, 158, 174, 233, 255, 141, 130, 172, 248, 228, 143, 25, 155, 6, 2, 166, 161, 28, 117, 125, 82, 4, 226, 153, 160, 176, 61, 165, 222, 19, 77, 24, 127, 229, 136]
# )
# reshape = np.reshape(x, (16, 16))
# pd.DataFrame(reshape).to_csv("file.csv")

