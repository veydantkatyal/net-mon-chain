from cryptography.fernet import Fernet

def load_key():
    return open("key.key", "rb").read()

def encrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(data.encode())

def decrypt_data(data):
    key = load_key()
    fernet = Fernet(key)
    return fernet.decrypt(data).decode()
