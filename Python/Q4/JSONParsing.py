import json
from pprint import pprint

data = json.load(open('data.json'))
pprint("eTag is "+ data['Records'][0]['s3']['object']['eTag'])
pprint("Bucket name is " + data['Records'][0]['s3']['bucket']['name'])
