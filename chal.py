#!/usr/bin/python3
from json import JSONDecodeError, loads, dumps
from binascii import hexlify, unhexlify
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from typing import Tuple

with open("milk") as f: 
    MILK = f.readline()

KEY = get_random_bytes(16)

def encrypt(plaintext: bytes) -> Tuple[bytes, bytes]:
    iv = get_random_bytes(16)
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    print("IV:", hexlify(iv).decode())
    return iv, aes.encrypt(plaintext)

def decrypt(ciphertext: bytes, iv: bytes) -> bytes:
    aes = AES.new(KEY, AES.MODE_CBC, iv)
    return aes.decrypt(ciphertext)

def create_milk(ingredients: str) -> Tuple[bytes, bytes]:
    payload = {"from": "guest", "act": "milk", "msg": ingredients}
    payload = dumps(payload).encode()
    while len(payload) % 16 != 0:
        payload += b'\x00'
    iv, payload = encrypt(payload)
    return hexlify(iv).decode('utf-8'), hexlify(payload).decode('utf-8')

def drink_milk(iv: bytes, milk: str):
    try: 
        iv = unhexlify(iv)
        milk = unhexlify(milk)
        milk = decrypt(milk, iv)
        while milk.endswith(b'\x00') and len(milk) > 0:
            milk = milk[:-1]
    except:
        print("Failed to decrypt")
        return 
    
    try:
        milk = milk.decode()
        milk = loads(milk)
    except UnicodeDecodeError:
        print(f"Failed to decode UTF-8: {hexlify(milk).decode('UTF-8')}")
        return
    except JSONDecodeError:
        print(f"Failed to decode JSON: {milk}")
        return

    match milk["act"]:
        case "milk":
            msg = milk['msg']
            print(f"You received the following milk: {msg}! Enjoy!")
        case "flag":
            if milk["from"] == "mommy":
                print(f"Thank you mommy! Here is my gift for you :3 {MILK}")
            else:
                print("You don't have permissions to perform this action")
        case action:
            print(f"Invalid action {action}")

def show_prompt():
    print("-" * 75)
    print("1. Create milk")
    print("2. Drink milk")
    print("3. Exit")
    print("-" * 75)

    try:
        sel = input("> ")
        sel = int(sel)

        match sel:
            case 1:
                msg = input("Please enter your ingredients: ")
                iv, milk = create_milk(msg)
                print(f"IV: {iv}")
                print(f"Milk: {milk}")
            case 2:
                iv = input("IV: ")
                milk = input("Command: ")
                drink_milk(iv, milk)
            case 3:
                exit(0)
            case _:
                print("Invalid selection")
                return
    except ValueError:
        print("Invalid selection")
        return


if __name__ == "__main__":
    while True:
        show_prompt()
