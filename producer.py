from datetime import datetime
import boto3
import calendar
import json
import random
import time

my_stream_name = 'smith8ca-kds-001'
kinesis_client = boto3.client('kinesis', region_name='us-east-1')


def put_to_stream(record_id, record_value, record_timestamp):
    payload = {
        'id': record_id,
        'value': str(record_value),
        'timestamp': str(record_timestamp)
    }

    print(json.dumps(payload, indent=4))

    put_response = kinesis_client.put_record(
        StreamName=my_stream_name,
        Data=json.dumps(payload),
        PartitionKey=record_id)


while True:
    record_value = random.randint(40, 120)
    record_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    record_id = 'aa-bb'

    put_to_stream(record_id, record_value, record_timestamp)

    # Wait for 30 second
    time.sleep(30)
