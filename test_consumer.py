from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector

TOPIC = 'info'
DATABASE = 'information'
USERNAME = 'root'
PASSWORD = 'test-kafka'

print("Connecting to the database")
try:
    with mysql.connector.connect(host='10.80.240.3', database=DATABASE, user=USERNAME, password=PASSWORD) as connection:
        print("Connected to the database")
        cursor = connection.cursor()

        print("Connecting to Kafka")
        consumer = KafkaConsumer(TOPIC)
        print("Connected to Kafka")
        print(f"Reading messages from the topic {TOPIC}")

        for msg in consumer:
            # Extract information from Kafka
            message = msg.value.decode("utf-8")

            # Transform
            (name, city, email, birth, age) = message.split(",")

            # Loading data into the database table
            sql = "INSERT INTO info (name, city, email, birth, age) VALUES (%s, %s, %s, %s, %s)"
            data = (name, city, email, birth, age)
            cursor.execute(sql, data)

            print("Data was inserted into the database")
            connection.commit()

except Exception as e:
    print("Could not connect to the database or encountered an error:", e)
