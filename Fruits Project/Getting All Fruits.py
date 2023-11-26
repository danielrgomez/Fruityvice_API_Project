# Databricks notebook source
# DBTITLE 1,Get JSON Response and set to object
import requests
import json
import datetime

from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType,BooleanType,DoubleType
from pyspark.sql import functions as Function
from pyspark.sql.functions import lit
#import pyspark.sql.functions as F

#from pyspark.sql import SQLContext as sc

res = requests.get('https://www.fruityvice.com/api/fruit/all')
json_response = json.loads(res.text)

# COMMAND ----------

spark = SparkSession.builder \
    .master("local[1]") \
    .appName("PySpark Read JSON") \
    .getOrCreate()

# COMMAND ----------

df = spark.read.json(sc.parallelize([json_response]))
df.show(truncate=False)

# COMMAND ----------

# DBTITLE 1,Adds multilines from JSON request as new columns to the DF
df = df.withColumn("calories",df["nutritions.calories"])
df = df.withColumn("carbohydrates",df["nutritions.carbohydrates"])
df = df.withColumn("fat",df["nutritions.fat"])
df = df.withColumn("protein",df["nutritions.protein"])
df = df.withColumn("sugar",df["nutritions.sugar"])

df.show()

# COMMAND ----------

# DBTITLE 1,Add timestamp to the dataframe
df=df.withColumn('current_timestamp',Function.current_timestamp())

# COMMAND ----------

# DBTITLE 1,Drop nutritions column
df = df.drop("nutritions")

# COMMAND ----------

# DBTITLE 1,Append transformations to table all_fruits_tbl
df.write.mode("append").saveAsTable("learn_data_engineering.default.all_fruits_tbl")
