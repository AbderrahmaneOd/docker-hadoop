from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum

# Initialize Spark session
spark = SparkSession.builder \
    .appName("OrderByCategory") \
    .master("spark://spark:7077") \
    .getOrCreate()

# Load data from HDFS
categories = spark.read.csv('hdfs://namenode:8020/input/customers-data/categories.csv', header=True, inferSchema=True)
products = spark.read.csv('hdfs://namenode:8020/input/customers-data/products.csv', header=True, inferSchema=True)
orders = spark.read.csv('hdfs://namenode:8020/input/customers-data/orders.csv', header=True, inferSchema=True)

# Inspect schemas
# categories.printSchema()
# products.printSchema()
# orders.printSchema()

# Join the data
joined = orders.join(products, orders.ProductID == products.ProductID)
joined_with_categories = joined.join(categories, joined.CategoryID == categories.CategoryID)

# Calculate the most ordered products by category
product_count = joined_with_categories.groupBy(
    col("CategoryName"), col("Name").alias("ProductName")
).agg(
    spark_sum("Quantity").alias("TotalQuantity")
).orderBy(
    col("CategoryName"), col("TotalQuantity").desc()
)

# Display the result
product_count.show()
