#!/bin/bash

# HDFS path for Tez library
HDFS_TEZ_PATH="/apps/tez-0.9.2/tez-0.9.2.tar.gz"

# Check if the file already exists in HDFS
hdfs dfs -test -e "$HDFS_TEZ_PATH"

# If the file doesn't exist, upload it
if [ $? -ne 0 ]; then
  echo "Initializing Tez: Creating directory and uploading Tez libraries to HDFS..."
  hdfs dfs -mkdir -p /apps/tez-0.9.2
  hdfs dfs -put /opt/tez/share/tez.tar.gz "$HDFS_TEZ_PATH"
else
  echo "Tez initialization skipped: Tez libraries already exist in HDFS."
fi