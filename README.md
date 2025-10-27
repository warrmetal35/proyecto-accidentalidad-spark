# Sistema de Análisis de Accidentalidad con Apache Spark y Kafka

## 🎯 Descripción del Proyecto
Este proyecto implementa una solución completa de análisis de datos para el monitoreo y estudio de accidentalidad vial. Combina técnicas de procesamiento batch para análisis histórico y streaming en tiempo real para la detección inmediata de patrones y tendencias. La solución permite a entidades gubernamentales y organizaciones de seguridad vial tomar decisiones basadas en datos tanto históricos como en tiempo real.

## 📊 Contexto del Problema
La accidentalidad vial representa un desafío significativo en seguridad pública y salud. Este sistema aborda la necesidad de:
- **Análisis histórico**: Identificar patrones estacionales, zonas de alto riesgo y factores contribuyentes en datos acumulados
- **Monitoreo en tiempo real**: Detectar incrementos súbitos en accidentalidad, correlacionar eventos y generar alertas tempranas
- **Visualización integral**: Proporcionar insights accionables para políticas de prevención y optimización de recursos de emergencia

## 🏗️ Arquitectura del Sistema

### Diagrama de Flujo de Datos

Fuente de Datos Históricos (CSV)
↓
Spark Batch Processing
↓
Análisis Exploratorio (EDA)
↓
Modelos de Tendencia

Generador Simulado de Eventos
↓
Apache Kafka (Message Broker)
↓
Spark Streaming Processing
↓
Dashboard Tiempo Real + Alertas

### Componentes Principales
1. **Capa de Ingesta**: Kafka como buffer de mensajes para datos en tiempo real
2. **Capa de Procesamiento**: Spark para transformaciones complejas y agregaciones
3. **Capa de Almacenamiento**: Parquet para datos limpios y resultados de análisis
4. **Capa de Visualización**: Consola Spark UI y outputs estructurados

## 🛠️ Stack Tecnológico Detallado

### Procesamiento de Datos
- **Apache Spark 3.5.0**: Motor de procesamiento distribuido para operaciones batch y streaming
- **Spark SQL**: Consultas estructuradas y optimizaciones Catalyst
- **Structured Streaming**: Procesamiento en tiempo real con semántica exactly-once

### Mensajería y Tiempo Real
- **Apache Kafka 3.7.2**: Plataforma de streaming distribuida para ingesta de eventos
- **Kafka Producers/Consumers**: Client libraries para Python y Spark integration

### Lenguajes y Librerías
- **Python 3**: Lenguaje principal de desarrollo
- **PySpark**: API de Python para Spark
- **Pandas**: Procesamiento de datos en memoria para el generador
- **JSON**: Serialización de mensajes entre componentes

## 📁 Estructura del Proyecto
proyecto-accidentalidad-spark/
│
├── data/
│ ├── raw/accidentes_2017_2022.csv # Dataset original
│ └── processed/ # Resultados EDA
│
├── src/
│ ├── batch/
│ │ └── spark_batch_analysis.py # Análisis histórico
│ ├── streaming/
│ │ ├── kafka_accidentes_producer.py # Generador eventos
│ │ └── spark_streaming_consumer.py # Procesamiento real-time
│ └── utils/
│ └── config.py # Configuraciones
│
├── results/
│ ├── accidentalidad_clean/ # Datos procesados
│ └── analysis_reports/ # Reportes generados
│
├── docs/
│ ├── architecture_diagram.png
│ └── setup_instructions.md
│
└── README.md

## 🚀 Guía de Instalación y Configuración

### Prerrequisitos del Sistema

# Versiones requeridas
Java 11+, Python 3.8+, Apache Spark 3.5+, Kafka 3.7+

# Instalación de dependencias Python
pip install kafka-python==2.0.2
pip install pandas==1.5.3
pip install pyspark==3.5.0

Configuración de Entorno

# Variables de entorno requeridas
export SPARK_HOME=/opt/spark
export KAFKA_HOME=/opt/kafka
export PATH=$PATH:$SPARK_HOME/bin:$KAFKA_HOME/bin

💻 Ejecución del Sistema
Fase 1: Procesamiento Batch (Análisis Histórico)

# Ejecutar análisis exploratorio sobre datos históricos
spark-submit spark_batch_analysis.py

# Este script realiza:
 - Limpieza y transformación de datos crudos
 - Análisis de distribución temporal (años, meses, horas)
 - Agregaciones por gravedad y patrones estacionales
 - Generación de datasets listos para reporting

Fase 2: Procesamiento Streaming (Tiempo Real)
# Paso 2.1: Iniciar el generador de eventos de accidentalidad
python3 kafka_accidentes_producer.py

# Este componente:
 - Lee el dataset histórico y simula eventos en tiempo real
 - Publica mensajes JSON al topic de Kafka cada 5 segundos
 - Incluye metadatos completos de cada accidente simulado

# Paso 2.2: Iniciar el consumidor Spark Streaming
spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1 spark_streaming_consumer.py

# Este componente:
 - Se suscribe al topic de Kafka y consume mensajes
 - Aplica ventanas deslizantes de 1 minuto para agregaciones
 - Calcula métricas en tiempo real por gravedad de accidente
 - Output continuo a consola con estadísticas actualizadas

Fase 3: Monitoreo y Visualización
# Acceder a la interfaz web de Spark
http://localhost:4040 (se reemplazo por mi ip)

# La UI proporciona:
 - Métricas de ejecución de jobs en tiempo real
 - Monitoring de recursos y performance
 - Debugging de operaciones de streaming

📊 Resultados y Análisis de Datos
Hallazgos del Análisis Batch
El procesamiento histórico reveló patrones significativos en la accidentalidad:

Distribución Temporal:
Tendencia anual de accidentes por gravedad
Patrones estacionales por meses del año
Horarios pico de incidencia de accidentes
Segmentación por Gravedad:
Proporción entre accidentes con heridos vs solo daños materiales
Correlación entre factores temporales y severidad
Métricas en Tiempo Real
El sistema de streaming permite:

Agregaciones Continuas:
Conteo de accidentes por ventanas de 1 minuto
Distribución en tiempo real por tipo de gravedad
Detección de picos anómalos en la frecuencia

Visualización Operacional:
Dashboard actualizado cada batch de procesamiento
Tracking de throughput del sistema
Latencia de procesamiento end-to-end

🖼️ Evidencias de Ejecución

#Captura 1: Pipeline de Ingesta en Tiempo Real
(https://github.com/warrmetal35/proyecto-accidentalidad-spark/blob/main/producer_kafka.png.png)
Kafka Producer generando eventos de accidentalidad simulados cada 5 segundos

