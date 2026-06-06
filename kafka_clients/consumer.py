from kafka import KafkaConsumer
from astra.db_api_client import database_connection
import json
import uuid


#getting data from the producer
consumer = KafkaConsumer( "weather",
    bootstrap_servers = "localhost:9092",
    group_id = "weather-group",
    auto_offset_reset = 'earliest',
    value_deserializer = lambda v : json.loads(v.decode('utf-8'))
)

#inserting the topic data to astra db table
database = database_connection()
table = database.get_table("cities_weather")

def run_consumer():
   
    #polling the consumer
    messages = consumer.poll(timeout_ms=1000)

    for tp, msgs in messages.items():
        for msg in msgs:
            for city_weather in msg.value:
                city_weather['id'] = uuid.uuid4()
                table.insert_one(city_weather)
                print("data uploaded!")
