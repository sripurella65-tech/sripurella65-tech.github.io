# Dev Notes

Lessons Learned:

- Kinesis shard capacity planning is critical.
- DynamoDB batch_write_item does not throw errors for partial failures.
- Delta Lake MERGE prevents duplicate records on restart.
- Watermarking is essential for late-arriving mobile transactions.

Future Improvements:

- Add data quality validation
- Add feature drift monitoring
- Build historical backfill pipeline
