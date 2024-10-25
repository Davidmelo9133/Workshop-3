from kafka import KafkaProducer
import json

# Crear productor Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Datos para enviar
datos = [
    {'Economy (GDP per Capita)': 1.2, 'Family': 1.3, 'Health (Life Expectancy)': 0.9, 'Freedom': 0.8, 'Trust (Government Corruption)': 0.2, 'Generosity': 0.3},
    {'Economy (GDP per Capita)': 1.2, 'Family': 1.3, 'Health (Life Expectancy)': 1.4, 'Freedom': 1.1, 'Trust (Government Corruption)': 0.5, 'Generosity': 0.3}
]

# Enviar datos a Kafka
for dato in datos:
    producer.send('predicciones', value=dato)
    print(f"Mensaje enviado a Kafka: {dato}")

# Cerrar productor
producer.flush()
producer.close()
