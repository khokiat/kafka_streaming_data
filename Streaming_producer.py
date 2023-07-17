"""
Streaming producer
"""
import requests
from kafka import KafkaProducer
producer = kafkaProducer(bootstrap = 'local host:9092')

TOPIC = 'info'
url = 'https://randomuser.me/api/'
try :

    raw = requests.get(url)
    re = raw["results"][0]
    name = re["name"]["first"]
    city = re["location"]["city"]
    email = re["email"]
    birth = re["dob"]["date"]
    age = re["dob"]["age"]
    record = (name, city, email, birth, age)
    message = bytearray(record.encode("utf-8"))
    producer.send(TOPIC, message)
    sleep(30)
except :
    Print("Cannot run code")

