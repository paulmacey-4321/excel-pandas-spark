from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("IndexMatch").getOrCreate()

# Create a DataFrame from the dataset
data = [("Region 1", 1000, 2000, 3000),
        ("Region 2", 4000, 5000, 6000),
        ("Region 3", 7000, 8000, 9000)]

schema = ["Region", "January", "February", "March"]

df = spark.createDataFrame(data, schema)

# Create a new DataFrame with a lookup value
lookup = spark.createDataFrame([("Region 2", "Region2_Total")], ["Region", "Value"])

# Use the join() function to perform a vlookup
merged_df = df.join(lookup, "Region", "left")

# Print the resulting DataFrame
merged_df.show()

# Using the index/match
df.createOrReplaceTempView("df")
result = spark.sql("SELECT January FROM df WHERE Region = 'Region 2'")
result.show()


or 

result = df.filter("Region == 'Region 2'").select("January")