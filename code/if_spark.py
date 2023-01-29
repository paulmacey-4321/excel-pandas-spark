from pyspark.sql import SparkSession
from pyspark.sql.functions import when, sum

# Create a SparkSession
spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

# Create a DataFrame from the dataset
data = [("Region 1", 1000, 2000, 3000),
        ("Region 2", 4000, 5000, 6000),
        ("Region 3", 7000, 8000, 9000)]

df = spark.createDataFrame(data, ["Region", "January", "February", "March"])

# Sum the values in the Region 2 column
region2_sum = df.filter(df.Region == "Region 2").agg(sum(df.January + df.February + df.March)).first()[0]

# Use an if-condition to check the sum and return "bonus" or "no bonus"
if region2_sum > 13000:
    print("bonus")
else:
    print("no bonus")
