import decrypt
import os


word = input("enter the word to hash it :")
word = word.encode()

hash = decrypt.encrypt(word)

os.system("cls")

print(hash)