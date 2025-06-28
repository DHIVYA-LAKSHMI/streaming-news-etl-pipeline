from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructField, StructType, StringType

import os
# Include necessary Kafka and AWS support JARs
os.environ['PYSPARK_SUBMIT_ARGS'] = (
    '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0,'
    'org.apache.hadoop:hadoop-aws:3.3.2 pyspark-shell'
)

# ✅ Define schema for NewsAPI articles
schema = StructType([
    StructField("source", StructType([
        StructField("id", StringType(), True),
        StructField("name", StringType(), True)
    ])),
    StructField("author", StringType(), True),
    StructField("title", StringType(), True),
    StructField("description", StringType(), True),
    StructField("url", StringType(), True),
    StructField("publishedAt", StringType(), True),
    StructField("content", StringType(), True)
])

# ✅ Create Spark Session with S3 support
spark = SparkSession.builder \
    .appName("NewsStreamToS3") \
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem") \
    .config("spark.hadoop.fs.s3a.aws.credentials.provider", "com.amazonaws.auth.DefaultAWSCredentialsProviderChain") \
    .getOrCreate()

spark.sparkContext.setLogLevel("WARN")

# ✅ Read from Kafka topic
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "news-topic") \
    .load()

# ✅ Parse JSON string and extract fields
parsed_df = df.selectExpr("CAST(value AS STRING) as json_string") \
    .select(from_json(col("json_string"), schema).alias("data")) \
    .select(
        "data.publishedAt",
        "data.title",
        "data.description",
        "data.source.name"
    )

# ✅ Write parsed news data to S3 bucket in CSV format
query = parsed_df.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "s3a://news-etl-dhivya/news-data/") \
    .option("checkpointLocation", "s3a://news-etl-dhivya/checkpoints/news-stream/") \
    .option("header", True) \
    .start()

query.awaitTermination()
