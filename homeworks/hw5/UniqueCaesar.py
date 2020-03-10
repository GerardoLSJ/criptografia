

def UniqueCaesar(text,key,op): 
    """
    op: 0 = CIFRAR
    op: 1 = DESCIFRAR
    """
    LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    result = "" 
    # Recorrer texto
    for i in range(len(text)): 
        char = text[i] 
        if (op == 0): 
            pos = LETTERS.find(char)
            pos += LETTERS.find(key[i]) # posicion de llave
            if(pos >= 27):
                pos = pos % 27
            result += LETTERS[pos]
        elif(op == 1):
            pos = LETTERS.find(char)
            pos -= LETTERS.find(key[i]) # posicion de llave
            if(pos <= 0):
                pos = pos % 27
            result += LETTERS[pos]

    return result 
  
#Prueba
mensaje = "AHOLADOTZ"
key = "AGERARDOZ"
print("Mensaje  : " + mensaje )
cifrado = UniqueCaesar(mensaje,key,0)
print("Cifrado: " + cifrado )
print("Descifrado: " + UniqueCaesar(cifrado,key,1) )
