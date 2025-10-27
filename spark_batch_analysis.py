from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# Inicializar Spark
spark = SparkSession.builder \
    .appName("AccidentalidadAnalysis") \
    .getOrCreate()

# Leer el dataset
df = spark.read.option("header", "true").option("quote", "\"").csv("/home/vboxuser/datos/accidentalidad/accidentes_2017_2022.csv")

# Mostrar esquema y datos
print("=== ESQUEMA ===")
df.printSchema()

print("=== PRIMERAS 10 FILAS ===")
df.show(10)

print("=== CONTEOS POR GRAVEDAD ===")
df.groupBy("gravedad").count().show()

# Limpieza y transformaciones
df_clean = df \
    .withColumn("fecha", to_timestamp(col("fecha"), "yyyy-MM-dd'T'HH:mm:ss.SSS")) \
    .withColumn("año", col("a_o").cast(IntegerType())) \
    .withColumn("mes_num", col("mes").cast(IntegerType())) \
    .withColumn("hora", hour(col("fecha"))) \
    .drop("a_o")  # Eliminar columna con nombre problemático

# Análisis exploratorio
print("=== ACCIDENTES POR AÑO ===")
df_clean.groupBy("año").count().orderBy("año").show()

print("=== ACCIDENTES POR DÍA DE LA SEMANA ===")
df_clean.groupBy("dia").count().orderBy(desc("count")).show()

print("=== ACCIDENTES POR HORA DEL DÍA ===")
df_clean.groupBy("hora").count().orderBy("hora").show()

print("=== DISTRIBUCIÓN POR GRAVEDAD Y AÑO ===")
df_clean.groupBy("año", "gravedad").count().orderBy("año", desc("count")).show()

# Guardar resultados
df_clean.write.mode("overwrite").parquet("/home/vboxuser/resultados/accidentalidad_clean")

print("=== ANÁLISIS COMPLETADO ===")
