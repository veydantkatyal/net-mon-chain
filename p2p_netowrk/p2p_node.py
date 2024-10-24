import socket
import threading
from p2p_network.kafka_producer import send_log_to_kafka

class Node:
    def __init__(self, host='127.0.0.1', port=5000):
        self.host = host
        self.port = port
        self.peers = []

    def handle_peer(self, conn, addr):
        while True:
            data = conn.recv(1024)
            if not data:
                break
            send_log_to_kafka(data.decode())
        conn.close()

    def start(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((self.host, self.port))
        server.listen(5)
        while True:
            conn, addr = server.accept()
            threading.Thread(target=self.handle_peer, args=(conn, addr)).start()

    def connect_to_peer(self, peer_host, peer_port):
        peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        peer.connect((peer_host, peer_port))
        self.peers.append((peer_host, peer_port))

        with open("traffic_log.txt", "r") as f:
            data = f.read()
            peer.send(data.encode())
        peer.close()

if __name__ == "__main__":
    node = Node(host='127.0.0.1', port=5001)
    threading.Thread(target=node.start).start()

    peer_host = '127.0.0.1'
    peer_port = 5000
    node.connect_to_peer(peer_host, peer_port)
