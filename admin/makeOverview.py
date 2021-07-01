'''
Pull all database results.
Run in venv: source venv/bin/activate
'''

from os import listdir
from os.path import isfile, join
from datetime import datetime, timezone
from collections import defaultdict
import csv 
import json


def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()

f = open('data/batch1.json')
d = json.load(f)

data = []

for page, allAnns in d["annotations"].items():
  for workerId, details in allAnns.items():
    details["tangramId"] = page+'.svg';
    details["workerId"] = workerId;
    data.append(details)


with open('./data/overview-batch1.json', 'w') as outfile:
  json.dump(data, outfile, default = myconverter)


