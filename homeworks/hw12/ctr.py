# from Cryptodome.Cipher import AES
# from Cryptodome.Util import Counter
# from Cryptodome import Random
# from base64 import b64encode

# init_ctr_str ='f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff'.encode("utf8")
# init_ctr = Counter.new(32, init_ctr_str) 
# key = b'2b7e151628aed2a6abf7158809cf4f3c' # .encode("utf8")
# plaintext = b'6bc1bee22e409f96e93d7e117393172a' # .encode("utf8")
# encrypto = AES.new(key, AES.MODE_ECB, ) #counter=init_ctr
# encrypted = encrypto.encrypt(plaintext)
# ct = b64encode(encrypted).decode('utf-8')
# print(encrypted)
# print(encrypted.hex())
# print(ct)
# decrypto = AES.new(key, AES.MODE_ECB)
# print(decrypto.decrypt(encrypted) )# prints "asdk"


import json
import sys
from base64 import b64encode
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
from Cryptodome import Random
import codecs

# data = b"6bc1bee22e409f96e93d7e117393172a"
# key = b"2b7e151628aed2a6abf7158809cf4f3c"
# IV= b"000102030405060708090a0b0c0d0e0f"
# print("MESSAGE INIT:", data)
# iv_decoded = codecs.decode(IV, 'hex')
# data_decoded=codecs.decode(data, 'hex')
# key_decoded=codecs.decode(key, 'hex')


# # print(sys.getsizeof(iv2))
# cipher = AES.new(key_decoded, AES.MODE_CBC, iv=iv_decoded)
# ct_bytes = cipher.encrypt(pad(data_decoded, AES.block_size))
# iv = b64encode(cipher.iv).decode('utf-8')
# ct = b64encode(ct_bytes).decode('utf-8')
# result = json.dumps({'iv':iv, 'ciphertext':ct})
# print(result)

# print(cipher.iv)
# print(codecs.encode(cipher.iv, 'hex'))
# print(codecs.encode(ct_bytes,"hex"))

# cipher = AES.new(key_decoded, AES.MODE_CBC, iv=iv_decoded)
# pt = unpad(cipher.decrypt(ct_bytes), AES.block_size)
# print("The message was: ", pt)
# print("MESSAGE DECR:", codecs.encode(pt,"hex"))

import binascii
import os
from Cryptodome.Cipher import AES
from Cryptodome.Util import Counter
def int_of_string(s):
    return int(binascii.hexlify(s), 16)
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


data = b"6bc1bee22e409f96e93d7e117393172a"
key = b"2b7e151628aed2a6abf7158809cf4f3c"
iv= b"f0f1f2f3f4f5f6f7f8f9fafbfcfdfeff"
iv_decoded = codecs.decode(iv, 'hex')
data_decoded=codecs.decode(data, 'hex')
key_decoded=codecs.decode(key, 'hex')

print("Message:",data)
e = encrypt_message(key_decoded, data_decoded, iv_decoded)
# print(e)
print("Ciphertext:", codecs.encode(e,"hex"))
d = decrypt_message(key_decoded, e, iv_decoded)
# print(d)  
print("Decipher:",codecs.encode(d,"hex"))
