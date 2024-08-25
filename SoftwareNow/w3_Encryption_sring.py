import string
import random

chars= " " + string.ascii_letters + string.punctuation + string.ascii_letters
chars = list (chars)
key= chars.copy()

random.shuffle (key)


#Enccryption:

plain_text=input("Enter a new message: ")
cipher_text= ""

for letters in plain_text:
    index= chars.index(letters)
    cipher_text += key[index]


print (f"Original message: {plain_text}")
print(f"Encrypted Message: {cipher_text}")


#Decryption:

cipher_text =input("Enter a new message: ")
plain_text = ""

for letters in cipher_text:
    index= key.index(letters)
    plain_text += chars[index]


print (f"Original Message: {plain_text}")
print(f"Decrypted Message: {cipher_text}")