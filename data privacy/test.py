import random
import hashlib


data = {}
while True:
    card = input("Enter the card number: ")
    card = "".join(card.split())
    
    # if card in data.keys():
    #     print(f"Your Token is already there: {data[card]}")
    # else:
    #     token = hashlib.sha256(card.encode())
    #     # while token in data.values():
    #     #     token = random.randint(1000,9999)
    #     data[card] = token.hexdigest()
    #     print(f"Your Token is: {token.hexdigest()}")
    # choice = input("Do you want to enter another Card? ")
    token = hashlib.md5(card.encode())
        # while token in data.values():
        #     token = random.randint(1000,9999)
    data[card] = token.hexdigest()
    print(f"Your Token is: {token.hexdigest()}")
    choice = input("Do you want to enter another Card? ")


    if choice.lower() == 'yes':
        continue
    else:
        break

print(data)