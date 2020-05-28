import numpy as np 
from sympy import Matrix

LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
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
            keyMatrix[i][j] = LETTERS.find(key[k])
            k += 1
    return keyMatrix
  
# Following function encrypts the message 
def encrypt(messageVector): 
    cipherMatrix = (Matrix(keyMatrix) * Matrix(messageVector)) % 37
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
    int_message = [LETTERS.find(x) for x in message] # ord
    aux = np.array(int_message, dtype=int)
    messageVector = np.reshape(aux,(3,-1)) # % 65
    mensaje_cifrado = encrypt(messageVector) 
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
    mat = Matrix(keyMatrix)
    print("DESCIFRADO:")
    print("key matrix:",mat)
    print("adjunta:",mat.adjugate() % 37)
    inv = mat.inv_mod(37) # cualquier modulo
    print("INVERSA: ", inv)
    res = np.dot(inv, data["cifrado"]) % 37
    flat = res.flatten()
    #print("res",flat)
    DecipherText = [] 
    for i in range(len(flat)): 
        DecipherText.append(LETTERS[flat[i]]) 
  
    return {
        "mensaje": "".join(DecipherText),
    }

#mensaje a encriptar
mensaje = "LOJL970403FR"
print("longitud: ", len(mensaje))
# Get the key 
key = "ALEXPECKS"
print("\nMENSAJE DE ENTRADA: \t\t",mensaje)
data = HillCipher(mensaje, key) 
print("\nCIFRADO: \t\t\t",data["mensaje"])
descifrado = HillDecipher(data, key)
print("\nMENSAJE DE DESCIFRADO: \t\t", descifrado["mensaje"])
# descifrado = getKeyMatrix()

M = [24, 25, 15, 3, 6, 2,29, 2, 13]
for x in M:
    print( LETTERS[x])

X
Y
O

D
G
C

2
C
N