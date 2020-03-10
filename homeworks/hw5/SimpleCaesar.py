
def SimpleCaesar(text,op): 
    """
    op: 0 = CIFRAR
    op: 1 = DESCIFRAR
    """
    LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
    result = "" 
    # Recorrer texto
    for i in range(len(text)): 
        char = text[i] 
        pos = LETTERS.find(char)
        if (op == 0): 
            pos += 3
            if(pos >= 27):
                pos = pos % 27
            result += LETTERS[pos]
        elif(op == 1):
            pos -= 3
            if(pos <= 0):
                pos = pos % 27
            result += LETTERS[pos]
  
    return result 
  
#Prueba
mensaje = "ABCDXYZ"
print("Mensaje  : " + mensaje )
cifrado = SimpleCaesar(mensaje,0)
print("Cifrado: " + cifrado )
print("Descifrado: " + SimpleCaesar(cifrado,1) )
