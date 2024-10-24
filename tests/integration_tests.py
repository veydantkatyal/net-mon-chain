import unittest
import threading
import socket
from net_monitor.packet_sniffer import process_packet
from encryption.encryption import encrypt_data, decrypt_data
from p2p_network.p2p_node import Node

class TestIntegration(unittest.TestCase):

    def setUp(self):
        # Start a P2P node in a separate thread for integration testing
        self.node = Node(host='127.0.0.1', port=5001)
        threading.Thread(target=self.node.start).start()

    def test_sniffer_encryption_p2p(self):
        # Simulate a captured network packet (Ethernet + IP + TCP)
        packet = b'\x00\x50\x56\xc0\x00\x01\x00\x0c\x29\x3b\xe0\xdd\x08\x00\x45\x00\x00\x3c\x1c\x46\x00\x00\x80\x06\xf6\x3d\xc0\xa8\x00\x68\xc0\xa8\x00\x01'
        
        # Process the packet
        processed_log = process_packet(packet)
        self.assertIsNotNone(processed_log)

        # Encrypt the processed log
        encrypted_log = encrypt_data(processed_log)
        self.assertNotEqual(processed_log, encrypted_log)

        # Send the encrypted log via P2P
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect(('127.0.0.1', 5001))
        peer.send(encrypted_log)
        peer.close()

        # Decrypt the log to verify data integrity
        decrypted_log = decrypt_data(encrypted_log)
        self.assertEqual(processed_log, decrypted_log)

    def tearDown(self):
        # Clean up or shutdown the node if needed
        pass

if __name__ == "__main__":
    unittest.main()
