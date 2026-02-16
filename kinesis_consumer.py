"""
kinesis_consumer.py

Simulates a real-time streaming pipeline for fraud detection.
"""

import logging
from pyspark.sql import SparkSession

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


def get_spark():
    return (
        SparkSession.builder
        .appName("fraud-feature-streaming")
        .getOrCreate()
    )


def run():
    spark = get_spark()
    log.info("Streaming job initialized successfully.")
    spark.stop()


if __name__ == "__main__":
    run()
