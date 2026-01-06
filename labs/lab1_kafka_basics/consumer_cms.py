from kafka import KafkaConsumer
import json
from cms import CountMinSketch

TOPIC = "hashtag_stream"
THRESHOLD = 100

def main():
    cms = CountMinSketch(d=5, w=2000)
    heavy = set()
    total = 0

    consumer = KafkaConsumer(
        TOPIC,
        bootstrap_servers=["localhost:9092"],
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        value_deserializer=lambda v: json.loads(v.decode()),
    )

    print(f"Consuming from '{TOPIC}'...")
    for msg in consumer:
        tag = msg.value.get("tag")
        if tag is None:
            continue
        total += 1
        cms.update(tag)
        est = cms.estimate(tag)
        if est >= THRESHOLD and tag not in heavy:
            heavy.add(tag)
            print(f"[HEAVY HITTER] {tag} ~ {est} ({est/total*100:.2f}%)")

if __name__ == "__main__":
    main()
