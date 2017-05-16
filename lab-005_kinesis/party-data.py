import boto3
import time
import json
import random

parties = [
'Conservatives',
'Labour',
'SNP',
'LibDems',
'Greens'
]

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
    party = random.choice(parties)
    print("Generating %s records for %s party" % (index, party))
    for i in range(n):
        print ("%s : %s" % (party.lower(), n))
