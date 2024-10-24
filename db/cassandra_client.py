from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connect_to_cassandra():
    """
    Connect to the Cassandra cluster.
    :return: Cassandra session object
    """
    # Update with your Cassandra connection details (for authentication, use appropriate credentials)
    auth_provider = PlainTextAuthProvider(username='your_username', password='your_password')
    cluster = Cluster(['127.0.0.1'], auth_provider=auth_provider)
    session = cluster.connect()

    # Set the keyspace (namespace)
    session.set_keyspace('network_logs')
    return session

def store_traffic_log(session, log):
    """
    Store a traffic log in the Cassandra database.
    :param session: Cassandra session
    :param log: Traffic log data (string format: 'source -> destination, protocol, size')
    """
    query = """
    INSERT INTO logs (log_id, traffic_data)
    VALUES (uuid(), %s)
    """
    session.execute(query, (log,))
    print(f"Stored log: {log}")
