from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

def send_log_to_kafka(log):
    producer.send('traffic_logs', value=log.encode())
    producer.flush()
