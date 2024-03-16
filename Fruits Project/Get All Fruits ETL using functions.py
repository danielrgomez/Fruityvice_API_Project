# Databricks notebook source
# Whole ETL Process

#Function calls the fruityvice api and loads the json response to a variable which is then returned.
def extract_all_fruits():
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
    return json_response
    
#The function transforms the json response from the previous function. It takes the multilines from the nutrition dictionary and adds each as a separate field in the dataframe
def transform_json_response(response):
    #Create sparksession and set it to object called spark
    spark = SparkSession.builder \
    .master("local[1]") \
    .appName("PySpark Read JSON") \
    .getOrCreate()
    
    #Read dataframe  and set to object called df
    df = spark.read.json(sc.parallelize([json_response]))
    df.show(truncate=False)

    #Add multilines as new fields pyspark dataframe
    df = df.withColumn("calories",df["nutritions.calories"])
    df = df.withColumn("carbohydrates",df["nutritions.carbohydrates"])
    df = df.withColumn("fat",df["nutritions.fat"])
    df = df.withColumn("protein",df["nutritions.protein"])
    df = df.withColumn("sugar",df["nutritions.sugar"])

    #Add timesstamp column to dataframe
    df=df.withColumn('current_timestamp',Function.current_timestamp())

    #Drop Nutritions column from dataframe
    df = df.drop("nutritions")
    return df

# The function loads the transformed data into the all_fruits_tbl in Databricks.
def load_dataframe_to_tbl(df):
    df.write.mode("append").saveAsTable("learn_data_engineering.default.all_fruits_tbl")





# Each function is ran one at a time. In order Extract, Transform, and Load. ----------

#Extract all fruits
extract_all_fruits()
json_request = extract_all_fruits()
print("Data Extracted")

#Transform Data
transformed_data = transform_json_response(json_request)
print("Data Transformed")

#Load Data to Table
load_dataframe_to_tbl(transformed_data)
print("Data Loaded")
