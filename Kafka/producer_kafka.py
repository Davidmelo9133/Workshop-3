from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

datos = {
    'Economy (GDP per Capita)': 1.2,
    'Family': 1.3,
    'Health (Life Expectancy)': 0.9,
    'Freedom': 0.8,
    'Trust (Government Corruption)': 0.2,
    'Generosity': 0.3
}

producer.send('predicciones', datos)
print("Datos enviados a Kafka...")

time.sleep(5)
