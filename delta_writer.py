"""
delta_writer.py

Handles writing features to DynamoDB and Delta Lake.
"""

from pyspark.sql import DataFrame


def write_to_stores(df: DataFrame, batch_id: int):
    print(f"Writing batch {batch_id}")
