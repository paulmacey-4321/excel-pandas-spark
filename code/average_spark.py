from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

# Create a DataFrame from the dataset
data = [("Region 1", 1000, 2000, 3000),
        ("Region 2", 4000, 5000, 6000),
        ("Region 3", 7000, 8000, 9000)]

df = spark.createDataFrame(data, ["Region", "January", "February", "March"])

# Calculate the average sales for January
january_avg = df.selectExpr("avg(January)").collect()[0][0]
print(january_avg)