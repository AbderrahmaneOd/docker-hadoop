from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Initialize Spark session
spark = SparkSession.builder \
    .appName("TopSpendersAnalysis") \
    .master("spark://spark:7077") \
    .getOrCreate()

# Load data from HDFS
users = spark.read.csv('hdfs://namenode:8020/input/customers-data/users.csv', header=True, inferSchema=True)
products = spark.read.csv('hdfs://namenode:8020/input/customers-data/products.csv', header=True, inferSchema=True)
orders = spark.read.csv('hdfs://namenode:8020/input/customers-data/orders.csv', header=True, inferSchema=True)

# Inspect schemas
# users.printSchema()
# products.printSchema()
# orders.printSchema()

# Join data
joined = orders.join(products, orders.ProductID == products.ProductID)
joined_with_users = joined.join(users, joined.UserID == users.UserID)

# Calculate total spent by each user
total_spent = joined_with_users.groupBy(col("Name").alias("UserName")) \
    .agg(expr("SUM(Quantity * Price)").alias("TotalSpent")) \
    .orderBy(col("TotalSpent").desc())

# Limit to the top 10 users
top_users = total_spent.limit(10)

# Display the result
top_users.show()
