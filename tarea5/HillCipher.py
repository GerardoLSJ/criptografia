import numpy as np 
from sympy import Matrix

"""
USING ASCII
"""


LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Llave 
keyMatrix = [[0] * 3 for i in range(3)] 
  
# Mensaje
messageVector = [[0] for i in range(3)] 
  
# Mensaje cifrado
cipherMatrix = [] # [[0] for i in range(3)] 
  
# GENERA LA MATRIZ LLAVE
def getKeyMatrix(key): 
    k = 0
    for i in range(3): 
        for j in range(3): 
            keyMatrix[i][j] = LETTERS.find(key[k]) #ord(key[k]) % 65
            k += 1
    return keyMatrix
  
# Following function encrypts the message 
def encrypt(messageVector): 
    cipherMatrix = (Matrix(keyMatrix) * Matrix(messageVector)) % 27
    return cipherMatrix.tolist()

def HillCipher(message, key): 
  
    # GENERA  LA MATRIZ LLAVE GLOBAL 
    keyMatrix = getKeyMatrix(key) 
    #print(keyMatrix)
    # Generate vector for the message 

    if(len(message) % 3 != 0):
        message += "X"
        if(len(message) % 3 != 0):
            message += "X"

    message = list(message)
    #print(message)
    int_message = [LETTERS.find(x) for x in message] # ord
    #print(int_message)
    aux = np.array(int_message, dtype=int)
    messageVector = np.reshape(aux,(3,-1)) # % 65
        #print(messageVector)

    mensaje_cifrado = encrypt(messageVector) 
    # print("cipherMatrix",mensaje_cifrado)
  
    # Generar texto desde la matriz
    CipherText = [] 
    mensaje_cifrado = np.array(mensaje_cifrado, dtype=int)
    # print("numpy", mensaje_cifrado)
    flat = mensaje_cifrado.flatten()
    for i in range(len(flat)): 
        CipherText.append(LETTERS[flat[i]])

    return {
        "mensaje": "".join(CipherText),
        "cifrado": mensaje_cifrado
    }
  

def HillDecipher(data, key):
    mat = Matrix(keyMatrix) # keyMatrix is your basic matrix ndrarray format
    inv = mat.inv_mod(27) #or any modulo you want
    res = np.dot(inv, data["cifrado"]) % 27
    flat = res.flatten()
    #print("res",flat)
    DecipherText = [] 
    for i in range(len(flat)): 
        DecipherText.append(LETTERS[flat[i]]) 
  
    return {
        "mensaje": "".join(DecipherText),
    }

# Driver Code 

# Get the message to  
# be encrypted 
mensaje = "SANTIBAÑEZPORMIRAZAHABLARAELESPIRITU"

# Get the key 
key = "GYBNQKURP"
print("\nMENSAJE DE ENTRADA: \t\t",mensaje)
data = HillCipher(mensaje, key) 
print("\nCIFRADO: \t\t\t",data["mensaje"])
descifrado = HillDecipher(data, key)
print("\nMENSAJE DE DESCIFRADO: \t\t", descifrado["mensaje"])
# descifrado = getKeyMatrix()