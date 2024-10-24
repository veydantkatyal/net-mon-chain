import unittest
from p2p_network.p2p_node import Node
import socket
import threading

class TestP2PNetwork(unittest.TestCase):

    def setUp(self):
        # Start a P2P node in a separate thread
        self.node = Node(host='127.0.0.1', port=5001)
        threading.Thread(target=self.node.start).start()

    def test_peer_connection(self):
        # Simulate a peer connection
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect(('127.0.0.1', 5001))
        peer.send(b"Test log data")
        peer.close()

        # Check if the peer is added to the node's peer list
        self.assertIn(('127.0.0.1', 5001), self.node.peers)

    def tearDown(self):
        # Clean up or shutdown the node if needed
        pass

if __name__ == "__main__":
    unittest.main()
