from datetime import datetime
from kafka import KafkaConsumer
import mysql.connector
import ast

TOPIC = 'information'
DATABASE = 'info'
USERNAME = 'root'
PASSWORD = 'test-kafka'

print("Connecting to the database")
try:
    with mysql.connector.connect(host='10.80.240.5', database=DATABASE, user=USERNAME, password=PASSWORD) as connection:
        print("Connected to the database")
        cursor = connection.cursor()

        print("Connecting to Kafka")
        consumer = KafkaConsumer(TOPIC)
        print("Connected to Kafka")
        print(f"Reading messages from the topic {TOPIC}")

        for msg in consumer:
            # Extract information from Kafka
            message = msg.value.decode("utf-8")
            print(message)
            # Transform
            my_list = ast.literal_eval(message)
            (name, city, email, birth_str, age_str) = my_list
            print(age_str)
            print(birth_str)
        
            # Convert age_str to an integer
            age = int(float(age_str))
        
            # Convert the date string to a datetime object
            try :
                date = datetime.strptime(birth_str, "%Y-%m-%d %H:%M:%S.%f")
                birth = date.strftime("%Y-%m-%d %H:%M:%S")
            except ValueError:
                date = datetime.strptime(birth_str, '%Y-%m-%dT%H:%M:%S.%fZ')
                birth = date.strftime("%Y-%m-%d %H:%M:%S")

            print("Data transformation is finished")

            # Loading data into the database table
            sql = "INSERT INTO info (name, city, email, Birth, Age) VALUES (%s, %s, %s, %s, %s)"
            data = (name, city, email, birth, age)
            cursor.execute(sql, data)

            print("Data was inserted into the database")
            connection.commit()

except mysql.connector.Error as e:
    print("Could not execute the SQL statement:", e)

    
