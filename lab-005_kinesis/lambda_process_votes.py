from __future__ import print_function

import base64
import json
import boto3

print('Loading function')

DDB = boto3.resource('dynamodb').Table('votes_cloud_platform')

def lambda_handler(event, context):
    # print("Received event: " + json.dumps(event, indent=2))

    for record in event['Records']:
        # kinesis data is base64 encoded so decode here
        payload = base64.b64decode(record['kinesis']['data'])
        if not payload in totals:
            totals[payload] = 0
        totals[payload] += 1

    for name, total in totals.iteritems():
        DDB.update_item(
            key={'Name': name},
            UpdateExpression='ADD EventCount :val',
            ExpressionAttributeValues={':val': total},
        )

        print("Decoded payload: " + payload)
    return 'Successfully processed {} records.'.format(len(event['Records']))
