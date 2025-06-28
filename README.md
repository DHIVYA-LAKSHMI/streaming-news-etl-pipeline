# Real-Time News ETL Pipeline

This project demonstrates a **real-time ETL pipeline** built with Apache Kafka and Apache Spark Streaming on AWS.  
It ingests live news articles from NewsAPI, streams them through Kafka, processes them in Spark, and stores the output in Amazon S3.

---

## 🚀 Project Overview

This pipeline is designed to simulate how media companies or data engineering teams process high-velocity news streams:

✅ **Fetch Data**  
Python producer pulls the latest headlines from NewsAPI.

✅ **Stream Data**  
Producer pushes data into a Kafka topic (`news-topic`).

✅ **Process Data**  
Spark Structured Streaming reads from Kafka, parses JSON, and extracts the `title` and `description`.

✅ **Store Data**  
Processed data is saved as CSV files in an S3 bucket for further analysis or reporting.

---

## 🛠️ Technologies Used

- **Apache Kafka** for messaging.
- **Apache Spark Streaming** for processing.
- **AWS EC2** to host Kafka and Spark.
- **Amazon S3** for storage.
- **Python** for the Kafka producer.

---

## 📸 Project Output Screenshots

Below are snapshots of key project stages:

---

### 🟢 EC2 Instance Creation
> Provisioning an EC2 instance to run Kafka and Spark.

![EC2 Creation](docs/ec2_creation.png)

---

### 🟢 SSH into EC2
> Connecting securely to your instance.

![SSH into EC2](docs/ssh_into_ec2.png)

---

### 🟢 Zookeeper Running
> Zookeeper service started successfully.

![Zookeeper Running](docs/zookeeper_running.png)

---

### 🟢 Kafka Broker Running
> Kafka broker active and listening.

![Kafka Running](docs/kafka_running.png)

---

### 🟢 Kafka Topic Creation
> Creating the `news-topic` for incoming data.

![Kafka Topic Creation](docs/topic_creation.png)

---

### 🟢 Kafka Producer Output
> Producer sending live news articles to Kafka.

![Kafka Producer Output](docs/kafka_producer_output.png)

---

### 🟢 S3 Output
> Processed CSV files saved in the S3 bucket.

![S3 Output](docs/s3_output.png)

---
## 📄 License

This project is licensed under the MIT License.



