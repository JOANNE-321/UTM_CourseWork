from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.functions import monotonically_increasing_id

spark = SparkSession.builder \
    .appName("Transform Star Schema") \
    .getOrCreate()

# Read the original CSV directly to avoid Windows Hadoop folder-listing error
input_path = "data/raw/school_census_sample.csv"

df = spark.read.csv(input_path, header=True, inferSchema=True)

print("Input schema:")
df.printSchema()

print("Input preview:")
df.show(5)

# Basic cleaning
df = df.dropDuplicates()

df = df.na.fill({
    "student_count": 0,
    "teacher_count": 0,
    "school_type": "Unknown",
    "education_stage": "Unknown",
    "region": "Unknown",
    "state": "Unknown",
    "city": "Unknown"
})

# Dimension table: Year
dim_year = df.select("year").distinct() \
    .withColumn("year_id", monotonically_increasing_id())

# Dimension table: School
dim_school = df.select(
    "school_id",
    "school_name",
    "school_type"
).distinct()

# Dimension table: Location
dim_location = df.select(
    "region",
    "state",
    "city"
).distinct().withColumn("location_id", monotonically_increasing_id())

# Dimension table: Education Stage
dim_education_stage = df.select("education_stage").distinct() \
    .withColumn("education_stage_id", monotonically_increasing_id())

# Fact table
fact_school_census = df.join(dim_year, on="year", how="left") \
    .join(dim_location, on=["region", "state", "city"], how="left") \
    .join(dim_education_stage, on="education_stage", how="left") \
    .select(
        "year_id",
        "school_id",
        "location_id",
        "education_stage_id",
        "student_count",
        "teacher_count"
    )

print("dim_year")
dim_year.show()

print("dim_school")
dim_school.show()

print("dim_location")
dim_location.show()

print("dim_education_stage")
dim_education_stage.show()

print("fact_school_census")
fact_school_census.show()

# Save outputs using Pandas instead of Spark writer
# This avoids the Windows Hadoop NativeIO error
output_base = Path("data/output")
output_base.mkdir(parents=True, exist_ok=True)

dim_year.toPandas().to_csv(output_base / "dim_year.csv", index=False)
dim_school.toPandas().to_csv(output_base / "dim_school.csv", index=False)
dim_location.toPandas().to_csv(output_base / "dim_location.csv", index=False)
dim_education_stage.toPandas().to_csv(output_base / "dim_education_stage.csv", index=False)
fact_school_census.toPandas().to_csv(output_base / "fact_school_census.csv", index=False)

print("Star schema transformation complete.")
print("Output CSV files saved in data/output/")

spark.stop()