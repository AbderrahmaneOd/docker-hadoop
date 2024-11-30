# Hadoop Ecosystem Docker Compose Setup

## Overview

This project provides a containerized Hadoop ecosystem with integrated Big Data processing tools, designed for learning, development, and small-scale testing.

## 🚀 Stack Versions

| Component | Version |
|-----------|---------|
| Hadoop    | 2.7.4   |
| Spark     | 2.4.5   |
| Hive      | 2.3.2   |
| Pig       | 0.17.0  |
| Tez       | 0.9.2   |
| Zeppelin  | 0.9.0   |

## 🎯 Project Objectives

1. Configure a ready-to-use distributed Big Data environment
2. Perform analytical processing with Hive, Pig, Spark, and Tez
3. Compare performance across different processing engines

## 📋 Prerequisites

- Docker and Docker Compose installed
- System with at least 8GB RAM recommended

## 📂 Folder Structure

```
.
├── config-pig/          # Pig configuration files
├── config-tez/          # Tez configuration files
├── datasets/            # Sample CSV datasets
├── pig/                 # Pig Dockerfile
├── tez/                 # Tez Dockerfile
├── spark-jobs/          # Pre-written Spark scripts
├── docker-compose.yaml  # Services definition
└── hadoop.env           # Hadoop environment variables
```

## 🛠 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/AbderrahmaneOd/hadoop-spark-tez-docker.git
cd hadoop-spark-tez-docker
```

### 2. Launch Services

```bash
docker compose up -d
```

### 3. Verify Containers

```bash
docker compose ps -a
```

## 🌐 Web Interfaces

| Service             | URL                        |
|---------------------|----------------------------|
| HDFS Namenode       | http://localhost:50070     |
| YARN ResourceManager| http://localhost:8088      |
| Spark Master        | http://localhost:8080      |
| Zeppelin            | http://localhost:8085      |

## 📊 Data Processing Workflows

### Upload Datasets to HDFS

```bash
docker compose exec namenode hdfs dfs -mkdir -p /input/customers-data
docker compose exec namenode hdfs dfs -put datasets/*.csv /input/customers-data
```

### Hive Jobs

1. Enter Hive server:
```bash
docker compose exec -it hive-server bash
hive
```

2. Create database and load data:
```sql
CREATE DATABASE customer_db;
USE customer_db;
CREATE TABLE users (
    user_id INT, 
    user_name STRING, 
    email STRING, 
    age INT, 
    country STRING
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;

LOAD DATA INPATH '/input/customers-data/users.csv' INTO TABLE users;
SELECT * FROM users LIMIT 5;
```

### Pig Jobs

1. Open Pig container:
```bash
docker compose exec -it pig bash
pig
```

2. Run Pig script:
```pig
users = LOAD '/input/customers-data/users.csv' 
         USING PigStorage(',') 
         AS (user_id:int, user_name:chararray, country:chararray);
DUMP users;
```

### Spark Jobs

1. Enter Spark container:
```bash
docker compose exec -it spark bash
```

2. Example PySpark job:
```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("spark://spark:7077") \
    .appName("RevenueByProduct") \
    .getOrCreate()

orders = spark.read.csv(
    'hdfs://namenode:8020/input/customers-data/orders.csv', 
    header=True, 
    inferSchema=True
)

products = spark.read.csv(
    'hdfs://namenode:8020/input/customers-data/products.csv', 
    header=True, 
    inferSchema=True
)

joined = orders.join(products, "product_id")
revenue = joined.groupBy("product_name") \
    .sum("quantity * price") \
    .orderBy("sum(quantity * price)", ascending=False)

revenue.show()
```

## 🔍 Included Services

- **Apache Hadoop**: Distributed system management (HDFS, YARN)
- **Apache Spark**: Fast in-memory processing
- **Apache Hive**: SQL query management
- **Apache Pig**: Script-based data transformations
- **Apache Tez**: Workflow optimization for Hadoop
