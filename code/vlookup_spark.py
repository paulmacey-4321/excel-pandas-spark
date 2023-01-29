from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

# Create a DataFrame from the dataset
data = [("Region 1", 1000, 2000, 3000),
        ("Region 2", 4000, 5000, 6000),
        ("Region 3", 7000, 8000, 9000)]
df = spark.createDataFrame(data, ["Region", "January", "February", "March"])

# Create a new DataFrame with a lookup value
lookup = spark.createDataFrame([("Region 2", "Region2_Total")], ["Region", "Lookup"])

# Use the join() function to perform a vlookup
merged_df = df.join(lookup, "Region", "left")

# Print the resulting DataFrame
merged_df.show()