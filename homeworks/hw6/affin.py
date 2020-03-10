'''
@title: CRIPTOGRAFÍA. TAREA 6. ALGORITMO DE CIFRADO Y DESCIFRADO POR EL MÉTODO AFFIN
@authors: Luis Gerardo López S. Jiménez, Marco A. Moreno Guerra
@date_creation: 06/03/2020
@date_last_update: 09/03/2020
@comments: 
	This code requires python 3 to be execute.
'''
LETTERS = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'

# Extended Euclidean Algorithm for finding modular inverse 
# eg: modinv(7, 27) = 15
def egcd(a, b): 
	x,y, u,v = 0,1, 1,0
	while a != 0: 
		q, r = b//a, b%a 
		m, n = x-u*q, y-v*q 
		b,a, x,y, u,v = a,r, u,v, m,n 
	gcd = b 
	return gcd, x, y 

def modinv(a, m): 
	gcd, x, y = egcd(a, m) 
	if gcd != 1: 
		return None # modular inverse does not exist 
	else: 
		return x % m 

# affine cipher encrytion function 
# returns the cipher text 
def affine_encrypt(text, a, b): 
	''' 
	M = (a*P + b) % 27 
	'''
	result = ""
	for char in text:
		m = (a*LETTERS.find(char) + b) % 27
		result += LETTERS[m]
	return result

# affine cipher decryption function 
# returns original text 
def affine_decrypt(cipher, a, b): 
	''' 
	P = (a^-1 * (C - b)) % 27
	'''
	result = ""
	inv = modinv(a, 27)
	for char in cipher:
		p = (inv * (LETTERS.find(char) - b)) % 27
		result += LETTERS[p]
	return result

# Driver Code to test the above functions 
def main(): 
	# declaring text and key 
	text = 'PORMIRAZAHABLARAELESPIRITU'
	a = 17
	b = 20

	# calling encryption function 
	affine_encrypted_text = affine_encrypt(text, a, b) 

	print('Plain text: {}'.format(text))
	print('Encrypted Text: {}'.format(affine_encrypted_text)) 
	print('Decrypted Text: {}'.format(affine_decrypt(affine_encrypted_text, a, b))) 

# Code execution
if __name__ == '__main__': 
	main() 