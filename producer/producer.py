from kafka import KafkaProducer
from datetime import datetime
import random
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

keys = [
    "APPLE",
    "MICROSOFT",
    "GOOGLE",
    "AMAZON",
    "TESLA"
]
while True:
    key = random.choice(keys)
    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "key": key,
        "value": random.randint(1, 1000)
    }
    topic_name = f"topic-{key.lower()}"
    producer.send(topic_name, data)
    print(f"Sent => {data}")
    producer.flush()
    time.sleep(10)

