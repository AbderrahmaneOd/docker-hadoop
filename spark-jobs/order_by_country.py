from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder \
    .appName("OrderByCountry") \
    .master("spark://spark:7077") \
    .getOrCreate()

# Load data
users = spark.read.csv('hdfs://namenode:8020/input/customers-data/users.csv', header=True, inferSchema=True)
orders = spark.read.csv('hdfs://namenode:8020/input/customers-data/orders.csv', header=True, inferSchema=True)

# Inspect schemas
# users.printSchema()
# orders.printSchema()

# Join the data on UserID
joined = orders.join(users, orders.UserID == users.UserID)

# Calculate the total number of orders per country
order_count = joined.groupBy(col("Country")) \
    .count() \
    .withColumnRenamed("count", "TotalOrders") \
    .orderBy(col("TotalOrders"), ascending=False)

# Display the result
order_count.show()
