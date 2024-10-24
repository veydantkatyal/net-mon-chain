import dpkt
import socket
from net_monitor.pcap_processor import process_packet, store_log_in_db

def packet_sniffer(pcap_file):
    with open(pcap_file, 'rb') as f:
        pcap = dpkt.pcap.Reader(f)
        for timestamp, packet in pcap:
            processed_packet = process_packet(packet)
            if processed_packet:
                store_log_in_db(processed_packet)

if __name__ == "__main__":
    packet_sniffer('traffic.pcap')
