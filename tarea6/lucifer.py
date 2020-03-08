'''
@title: CRIPTOGRAFÍA. TAREA 6. ALGORITMO DE CIFRADO Y DESCIFRADO LUCIFFER
@authors: Luis Gerardo López S. Jiménez, Marco A. Moreno Guerra
@date_creation: 06/03/2020
@date_last_update: 08/03/2020
'''

# Global variable of the alphabet universe
LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Functions
def blockOperations(blocks, permute_order, shift):
	final_result = []
	for block in blocks:
		block4 = [block[i:i+4] for i in range(0, len(block), 4)]
		# Takes only left 4 char block
		tmp = shiftLetters(block4[0], shift)
		tmp = permutateLetters(tmp, permute_order)
		final_result.append(crossBlocks(tmp, block4[1]))
		print('PARTIAL RESULT: {}'.format(final_result))
	return ''.join(final_result)

def shiftLetters(block4, shift):
	print("Before shift: ",block4)
	newBlock4 = [0,0,0,0]
	for i, char in enumerate(block4):
		idx = LETTERS.find(char)
		idx = (idx + 1) % 27
		newBlock4[i] = LETTERS[idx]
	result = ''.join(newBlock4)
	print("After shift: ",result)
	return result

def permutateLetters(block4, permute_order):
	print('Before permutate: {}'.format(block4))
	newBlock4 = [0,0,0,0]
	for i, char in enumerate(block4):
		newBlock4[i] = block4[permute_order[i]-1]
		# 4213
	result = ''.join(newBlock4)
	print('After permutate: {}'.format(result))
	return result

def crossBlocks(left_block, right_block):
	return right_block + left_block

def lucifer_encrypt(text, permute_order, shift, times = 4): # default times = 4
	block_size = 8
	mod = len(text) % block_size
	# completar con caracter X si faltan letras en el bloque
	if(mod != 0):
		for i in range(0,block_size-mod):
			text += "X"

	blocks = text

	for i in range(0, times):
		print('\nROUND {}:'.format(i + 1))
		blocks = [blocks[i:i+block_size] for i in range(0, len(blocks), block_size)]
		blocks = blockOperations(blocks, permute_order, shift)

	return blocks

def lucifer_decrypt():
	pass

def main(): 
	# declaring text and key 
	plain_text = 'MORENOGUERRALOPEZSANTIBAÑEZ'
	permute_order = [4, 2, 1, 3]
	shift = 1
	rounds = 4

	# calling encryption function 
	lucifer_encrypted_text = lucifer_encrypt(plain_text, permute_order, shift, rounds) 

	print('Plaint text: {}'.format(plain_text))
	print('Encrypted text: {}'.format(lucifer_encrypted_text)) 

	# calling decryption function 
	#print('Decrypted Text: {}'.format( lucifer_decrypt(lucifer_encrypted_text, a, b) )) 


# Code execution
if __name__ == '__main__': 
	main() 