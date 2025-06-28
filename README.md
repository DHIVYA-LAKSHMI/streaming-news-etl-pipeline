# Real-Time News ETL Pipeline

This project implements a real-time ETL pipeline using Apache Kafka and Apache Spark Streaming on AWS.

## 📸 Project Output Screenshots

#### 🟢 EC2 Instance Creation
> Provisioning an EC2 instance to run Kafka and Spark.

![EC2 Creation](docs/ec2_creation.png)

#### 🟢 SSH into EC2
> Connecting securely to your instance.

![SSH into EC2](docs/ssh_into_ec2.png)

#### 🟢 Zookeeper Running
> Zookeeper service started successfully.

![Zookeeper Running](docs/zookeeper_running.png)

#### 🟢 Kafka Broker Running
> Kafka broker active and listening.

![Kafka Running](docs/kafka_running.png)

#### 🟢 Kafka Topic Creation
> Creating the `news-topic` for incoming data.

![Kafka Topic Creation](docs/topic_creation.png)

#### 🟢 Kafka Producer Output
> Producer sending live news articles to Kafka.

![Kafka Producer Output](docs/kafka_producer_output.png)

#### 🟢 S3 Output
> Processed CSV files saved in S3 bucket.

![S3 Output](docs/s3_output.png)
