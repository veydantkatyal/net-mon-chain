import socket
from db.cassandra_client import store_traffic_log

def process_packet(packet):
    eth = dpkt.ethernet.Ethernet(packet)
    if isinstance(eth.data, dpkt.ip.IP):
        ip = eth.data
        ip_src = socket.inet_ntoa(ip.src)
        ip_dst = socket.inet_ntoa(ip.dst)
        protocol = "TCP" if isinstance(ip.data, dpkt.tcp.TCP) else "UDP" if isinstance(ip.data, dpkt.udp.UDP) else "Other"
        return f"{ip_src} -> {ip_dst}, Protocol: {protocol}, Size: {len(packet)} bytes"
    return None

def store_log_in_db(log):
    print(f"Storing log: {log}")
    session = store_traffic_log(log)
