# Consumer will start consuming the data as the producer puts it to the stream
from datetime import datetime
import boto3
import json
import time

my_stream_name = 'smith8ca-kds-001'
kinesis_client = boto3.client('kinesis', region_name='us-east-1')

# Get the description of kinesis shard; It is the JSON from which we will get the shard ID
response = kinesis_client.describe_stream(StreamName=my_stream_name)
my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']

shard_iterator = kinesis_client.get_shard_iterator(
    StreamName=my_stream_name, ShardId=my_shard_id, ShardIteratorType='LATEST')
my_shard_iterator = shard_iterator['ShardIterator']

record_response = kinesis_client.get_records(
    ShardIterator=my_shard_iterator, Limit=2)

while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(
        ShardIterator=record_response['NextShardIterator'], Limit=2)

    # If data exists in the "records" field, print the data
    if (record_response['Records']):
        print(record_response['Records'])

    # Wait for 10 seconds
    time.sleep(10)
