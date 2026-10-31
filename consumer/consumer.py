from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "topic-apple",
    "topic-microsoft",
    "topic-google",
    "topic-amazon",
    "topic-tesla",
    bootstrap_servers=['kafka:9092'],
    group_id="file-writer-group",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

files = {
    "APPLE": open("APPLE.txt", "a"),
    "MICROSOFT": open("MICROSOFT.txt", "a"),
    "GOOGLE": open("GOOGLE.txt", "a"),
    "AMAZON": open("AMAZON.txt", "a"),
    "TESLA": open("TESLA.txt", "a")
}
for msg in consumer:
    data = msg.value
    line = (
        f"{data['timestamp']} | "
        f"{data['key']} | "
        f"{data['value']}\n"
    )
    files[data["key"]].write(line)
    files[data["key"]].flush()
    print("Written:", line.strip())

