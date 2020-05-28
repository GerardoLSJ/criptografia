'''
@title: CRIPTOGRAFÍA. TAREA 6. ALGORITMO DE CIFRADO Y DESCIFRADO LUCIFFER
@authors: Luis Gerardo López S. Jiménez, Marco A. Moreno Guerra
@date_creation: 06/03/2020
@date_last_update: 09/03/2020
@comments: 
	This code requires python 3 to be execute.
	To get more detailed process' information, uncomment print lines: 32, 36, 46, 50, 55, 71, 81.
	There are some global constants at the beginning that facilite the change of values.
'''

# Global variables
LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
PLAIN_TEXT = 'LOPEZSANTIBAÑEZJIMENEZLU'
BLOCK_SIZE = 8
ROUNDS = 16
SHIFT = 1


# Functions
def blockOperations(blocks, permute_order, shift, process = 'encryption'):
	final_result = []
	for block in blocks:
		block4 = [block[i:i+4] for i in range(0, len(block), 4)]
		if (process == 'encryption'):
			partial_result1 = shiftLetters(block4[0], shift, process)
			partial_result1 = permuteLetters(partial_result1, permute_order)
			final_result.append(crossBlocks(partial_result1, block4[1]))
		else:
			partial_result1 = crossBlocks(block4[0], block4[1])
			partial_result2 = permuteLetters(partial_result1[0:4], permute_order)
			final_result.append(shiftLetters(partial_result2, shift, process) + partial_result1[4:8])
		#print('PARTIAL RESULT: {}'.format(final_result))
	return ''.join(final_result)

def shiftLetters(block4, shift, operation = 'encryption'):
	#print("Before shift: ",block4)
	newBlock4 = [0, 0, 0, 0]
	for i, char in enumerate(block4):
		idx = LETTERS.find(char)
		if (operation == 'encryption'):
			idx = (idx + shift) % 27
		else:
			idx = (idx - shift) % 27
		newBlock4[i] = LETTERS[idx]
	result = ''.join(newBlock4)
	#print("After shift: ",result)
	return result

def permuteLetters(block4, permute_order):
	#print('Before permutate: {}'.format(block4))
	newBlock4 = [0, 0, 0, 0]
	for i, char in enumerate(block4):
		newBlock4[i] = block4[permute_order[i]-1]
	result = ''.join(newBlock4)
	#print('After permutate: {}'.format(result))
	return result

def crossBlocks(left_block, right_block):
	return right_block + left_block

def lucifer_encrypt(text, permute_order, shift, times = 4): # default times = 4
	mod = len(text) % BLOCK_SIZE
	# Fills with X character if a block is not completed (8 chars)
	if(mod != 0):
		for i in range(0,BLOCK_SIZE-mod):
			text += 'X'

	blocks = text

	for i in range(0, times):
		#print('\nENCRYPTION ROUND {}:'.format(i + 1))
		blocks = [blocks[i:i+BLOCK_SIZE] for i in range(0, len(blocks), BLOCK_SIZE)]
		blocks = blockOperations(blocks, permute_order, shift)

	return blocks

def lucifer_decrypt(text, permute_order, shift, times = 4): # default times = 4 (same that encryption)
	blocks = text

	for i in range(0, times):
		#print('\nDECRYPTION ROUND {}:'.format(i + 1))
		blocks = [blocks[i:i+BLOCK_SIZE] for i in range(0, len(blocks), BLOCK_SIZE)]
		blocks = blockOperations(blocks, permute_order, shift, 'decryption')

	return blocks

def main(): 
	# ENCRYPTION 
	#permute_order_encrypt = [4, 2, 1, 3]
	permute_order_encrypt = [2, 3, 1, 4]
	lucifer_encrypted_text = lucifer_encrypt(PLAIN_TEXT, permute_order_encrypt, SHIFT, ROUNDS) 
	print('Encrypt permute order: {}'.format(permute_order_encrypt))

	# DECRYPTION 
	permute_order_decrypt = [3, 1, 2, 4]
	print('Decrypt permute order: {}'.format(permute_order_decrypt))

	# RESULTS (SUMMARY)
	print('Plain text: {}'.format(PLAIN_TEXT))
	print('Longitud: {}'.format(len(PLAIN_TEXT)))
	print('Encrypted text: {}'.format(lucifer_encrypted_text))
	print('Decrypted Text: {}'.format(lucifer_decrypt(lucifer_encrypted_text, permute_order_decrypt, SHIFT, ROUNDS))) 

# Code execution
if __name__ == '__main__': 
	main() 