"""
Streaming data consumer
"""
from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector

TOPIC='info'
DATABASE = 'test-kafka'
USERNAME = 'root'
PASSWORD = 'test-kafka'

print("Connecting to the database")
try:
    connection = mysql.connector.connect(host='10.80.240.3', database=DATABASE, user=USERNAME, password=PASSWORD)
except Exception:
    print("Could not connect to database. Please check credentials")
else:
    print("Connected to database")
cursor = connection.cursor()

print("Connecting to Kafka")
consumer = KafkaConsumer(TOPIC)
print("Connected to Kafka")
print(f"Reading messages from the topic {TOPIC}")
for msg in consumer:

    # Extract information from kafka

    message = msg.value.decode("utf-8")

    # Transform 
    (name, city, email, birth, age) = message.split(",")
    

    # Loading data into the database table

    sql = "insert into info data values"
    result = cursor.execute(sql, (name, city, email, birth, age))
    print("Data was inserted into the database")
    connection.commit()
connection.close()