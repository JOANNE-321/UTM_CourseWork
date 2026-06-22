from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("CSV to Processed CSV") \
    .getOrCreate()

input_path = "data/raw/school_census_sample.csv"
output_path = "data/parquet/school_census"

df = spark.read.csv(input_path, header=True, inferSchema=True)

print("CSV schema:")
df.printSchema()

print("CSV preview:")
df.show(5)

df.coalesce(1).write.mode("overwrite").option("header", True).csv(output_path)

print(f"Processed CSV saved to: {output_path}")

spark.stop()