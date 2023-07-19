# kafka_python_streaming_data
This project will retrive data by calling API and pass data to Mysql database by using kafka interacting with python.
By this project will be composed all service in google cloud platform.
![image](https://github.com/khokiat/kafka_streaming_data/blob/main/Image/data%20architecture.jpg)

## Prerequisition & tools
1. Mysql 8.0
2. Compute engine (VM)
3. kafka == 2.12-2.8.0
4. Dbeaver (if any) to display data table

## step to run

1. Create Mysql database, in this project used Mysql 8.0. Defind connection by seleting private ip and also public ip if you need to connect database to database tool for instances Dbeaver, then create instances of database.

2. Compose VM by going to compute engine, in this project we chose debain os, set up network by using the valur that we've already set in Mysql database then create.

3. After strating VM you need to install package for PIP and java11 byusing below command
```bash
$sudo apt update
$sudo sudo apt install python3-pip #for pip python3
$sudo sudo apt install openjdk-11-jdk #for java11
```
4. Install mysql-client to connect with mysql database via VM byusing code
```bash
$sudo apt-get install default-mysql-client
```
5. Dowload and install kafka into VM
```bash
#DOWLAOD
$wget https://archive.apache.org/dist/kafka/2.8.0/kafka_2.12-2.8.0.tgz
#EXTRACT
$tar -xzf kafka_2.12-2.8.0.tgz
```
6. Interact witn SQL database via VM by using command 
```bash
$mysql --host='Mysql host ip' --port=3306 --user= 'username' --password= 'databasepassword'
```
7. Then create database and table into mysql 
```Mysql
#Create table
$CREATE DATABASE Database name 
$USE Database name

#Create table
CREATE TABLE tablename (name VARCHAR(100),city VARCHAR(100),email VARCHAR(255),Birth datetime,Age int);

$EXIT #exit Mysql
```

8. After composing database and table to interact with kafka and Mysql with python, we need to install python module Kafka-python and mysql-connector-python.

   kafka-python is a Python client for the Apache Kafka distributed stream processing system, which aims to provide similar functionalities as the main Kafka Java client as well as mysql-connector-python which help python to interact with mysql database.
``` bash
$python3 -m pip install kafka-python
$python3 python3 -m pip install mysql-connector-python==8.0.31
```
9. Since this we are going to start with kafka. first step is to start "zookeeper" by running following command
```shell
$cd kafka_2.12-2.8.0
$bin/zookeeper-server-start.sh config/zookeeper.properties
```

10. Open new terminal to run kafka broker
```shell
$cd kafka_2.12-2.8.0
$bin/kafka-server-start.sh config/server.properties
```
11. Create topic in kafka to recieve and retrive data by running following command.
```shell
$cd kafka_2.12-2.8.0
bin/kafka-topics.sh --create --topic "topic name" --bootstrap-server localhost:9092
```
12. Run [steraming_producer.py](https://github.com/khokiat/kafka_streaming_data/blob/main/Streaming_producer.py) file to calling api and produce message to kafka topic. command to run as below.--
**Please check detail and environment in python script before run your code.
```shell
$python3 steraming_producer.py
```

13. Run [streaming_consumer.py](https://github.com/khokiat/kafka_streaming_data/blob/main/streaming_consumer.py) to retrieve data from kafka topic that was produced from producer and transform datatype before inserting in mysql database. To run python script, use command
```shell
$python3 streaming_consumer.py
```
**Please check detail and environment in python script before running command.

## output
After running code, producer will calling API to retrive data from API then transform to message and pass to kafka topic. Then, consumer will retrieve data from kafka topic and transform data type into the form that we've set in Mysql database. finnally, consumer will insert data into database completely as table below. 
![image](https://github.com/khokiat/kafka_streaming_data/blob/main/Image/Image%2019-7-2566%20BE%20at%2014.21.jpg)

***In the picture, we displayed data table by using Dbeaver program to connect to Mysql database to help displaying datatable.