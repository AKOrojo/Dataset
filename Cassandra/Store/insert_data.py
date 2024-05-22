from cassandra.cluster import Cluster
import random
from datetime import datetime, timedelta


def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )


def main():
    cluster = Cluster(['172.18.0.2'])  # Use the IP address of your Cassandra container
    session = cluster.connect('store')  # Connect to the keyspace

    insert_statement = session.prepare(
        "INSERT INTO shopping_cart (userid, item_count, last_update_timestamp) VALUES (?, ?, ?)")

    start_date = datetime(2020, 1, 1)
    end_date = datetime(2024, 12, 31)

    for i in range(3000):
        userid = str(random.randint(1000, 9999))  # Convert userid to string
        item_count = random.randint(1, 20)
        last_update_timestamp = random_date(start_date, end_date)
        session.execute(insert_statement, (userid, item_count, last_update_timestamp))
        if i % 100 == 0:  # Print progress every 100 inserts
            print(f'{i} records inserted')

    cluster.shutdown()


if __name__ == "__main__":
    main()
