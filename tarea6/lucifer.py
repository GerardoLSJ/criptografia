

LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

def blockOperations(blocks, pi, shift):
    for block in blocks:
        block4 = [block[i:i+4] for i in range(0, len(block), 4)]
        tmp = shiftLetters(block4[0], shift)
        #tmp = permutateLetters(tmp, pi)


def shiftLetters(block4, shift):
    print("before",block4)
    newBlock4 = [0,0,0,0]
    for i, char in enumerate(block4):
        idx = LETTERS.find(char)
        idx = (idx + 1) % 27
        newBlock4[i] = LETTERS[idx]
    result = ''.join(newBlock4)
    print("after",result)
    return result

def permutateLetters(block4, pi):
    pass

def crossBlocks():
    pass

def lucifer_encrypt(text, pi, shift, times):
    block_size = 8
    mod = len(text) % block_size
    # completar con X si faltan letras en el bloque
    if(mod != 0):
        for i in range(0,block_size-mod):
            text+="X"

    blocks = [text[i:i+block_size] for i in range(0, len(text), block_size)]

    for i in range(0,times): # default times = 16
        blockOperations(blocks, pi, shift)



    return blocks

def lucifer_decrypt():
    pass


def main(): 
	# declaring text and key 
	text = 'AAAABBBBC'
	pi = [1,3,2,4]
	shift = 1

	# calling encryption function 
	lucifer_encrypted_text = lucifer_encrypt(text, pi, shift, 1) 

	print('Encrypted Text: {}'.format( lucifer_encrypted_text )) 

	# calling decryption function 
	#print('Decrypted Text: {}'.format( lucifer_decrypt(lucifer_encrypted_text, a, b) )) 


if __name__ == '__main__': 
	main() 