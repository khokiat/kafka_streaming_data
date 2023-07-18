"""
Streaming producer
"""
import requests
from kafka import KafkaProducer
import json
from time import sleep

producer = KafkaProducer(bootstrap_servers='10.170.0.27:9092')

TOPIC = 'information'
url = 'https://randomuser.me/api/'

for i in range (10000) : 
    response = requests.get(url)
    data = response.json()
    re = data["results"][0]
    print("Read data finish")
    name = re["name"]["first"]
    city = re["location"]["city"]
    email = re["email"]
    birth = re["dob"]["date"]
    age = re["dob"]["age"]
    record = (name, city, email, birth, age) #tuple
    message = json.dumps(record).encode("utf-8") #change to string and encode
    producer.send(TOPIC, message)
    sleep(30)
    print("done")
print("Cannot run code")

