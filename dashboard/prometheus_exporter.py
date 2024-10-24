from prometheus_client import start_http_server, Counter
import time
import random

# Prometheus metric to track the number of packets by protocol
protocol_counter = Counter('traffic_protocol_count', 'Traffic by Protocol', ['protocol'])

def export_logs_to_prometheus():
    """
    Simulates exporting traffic logs as Prometheus metrics.
    """
    # Start Prometheus metrics server
    start_http_server(8000)

    # Simulate continuous log updates (this would typically come from the network)
    protocols = ['TCP', 'UDP', 'ICMP']
    
    while True:
        # Increment the Prometheus counter for a random protocol
        protocol = random.choice(protocols)
        protocol_counter.labels(protocol=protocol).inc()
        
        # Sleep before updating the next metric (simulate log processing delay)
        time.sleep(2)

if __name__ == "__main__":
    export_logs_to_prometheus()
