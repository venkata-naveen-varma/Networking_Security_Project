import os
from config import key
from pytea import TEA


def encrypt(plain_text):
    _key = bytes(key, 'utf-8')
    tea = TEA(_key)
    encrypted_text = tea.encrypt(plain_text.encode())
    return encrypted_text.hex()

def decrypt(encrypted_text):
    tea1 = TEA(key)
    decrypted_bytes = bytes.fromhex(encrypted_text)
    decrypted_text = tea1.decrypt(decrypted_bytes)
    return decrypted_text.decode()