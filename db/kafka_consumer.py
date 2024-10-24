from kafka import KafkaConsumer
from cassandra_client import connect_to_cassandra, store_traffic_log

def consume_logs():
    """
    Consume traffic logs from Kafka and store them in Cassandra.
    """
    # Set up Kafka consumer
    consumer = KafkaConsumer(
        'traffic_logs', 
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='traffic-log-group'
    )

    # Connect to Cassandra
    session = connect_to_cassandra()

    # Consume and store logs
    for message in consumer:
        log = message.value.decode('utf-8')
        store_traffic_log(session, log)

if __name__ == "__main__":
    consume_logs()
