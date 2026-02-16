# Fraud Detection Feature Store

Real-time streaming feature engineering pipeline for fraud detection.

This project simulates how modern financial systems compute fraud features
in near real-time instead of relying on 24-hour stale batch features.

Architecture:

Transaction API
    ↓
AWS Kinesis
    ↓
Spark Structured Streaming
    ↓
DynamoDB (Online Store)
Delta Lake (Offline Store)

Tech Stack:
Python · PySpark · AWS Kinesis · DynamoDB · Delta Lake · MLflow

How to Run:

pip install -r requirements.txt
python src/kinesis_consumer.py

Author: Sri Chandana Purella
