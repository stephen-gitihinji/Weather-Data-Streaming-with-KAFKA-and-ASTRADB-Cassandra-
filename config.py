from dotenv import load_dotenv
import os

load_dotenv()

#configuration for open weather
MY_OPENWEATHER_KEY = os.getenv("OPEN_WEATHER_KEY")

#configuration for astra db

MY_ASTRADB_ENDPOINT = os.getenv("ASTRA_ENDPOINT")
MY_ASTRADB_TOKEN  = os.getenv("ASTRA_TOKEN")
MY_KEYSPACE = os.getenv("ASTRA_KEYSPACE")

