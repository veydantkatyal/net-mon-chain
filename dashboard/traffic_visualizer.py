import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def generate_visualizations(logs):
    """
    Generates advanced visualizations for network traffic using Matplotlib/Seaborn.
    :param logs: List of traffic logs
    """
    # Convert logs to DataFrame
    df = pd.DataFrame([log.split(",") for log in logs], columns=["Source", "Destination", "Protocol", "Size"])
    df['Size'] = df['Size'].astype(int)

    # Traffic Size Distribution by Protocol
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Protocol", y="Size", data=df)
    plt.title("Traffic Size Distribution by Protocol")
    plt.show()

    # Traffic Volume by Source IP
    traffic_volume = df.groupby("Source")['Size'].sum().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Source", y="Size", data=traffic_volume)
    plt.title("Traffic Volume by Source IP")
    plt.xticks(rotation=45)
    plt.show()


# Example usage:
if __name__ == "__main__":
    # Example logs
    logs = [
        "192.168.1.1,192.168.1.2,TCP,512",
        "192.168.1.2,192.168.1.3,UDP,1024",
        "192.168.1.3,192.168.1.4,TCP,256"
    ]
    generate_visualizations(logs)
