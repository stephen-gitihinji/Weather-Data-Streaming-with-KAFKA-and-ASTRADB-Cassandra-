from astra.table_definition import create_table
from kafka_clients.producer import run_producer
from kafka_clients.consumer import run_consumer
import logging
import time

logger = logging.getLogger(__name__)

def main():
    logger.info("Starting application")
    try:
        create_table()
        while True:
            run_producer()
            run_consumer()
            time.sleep(30)
    except Exception as e:
        logging.exception("There was a problem running the application!", e)

if __name__ == "__main__":
    main()