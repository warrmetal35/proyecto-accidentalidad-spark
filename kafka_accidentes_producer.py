import time
import json
import random
from kafka import KafkaProducer
import pandas as pd

# Leer el dataset original para tomar muestras
df = pd.read_csv('/home/vboxuser/datos/accidentalidad/accidentes_2017_2022.csv')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

print("Enviando datos de accidentalidad a Kafka...")

while True:
    # Tomar una fila aleatoria del dataset
    accidente = df.sample(1).iloc[0]
    mensaje = {
        "orden": int(accidente['orden']),
        "ipat": accidente['ipat'],
        "fecha": accidente['fecha'],
        "gravedad": accidente['gravedad'],
        "dia": accidente['dia'],
        "timestamp_stream": int(time.time())
    }
    producer.send('accidentes_stream', value=mensaje)
    print(f"Enviado: {mensaje['ipat']} - {mensaje['gravedad']}")
    time.sleep(5)  # Enviar cada 5 segundos
