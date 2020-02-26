import numpy as np 
from sympy import Matrix

keyMatrix = [[0] * 3 for i in range(3)] 
  
# Generate vector for the message 
messageVector = [[0] for i in range(3)] 
  
# Generate vector for the cipher 
cipherMatrix = [[0] for i in range(3)] 
  
# Following function generates the 
# key matrix for the key string 
def getKeyMatrix(key): 
    k = 0
    for i in range(3): 
        for j in range(3): 
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    # return keyMatrix
  
# Following function encrypts the message 
def encrypt(messageVector): 
    for i in range(3): 
        for j in range(1): 
            cipherMatrix[i][j] = 0
            for x in range(3): 
                cipherMatrix[i][j] += (keyMatrix[i][x] * 
                                       messageVector[x][j]) 
            cipherMatrix[i][j] = cipherMatrix[i][j] % 26
  
def HillCipher(message, key): 
  
    # Get key matrix from the key string 
    getKeyMatrix(key) 
  
    # Generate vector for the message 
    for i in range(3): 
        messageVector[i][0] = ord(message[i]) % 65
  
    # Following function generates 
    # the encrypted vector 
    encrypt(messageVector) 
  
    # Generate the encrypted text  
    # from the encrypted vector 
    CipherText = [] 
    for i in range(3): 
        CipherText.append(chr(cipherMatrix[i][0] + 65)) 
  
    # Finally print the ciphertext 
    # print("Ciphertext: ", "".join(CipherText)) 
    return "".join(CipherText)
  

def HillDecipher(key):
    mat = Matrix(keyMatrix) # keyMatrix is your basic matrix ndrarray format
    inv = mat.inv_mod(26) #or any modulo you want

    print(cipherMatrix)
    res = np.dot(inv, cipherMatrix) 
    print(res)
    DecipherText = [] 
    for i in range(3): 
        DecipherText.append(chr(res[i][0]%26 + 65)) 
  
    return "".join(DecipherText)

# Driver Code 

# Get the message to  
# be encrypted 
mensaje = "ACT"

# Get the key 
key = "GYBNQKURP"
print("mensaje",mensaje)
cifrado = HillCipher(mensaje, key) 
print("cifrado",cifrado)

print(HillDecipher(key))
# descifrado = getKeyMatrix()