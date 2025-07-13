from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Ingest JSON to HDFS") \
    .config("spark.hadoop.fs.defaultFS", "hdfs://namenode:9000") \
    .getOrCreate()

tables = ["business", "review", "user", "checkin", "tip"]
for table in tables:
    input_path = f"/data/yelp_academic_dataset_{table}.json"
    output_path = f"/raw_db/{table}"

    print(f"📦 Ingesting {table}...")
    df = spark.read.json(input_path)
    df.write.mode("overwrite").parquet(output_path)
    print(f"✅ Done: {output_path}")
