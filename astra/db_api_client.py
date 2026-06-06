from astrapy import DataAPIClient, Database
import os
from dotenv import load_dotenv
from config import MY_ASTRADB_ENDPOINT, MY_ASTRADB_TOKEN, MY_KEYSPACE

load_dotenv()

def database_connection() -> Database:
    endpoint = MY_ASTRADB_ENDPOINT
    token = MY_ASTRADB_TOKEN
    keyspace = MY_KEYSPACE

    if not endpoint or not token:
        raise RuntimeError(
            "An endpoint and token are required to connect to the database."
        )

    client = DataAPIClient()
    database = client.get_database(endpoint, token= token, keyspace= keyspace)
    print("Conection Successful!")

    return database