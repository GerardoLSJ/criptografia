import numpy as np 
from sympy import Matrix

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
            keyMatrix[i][j] = ord(key[k]) % 65
            k += 1
    return keyMatrix
  
# Following function encrypts the message 
def encrypt(messageVector): 
    cipherMatrix = (Matrix(keyMatrix) * Matrix(messageVector)) % 26
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
    int_message = [ord(x) for x in message]
    #print(int_message)
    aux = np.array(int_message, dtype=int)
    messageVector = np.reshape(aux,(3,-1)) % 65
        #print(messageVector)

    mensaje_cifrado = encrypt(messageVector) 
    # print("cipherMatrix",mensaje_cifrado)
  
    # Generar texto desde la matriz
    CipherText = [] 
    mensaje_cifrado = np.array(mensaje_cifrado, dtype=int)
    # print("numpy", mensaje_cifrado)
    flat = mensaje_cifrado.flatten()
    for i in range(len(flat)): 
        CipherText.append(chr(flat[i] + 65)) 

    return {
        "mensaje": "".join(CipherText),
        "cifrado": mensaje_cifrado
    }
  

def HillDecipher(data, key):
    mat = Matrix(keyMatrix) # keyMatrix is your basic matrix ndrarray format
    inv = mat.inv_mod(26) #or any modulo you want
    res = np.dot(inv, data["cifrado"]) % 26
    flat = res.flatten()
    #print("res",flat)
    DecipherText = [] 
    for i in range(len(flat)): 
        DecipherText.append(chr(flat[i] + 65)) 
  
    return {
        "mensaje": "".join(DecipherText),
    }

# Driver Code 

# Get the message to  
# be encrypted 
mensaje = "PORMIRAZAHABLARAELESPIRITU"

# Get the key 
key = "GYBNQKURP"
print("mensaje",mensaje)
data = HillCipher(mensaje, key) 
print("cifrado",data["mensaje"])
descifrado = HillDecipher(data, key)
print(descifrado)
# descifrado = getKeyMatrix()