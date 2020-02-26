
from collections import OrderedDict 

def removeDupWithOrder(str): 
    return "".join(OrderedDict.fromkeys(str)) 

def KeyCaesar(text,key,op): 
    """
    op: 0 = CIFRAR
    op: 1 = DESCIFRAR
    """
    LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    LETTERS_KEY = removeDupWithOrder(key+LETTERS)
    result = "" 
    # Recorrer texto
    for i in range(len(text)): 
        char = text[i] 
        if (op == 0): 
            pos = LETTERS.find(char)
            result += LETTERS_KEY[pos]
        elif(op == 1):
            pos = LETTERS_KEY.find(char)
            result += LETTERS[pos]

    return result 
  
#Prueba
mensaje = "ABCDXYZ"
key = "ZZZRRFG"
print("Mensaje  : " + mensaje )
cifrado = KeyCaesar(mensaje,key,0)
print("Cifrado: " + cifrado )
print("Descifrado: " + KeyCaesar(cifrado,key,1) )
