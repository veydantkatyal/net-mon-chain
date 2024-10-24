# NetMonChain: Decentralized Network Traffic Monitoring

## Overview
NetMonChain is a decentralized system for monitoring network traffic across distributed nodes. Traffic logs are captured using packet sniffing, encrypted, and shared across nodes using a P2P communication system. Logs are stored in a distributed database for real-time visualization and analysis.

## Features
- **Packet Sniffing**: Efficient packet capture using `dpkt`.
- **P2P Network**: Decentralized peer-to-peer communication.
- **Encryption**: AES encryption for secure log transmission.
- **Traffic Visualization**: Real-time traffic analysis using Streamlit and Grafana.
- **Distributed Storage**: Logs stored in Cassandra for scalability.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/veydantkatyal/net-mon-chain.git
    cd net-mon-chain
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the packet sniffer:
    ```bash
    python net_monitor/packet_sniffer.py
    ```

4. Start the P2P node:
    ```bash
    python p2p_network/p2p_node.py
    ```

5. Launch the dashboard:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

## License
This is project is licensed under MIT License[], please go through it carefully.
