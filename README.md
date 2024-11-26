# Apache Tez vs Apache Spark Project  

## Description  

This project aims to configure a distributed Big Data environment using Docker to integrate and explore tools for massive data processing and orchestration. The main goal is to execute automated ELT pipelines using Apache Airflow and Tez for data processing while comparing the performance of tools such as Apache Spark, Hive, and Pig.  

The project includes:  
- Configuring a Big Data environment with Docker.  
- Managing workflows with Apache Airflow.  
- Implementing distributed analytical processing (Tez, Hive, Spark, Pig).  
- Comparing the performance of processing engines.  

---

## Objectives  

1. Configure a ready-to-use distributed Big Data environment.  
2. Automate data workflows using Apache Airflow and sensors.  
3. Perform complex analytical processing with Tez, Spark, Hive, and Pig.  
4. Compare the performance of tools and processing engines.  

---

## Prerequisites  

- Docker (version 20.x or later) and Docker Compose (1.27 or later).  
- A machine with at least 8 GB of RAM and 2 vCPUs.  

---

## Installation  

1. Clone the GitHub repository:  

    ```bash
    git clone https://github.com/AbderrahmaneOd/docker-hadoop.git
    cd docker-hadoop
    ```

2. Launch the services defined in `docker-compose.yaml`:  

    ```bash
    docker compose up -d
    ```

3. Verify that all containers are running:  

    ```bash
    docker compose ps -a
    ```

    Key services include:  
    - HDFS Namenode: [http://localhost:50070](http://localhost:50070)  
    - YARN ResourceManager: [http://localhost:8088](http://localhost:8088)  
    - Apache Spark Master: [http://localhost:8080](http://localhost:8080)  
    - Apache Airflow: [http://localhost:8085](http://localhost:8085)  

---

## How to Run a Job  

### 1. Import Data  

Place CSV files into HDFS:  

```bash
docker compose exec namenode hdfs dfs -mkdir -p /input/customers-data
docker compose exec namenode hdfs dfs -put datasets/*.csv /input/customers-data
```
### 2. Orchestrate with Airflow  
- Access the Airflow interface ([http://localhost:8085](http://localhost:8085)).  
- Enable the etl_pipeline_with_tez DAG to execute the pipeline.

### 3. Manually Execute Tasks  
Use the following commands to interact with Airflow via CLI:  
- List DAGs:  
  ``` bash
   airflow dags list
  ```   
- Trigger a DAG:  
  ``` bash
   airflow dags trigger etl_pipeline_with_tez
   ```  
- View task logs:  
  ``` bash
   airflow logs <task_id> <dag_id>
  ``` 

---

## Included Services  
- Apache Hadoop: Distributed system management (HDFS, YARN).  
- Apache Spark: Fast in-memory processing.  
- Apache Hive: SQL query management.  
- Apache Pig: Script-based data transformations.  
- Apache Tez: Workflow optimization for Hadoop.  
- Apache Airflow: Workflow orchestration and management.
