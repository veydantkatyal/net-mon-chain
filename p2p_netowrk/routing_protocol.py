class DistanceVectorNode:
    def __init__(self, node_id, neighbors):
        """
        Initializes the node with its ID and neighboring nodes.
        :param node_id: The unique ID of the node
        :param neighbors: A dictionary of neighboring nodes and their associated costs
        """
        self.node_id = node_id
        self.neighbors = neighbors  # Neighbors: {neighbor_id: cost}
        self.routing_table = {node_id: (0, None)}  # {destination_id: (cost, next_hop)}

    def update_routing_table(self):
        """
        Applies the Distance Vector algorithm to update the routing table.
        :return: True if the table was updated, False otherwise
        """
        updated = False

        # Iterate over each neighbor and update routing table
        for neighbor, cost in self.neighbors.items():
            neighbor_table = self.get_neighbor_routing_table(neighbor)

            # Update the routing table based on neighbor information
            for destination, (neighbor_cost, _) in neighbor_table.items():
                total_cost = cost + neighbor_cost
                if destination not in self.routing_table or total_cost < self.routing_table[destination][0]:
                    self.routing_table[destination] = (total_cost, neighbor)
                    updated = True

        return updated

    def get_neighbor_routing_table(self, neighbor):
        """
        Simulates the retrieval of a neighbor's routing table.
        :param neighbor: The neighbor node
        :return: The neighbor's routing table (For simplicity, this is hardcoded or predefined)
        """
        # In a real-world application, this would involve querying the neighbor over the network
        # Here, we simulate it with predefined routing tables.
        if neighbor == 'node2':
            return {'node1': (1, 'node2'), 'node3': (2, 'node2')}
        elif neighbor == 'node3':
            return {'node1': (5, 'node3'), 'node2': (2, 'node3')}
        return {}

    def print_routing_table(self):
        """
        Prints the current routing table.
        """
        print(f"Routing Table for {self.node_id}:")
        for destination, (cost, next_hop) in self.routing_table.items():
            print(f"Destination: {destination}, Cost: {cost}, Next Hop: {next_hop}")


# Example usage of Distance Vector Routing
if __name__ == "__main__":
    # Define neighbors and their costs
    neighbors_node1 = {'node2': 1, 'node3': 5}
    neighbors_node2 = {'node1': 1, 'node3': 2}
    neighbors_node3 = {'node1': 5, 'node2': 2}

    # Create nodes with their neighbors
    node1 = DistanceVectorNode('node1', neighbors_node1)
    node2 = DistanceVectorNode('node2', neighbors_node2)
    node3 = DistanceVectorNode('node3', neighbors_node3)

    # Update the routing tables for each node
    node1.update_routing_table()
    node2.update_routing_table()
    node3.update_routing_table()

    # Print the routing tables
    node1.print_routing_table()
    node2.print_routing_table()
    node3.print_routing_table()
