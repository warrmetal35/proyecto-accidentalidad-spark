from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder \
    .appName("AccidentesStreaming") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# Esquema para los datos de accidentes
schema = StructType([
    StructField("orden", IntegerType()),
    StructField("ipat", StringType()),
    StructField("fecha", StringType()),
    StructField("gravedad", StringType()),
    StructField("dia", StringType()),
    StructField("timestamp_stream", IntegerType())
])

# Leer desde Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "accidentes_stream") \
    .load()

# Parsear JSON
parsed_df = df.select(
    from_json(col("value").cast("string"), schema).alias("data")
).select("data.*")

# Convertir timestamp
parsed_df = parsed_df.withColumn("timestamp", col("timestamp_stream").cast("timestamp"))

# Análisis en tiempo real - Conteo por gravedad cada 1 minuto
conteo_gravedad = parsed_df \
    .groupBy(
        window(col("timestamp"), "1 minute"),
        "gravedad"
    ) \
    .count() \
    .orderBy("window")

# Escribir resultados
query = conteo_gravedad \
    .writeStream \
    .outputMode("complete") \
    .format("console") \
    .option("truncate", "false") \
    .start()

query.awaitTermination()
