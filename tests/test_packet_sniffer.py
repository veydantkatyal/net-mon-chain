import unittest
from net_monitor.packet_sniffer import process_packet

class TestPacketSniffer(unittest.TestCase):

    def test_process_tcp_packet(self):
        # Sample TCP packet (Ethernet + IP + TCP headers)
        packet = b'\x00\x50\x56\xc0\x00\x01\x00\x0c\x29\x3b\xe0\xdd\x08\x00\x45\x00\x00\x3c\x1c\x46\x00\x00\x80\x06\xf6\x3d\xc0\xa8\x00\x68\xc0\xa8\x00\x01'
        result = process_packet(packet)
        self.assertIsNotNone(result)
        self.assertIn("TCP", result)

    def test_process_udp_packet(self):
        # Sample UDP packet (Ethernet + IP + UDP headers)
        packet = b'\x00\x50\x56\xc0\x00\x01\x00\x0c\x29\x3b\xe0\xdd\x08\x00\x45\x00\x00\x3c\x1c\x46\x00\x00\x80\x11\xf6\x3d\xc0\xa8\x00\x68\xc0\xa8\x00\x01'
        result = process_packet(packet)
        self.assertIsNotNone(result)
        self.assertIn("UDP", result)

    def test_process_invalid_packet(self):
        # Invalid packet
        packet = b'\x00\x50\x56\xc0\x00\x01'
        result = process_packet(packet)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
