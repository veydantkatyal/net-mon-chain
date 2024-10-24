import streamlit as st
import pandas as pd
import os

def load_traffic_logs(log_file="traffic_log.txt"):
    """
    Loads traffic logs from the log file.
    :param log_file: Path to the log file
    :return: List of logs
    """
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            logs = f.readlines()
        return [log.strip() for log in logs]
    else:
        return []

def visualize_traffic():
    """
    Creates a Streamlit-based visualization of network traffic logs.
    """
    st.title("NetMonChain - Network Traffic Monitor")

    # Load traffic logs
    logs = load_traffic_logs()

    if logs:
        # Parse the logs into a DataFrame
        df = pd.DataFrame([log.split(",") for log in logs], columns=["Source", "Destination", "Protocol", "Size"])
        st.write("### Network Traffic Logs")
        st.dataframe(df)

        # Additional visualizations (Traffic by Protocol)
        protocol_counts = df['Protocol'].value_counts()
        st.write("### Traffic by Protocol")
        st.bar_chart(protocol_counts)

    else:
        st.write("No traffic logs available.")

if __name__ == "__main__":
    visualize_traffic()

