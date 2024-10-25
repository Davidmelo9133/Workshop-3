from kafka import KafkaConsumer
import json
import pickle
import numpy as np
import mysql.connector

def conectar_mysql():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="workshop_ml"
    )
    return conn

def guardar_predicciones_mysql(X_test, y_pred):
    conn = conectar_mysql()
    cursor = conn.cursor()
    
    for i in range(len(y_pred)):
        query = """
        INSERT INTO predicciones (economy_gdp, family, health_life_expectancy, freedom, trust_government_corruption, generosity, happiness_score_predicho)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (float(X_test[i][0]), float(X_test[i][1]), float(X_test[i][2]), float(X_test[i][3]), float(X_test[i][4]), float(X_test[i][5]), float(y_pred[i]))
        cursor.execute(query, values)

    conn.commit()
    cursor.close()
    conn.close()
    print("Predicciones guardadas exitosamente en la base de datos.")

consumer = KafkaConsumer(
    'predicciones',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_deserializer=lambda x: x.decode('utf-8') if x else None
)
#Remplaza tu ruta para tu archivo
with open('C:/Users/Admin/Desktop/SEMESTRE 2024-2/ETL/Workshop_#3/Model/random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

print("Esperando datos de Kafka...")

for message in consumer:
    try:
        if message.value:  
            print(f"Mensaje en bruto recibido: {message.value}")
            try:
                datos = json.loads(message.value)
                print(f"Datos recibidos de Kafka: {datos}")

                X = np.array([[  
                    datos['Economy (GDP per Capita)'],
                    datos['Family'],
                    datos['Health (Life Expectancy)'],
                    datos['Freedom'],
                    datos['Trust (Government Corruption)'],
                    datos['Generosity']
                ]])

                
                prediccion = model.predict(X)
                print(f"Predicción: {prediccion[0]}")

               
                guardar_predicciones_mysql(X, prediccion)

            except json.JSONDecodeError:
                print(f"Error al decodificar JSON: {message.value}")
        else:
            print("Mensaje vacío recibido.")
    except Exception as e:
        print(f"Error procesando el mensaje: {e}")
