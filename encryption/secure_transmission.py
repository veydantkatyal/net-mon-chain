from encryption.encryption import encrypt_data, decrypt_data

def secure_send(data):
    encrypted = encrypt_data(data)
    print(f"Sending encrypted data: {encrypted}")

def secure_receive(encrypted_data):
    decrypted = decrypt_data(encrypted_data)
    print(f"Received decrypted data: {decrypted}")
