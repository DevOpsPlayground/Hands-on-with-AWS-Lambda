import boto3
import time
import json
import random

client = boto3.client('kinesis', 'us-west-1')
STREAM_NAME = 'events'
PARTITION_KEY = 'my-partition-key-0001'

for index in range(1, 101):
    time.sleep(0.5)
    n = random.randint(100, 500)
    print("Generating %s records for 'event%s'" % (n, index))
    for i in range(n):
        print (b'name-%s = n' % index, n)
