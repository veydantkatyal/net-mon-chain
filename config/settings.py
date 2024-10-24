# Global settings for the NetMonChain project

# Kafka settings
KAFKA_BROKER = 'localhost:9092'  # The address of the Kafka broker
KAFKA_TOPIC = 'traffic_logs'      # The topic where traffic logs are published
KAFKA_GROUP_ID = 'traffic-log-group'  # The Kafka consumer group ID for consuming logs

# Cassandra settings
CASSANDRA_HOSTS = ['127.0.0.1']   # List of Cassandra nodes
CASSANDRA_KEYSPACE = 'network_logs'  # The keyspace (namespace) in Cassandra
CASSANDRA_USERNAME = 'your_username'  # Replace with your Cassandra username
CASSANDRA_PASSWORD = 'your_password'  # Replace with your Cassandra password

# Application settings
NODE_PORT = 5000                  # Default port for P2P node communication
LOG_FILE = 'netmonchain.log'       # Log file for storing application logs

# Prometheus settings (for metrics export)
PROMETHEUS_PORT = 8000            # Port for Prometheus to scrape metrics
