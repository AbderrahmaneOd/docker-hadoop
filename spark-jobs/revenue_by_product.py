from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Initialize Spark session
spark = SparkSession.builder \
    .appName("RevenueByProduct") \
    .master("spark://spark:7077") \
    .getOrCreate()

# Load data from HDFS
orders = spark.read.csv('hdfs://namenode:8020/input/customers-data/orders.csv', header=True, inferSchema=True)
products = spark.read.csv('hdfs://namenode:8020/input/customers-data/products.csv', header=True, inferSchema=True)

# Inspect schemas (optional, for debugging purposes)
orders.printSchema()
products.printSchema()

# Join the data on ProductID
joined = orders.join(products, orders.ProductID == products.ProductID)

# Calculate total revenue per product
revenue = joined.groupBy(col("Name").alias("ProductName")) \
    .agg(expr("SUM(Quantity * Price)").alias("TotalRevenue")) \
    .orderBy(col("TotalRevenue").desc())

# Show the result
revenue.show()


# Save output locally (optional)
# output_path = "output/transformed_data"
# revenue.write.mode("overwrite").csv(output_path)

# Stop the Spark session
# spark.stop()
