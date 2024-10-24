import unittest
from encryption.encryption import encrypt_data, decrypt_data

class TestEncryption(unittest.TestCase):

    def test_encryption_decryption(self):
        # Original data
        original_data = "Test network traffic log"

        # Encrypt the data
        encrypted_data = encrypt_data(original_data)
        self.assertNotEqual(original_data, encrypted_data)

        # Decrypt the data
        decrypted_data = decrypt_data(encrypted_data)
        self.assertEqual(original_data, decrypted_data)

if __name__ == "__main__":
    unittest.main()
