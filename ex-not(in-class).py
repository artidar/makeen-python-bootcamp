import re  # Mostafa Felani ----> # mostafa.felani
import json
import requests
import random
import qrcode
name = input("Enter your name : ")
# user_name = str
pattern = '^[A-Z][a-z]+\s[A-Z][a-z]+$'
if re.search(pattern, name) :
    user_name = name.lower()
    re.sub('\s','.',user_name)
else:
    print("Wrong Input")
    
id_1 = random.randint(1000,9999)

img = qrcode.make(f'name :{name} \nID:{id_1} \nUsername: {user_name}\n')
img.save('test.jpeg')

    






