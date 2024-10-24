import hashlib
import random

class DHTNode:
    def __init__(self, node_id, address):
        self.node_id = node_id  # Unique ID for each node
        self.address = address  # Node address in the format 'IP:PORT'
        self.routing_table = {}  # DHT routing table: {hash_key: DHTNode}

    def hash_key(self, key):
        """
        Hashes a key (e.g., node_id) using SHA-1 to ensure consistent placement in the DHT.
        :param key: The key to hash (node_id)
        :return: A consistent hash value for the key
        """
        return int(hashlib.sha1(key.encode()).hexdigest(), 16)

    def add_peer(self, peer_node):
        """
        Adds a peer to the DHT routing table.
        :param peer_node: The peer node to add
        """
        peer_hash = self.hash_key(peer_node.node_id)
        self.routing_table[peer_hash] = peer_node
        print(f"Peer {peer_node.node_id} added to routing table with address {peer_node.address}")

    def lookup(self, node_id):
        """
        Looks up a peer in the DHT by node_id.
        :param node_id: The ID of the peer to find
        :return: The DHTNode if found, otherwise None
        """
        peer_hash = self.hash_key(node_id)
        return self.routing_table.get(peer_hash, None)

    def get_random_peer(self):
        """
        Returns a random peer from the routing table.
        :return: A random DHTNode or None if no peers exist
        """
        if self.routing_table:
            return random.choice(list(self.routing_table.values()))
        return None


# Example usage of peer discovery using DHT
if __name__ == "__main__":
    # Create DHT nodes
    node1 = DHTNode('node1', '127.0.0.1:5000')
    node2 = DHTNode('node2', '127.0.0.1:5001')
    node3 = DHTNode('node3', '127.0.0.1:5002')

    # Add peers to the DHT
    node1.add_peer(node2)
    node1.add_peer(node3)

    # Lookup a peer by ID
    peer = node1.lookup('node2')
    if peer:
        print(f"Found peer: {peer.node_id} at {peer.address}")
    else:
        print("Peer not found.")

    # Get a random peer from the routing table
    random_peer = node1.get_random_peer()
    if random_peer:
        print(f"Random peer: {random_peer.node_id} at {random_peer.address}")
