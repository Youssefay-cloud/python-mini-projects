import string
import random

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)


msg = input("Enter a message to encrypt: ")
cipher = ""

for char in msg:
    index = chars.index(char)
    cipher += key[index]

print(f"message is {msg}")    
print(f"encryptes message is {cipher}")



cipher = input("Enter encrypted message : ")
message = ""

for char in msg:
    index = key.index(char)
    message += chars[index]

print(f"encrypted message is {cipher}")
print(f"message is {msg}")    
