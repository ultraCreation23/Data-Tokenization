import hashlib
import ctypes

card = input("Enter the card number: ")
card = "".join(card.split())

def hashing(card):
    digest = hashlib.sha256(card.encode())
    hash = bytearray(digest.digest())
    hexString = ""
    # hexString = ctypes.create_string_buffer(hexString) 
    for i in range(len(hash)):
        hex1 = hex(0xFF & int(hash[i]))
        if (len(hex1) == 1):
            hexString += '0'
        hexString += hex1
    return hexString

    # m = hashlib.sha256(card)
    # m.update(str.encode('utf-8'))
    # bytes = m.digest()
    # return ''.join('{:02x}'.format(x) for x in bytes)

print(hashing(card))


