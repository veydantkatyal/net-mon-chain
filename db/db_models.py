from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def create_keyspace():
    """
    Create the keyspace (namespace) in Cassandra.
    """
    auth_provider = PlainTextAuthProvider(username='your_username', password='your_password')
    cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
    session = cluster.connect()

    # Create keyspace if not exists
    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS network_logs
    WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1}
    """)

def create_db_models():
    """
    Create the 'logs' table in the 'network_logs' keyspace.
    """
    # Connect to Cassandra
    auth_provider = PlainTextAuthProvider(username='your_username', password='your_password')
    cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
    session = cluster.connect()
    
    # Set the keyspace
    session.set_keyspace('network_logs')

    # Create the logs table
    session.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        log_id UUID PRIMARY KEY,
        traffic_data TEXT
    )
    """)
    print("Table 'logs' created successfully.")

if __name__ == "__main__":
    create_keyspace()
    create_db_models()
