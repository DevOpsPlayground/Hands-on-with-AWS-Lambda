import boto3
import time
import json
import random

STREAM_NAME = 'cloudStream'

cloudProviders = [
'AWS',
'MicrosoftClould',
'GoogleCloud',
'ibmBlueMix',
'Salesforce',
'Rackspace',
'RedHat',
'digitalOcean',
'dockerDataCenter'
]

for index in range(1, 101):
    time.sleep(0.5)
    n = random.randint(100, 500)
    vendor = random.choice(cloudProviders)
    print("Generating %s records for votes, %s " % (n, vendor))
    for i in range(n):
        print ("%s : %s" % (vendor.lower(), i))
'''
    client.put_records(
        StreamName=STREAM_NAME,
        Records=[
            {
                'Data': b'name-%s' % index,
                'PartitionKey': 'my-partition-key-0001',
            } for i in range(n)
        ]
    )
'''
