# Machine Learning and Data Streaming Workshop

## Estructura del Proyecto

Este repositorio contiene la implementación de un modelo de Machine Learning y la integración de Kafka para la transmisión de datos, junto con MySQL para almacenar las predicciones. Los modelos de Random Forest y Árbol de Decisión se entrenan en un conjunto de datos de puntuaciones de felicidad en varios países. Las predicciones se producen a través de Kafka y se almacenan en una base de datos MySQL.

### Estructura de Carpetas
```
Data/
    2015.csv
    2016.csv
    2017.csv
    2018.csv
    2019.csv
    dataset_combinado.csv
Kafka/
    consumer_kafka.py
    producer_kafka.py
    producer_kafka_predictions.py
Model/
    decision_tree_model.pkl
    random_forest_model.pkl
Notebooks/
    EDA_YEARS.ipynb
    Model_Training_Arbol.ipynb
    Model_Training_RandomForest.ipynb
db_operations/
    DB_OPERATIONS.ipynb
    Verificacion.ipynb
requirements.txt
.gitignore
README.md
```

### Explicación de Archivos:

#### 1. Carpeta Data
- **2015.csv a 2019.csv**: Datos de diferentes años utilizados para analizar la puntuación de felicidad a lo largo del tiempo.
- **dataset_combinado.csv**: El conjunto de datos combinado de todos los años para el entrenamiento y prueba final.

#### 2. Carpeta Kafka
- **consumer_kafka.py**: Consumidor de Kafka que escucha mensajes del tema "predicciones" y realiza predicciones utilizando el modelo de Random Forest preentrenado.
- **producer_kafka.py**: Productor de Kafka para enviar mensajes de muestra al tema "predicciones".
- **producer_kafka_predictions.py**: Productor de Kafka que envía datos relacionados con las predicciones al tema "predicciones".

#### 3. Carpeta Model
- **decision_tree_model.pkl**: Modelo de Árbol de Decisión preentrenado.
- **random_forest_model.pkl**: Modelo de Random Forest preentrenado.

#### 4. Carpeta Notebooks
- **EDA_YEARS.ipynb**: Notebook de Análisis Exploratorio de Datos para visualizar las puntuaciones de felicidad de los conjuntos de datos.
- **Model_Training_Arbol.ipynb**: Notebook para entrenar el modelo de Árbol de Decisión.
- **Model_Training_RandomForest.ipynb**: Notebook para entrenar el modelo de Random Forest.

#### 5. Carpeta db_operations
- **DB_OPERATIONS.ipynb**: Notebook para crear la base de datos MySQL y la tabla para almacenar las predicciones.
- **Verificacion.ipynb**: Notebook para verificar que las predicciones se almacenan correctamente en MySQL después de ser procesadas por Kafka.

### Cómo Ejecutar el Proyecto

1. **Instalar las dependencias requeridas** ejecutando:
     ```bash
     pip install -r requirements.txt
     ```

2. **Ejecutar la configuración de MySQL**:
     - Crear una base de datos llamada `workshop_ml` ejecutando los comandos en el notebook `DB_OPERATIONS.ipynb`.

3. **Configuración de Kafka**:
     - Iniciar los servicios de Zookeeper y Kafka usando los siguientes comandos (asumiendo que Kafka está instalado):
         ```bash
         zookeeper-server-start.bat ../config/zookeeper.properties
         kafka-server-start.bat ../config/server.properties
         ```
     - Crear un tema de Kafka llamado `predicciones`:
         ```bash
         kafka-topics.bat --create --topic predicciones --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
         ```

4. **Ejecutar el Productor de Kafka** para enviar datos de predicciones:
     ```bash
     python Kafka/producer_kafka_predictions.py
     ```

5. **Ejecutar el Consumidor de Kafka** para escuchar las predicciones y almacenarlas en MySQL:
     ```bash
     python Kafka/consumer_kafka.py
     ```

6. **Verificar que los datos se almacenen** revisando la tabla en la base de datos MySQL usando `Verificacion.ipynb`.

### Autor
David Melo Valbuena

