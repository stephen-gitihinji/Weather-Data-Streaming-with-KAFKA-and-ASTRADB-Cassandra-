import requests as req
from kafka import KafkaProducer
import pandas as pd
import os
from dotenv import load_dotenv
import json
import time
import uuid
from datetime import datetime
from config import MY_OPENWEATHER_KEY

load_dotenv()

#extracting data from open weather 
def extract_weather():
    api_key = MY_OPENWEATHER_KEY

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    cities = ['nairobi', 'kisumu', 'eldoret', 'nakuru', 'mombasa']
    # test_city = cities[0]
    weather = []
    for city in cities:
        parameters = {
            'q':city,
            'appid':api_key
        }
        #getting the data
        weather.append(req.get(BASE_URL, params = parameters))
    return weather

#Transforming the extracted data to remain with what we need
def transform_data(raw_data):
    weather_data = pd.DataFrame()
    for city_weather in raw_data:
        extracted_data = pd.json_normalize(city_weather.json())

        required_data = extracted_data[['name','sys.country','main.temp', 'main.pressure',
                                    'main.humidity', 'wind.speed',]]
        required_data = required_data.rename(columns= {'name':'city', 'sys.country':'country','main.temp':'temperature','main.pressure':'pressure', 'main.humidity':'humidity','wind.speed':'wind_speed'})
        required_data['id'] = str(uuid.uuid4())
        required_data['timestamp'] = datetime.now().replace(microsecond=0).isoformat(sep=' ')
        weather_data = pd.concat([weather_data, required_data], ignore_index = True)
    return weather_data

#loading the data to a topic for streaming
def stream_data(transformed_data):
    topic = 'weather'
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: v.to_json(orient="records").encode('utf-8')
    )

    producer.send(topic, transformed_data)
    print('data has been streamed!')

def run_producer():
    raw_data = extract_weather()
    transformed_data = transform_data(raw_data)
    stream_data(transformed_data)
