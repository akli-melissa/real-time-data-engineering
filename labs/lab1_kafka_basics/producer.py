from kafka import KafkaProducer
import json, random, time

TOPIC = "hashtag_stream"
hashtags = ["#ai", "#ml", "#data", "#python", "#stream"]

def main():
    producer = KafkaProducer(
        bootstrap_servers=["localhost:9092"],
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )
    print(f"Producing messages to topic '{TOPIC}'...")
    try:
        while True:
            msg = {"tag": random.choice(hashtags), "ts": time.time()}
            producer.send(TOPIC, value=msg)
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Stopped.")
    finally:
        producer.flush()
        producer.close()

if __name__ == "__main__":
    main()
