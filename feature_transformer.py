"""
feature_transformer.py

Computes fraud detection features.
"""

from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window

HIGH_RISK_MCC = {"6011", "7995", "4829", "6051", "5912"}


def compute_features(df: DataFrame) -> DataFrame:

    window_spec = (
        Window.partitionBy("account_id")
        .orderBy(F.col("event_time").cast("long"))
        .rangeBetween(-3600, 0)
    )

    df = df.withColumn(
        "txn_count_1h",
        F.count("transaction_id").over(window_spec)
    )

    df = df.withColumn(
        "amount_sum_1h",
        F.sum("amount").over(window_spec)
    )

    df = df.withColumn(
        "is_high_risk_mcc",
        F.col("merchant_category_code").isin(list(HIGH_RISK_MCC)).cast("int")
    )

    return df
