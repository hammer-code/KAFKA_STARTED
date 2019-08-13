from kafka import KafkaProducer
import json
import os

KAFKA_HOST = os.getenv("KAFKA_HOST", "localhost")
KAFKA_PORT = os.getenv("KAFKA_PORT", "9092")
BROKER = KAFKA_HOST+":"+KAFKA_PORT
def get_producer():
    try:
        producer = KafkaProducer(
                        bootstrap_servers=[BROKER],
                        value_serializer=lambda m: json.dumps(m).encode('utf-8'))
    except Exception as e:
        print(e)
        exit()
    else:
        return producer