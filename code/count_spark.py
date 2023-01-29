from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

# Create a DataFrame from the dataset
data = [("Region 1", 1000, 2000, 3000),
        ("Region 2", 4000, 5000, 6000),
        ("Region 3", 7000, 8000, 9000)]

df = spark.createDataFrame(data, ["Region", "January", "February", "March"])

# Count the number of non-null values in the January column
january_count = df.filter(df["January"].isNotNull()).count()
print(january_count)