

import binascii
import os
import codecs
from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
def int_of_string(s):
    #return int(binascii.hexlify(s), 16)
    return int(s, 16)
def encrypt_message(key, plaintext, iv):
    #iv = os.urandom(16)
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.encrypt(plaintext)
def decrypt_message(key, ciphertext, iv):
    #iv = ciphertext[:16]
    ctr = Counter.new(128, initial_value=int_of_string(iv))
    aes = AES.new(key, AES.MODE_CTR, counter=ctr)
    return aes.decrypt(ciphertext)


# data = b"6bc1bee22e409f96e93d7e117393172a"
# key = b"2b7e151628aed2a6abf7158809cf4f3c"
# iv= b"f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"
# #iv_decoded = codecs.decode(iv, 'hex')
# data_decoded=codecs.decode(data, 'hex')
# key_decoded=codecs.decode(key, 'hex')

# print("Message:",data)
# e = encrypt_message(key_decoded, data_decoded, iv)
# # print(e)
# print("Ciphertext:", codecs.encode(e,"hex"))
# d = decrypt_message(key_decoded, e, iv)
# # print(d)  
# print("Decipher:",codecs.encode(d,"hex"))

"""
OUTPUT:

➜  hw12 git:(master) ✗ python3 ctr.py
Message: b'6bc1bee22e409f96e93d7e117393172a'
Ciphertext: b'874d6191b620e3261bef6864990db6ce'
Decipher: b'6bc1bee22e409f96e93d7e117393172a'
➜  hw12 git:(master) ✗ 
"""

data = b"00112233445566778899aabbccddeeff"
key = b"000102030405060708090a0b0c0d0e0f1011121314151617"
iv= b"f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"
#iv_decoded = codecs.decode(iv, 'hex')
data_decoded=codecs.decode(data, 'hex')
key_decoded=codecs.decode(key, 'hex')

print("Key:",key)
print("IV:", iv)
print("Message:",data)
e = encrypt_message(key_decoded, data_decoded, iv)
# print(e)
print("Ciphertext:", codecs.encode(e,"hex"))
d = decrypt_message(key_decoded, e, iv)
# print(d)  
print("Decipher:",codecs.encode(d,"hex"))

""" 

Message: b'00112233445566778899aabbccddeeff'
Ciphertext: b'917373b15826c3554b0f7c9cf4dc78f8'
Decipher: b'00112233445566778899aabbccddeeff'
"""