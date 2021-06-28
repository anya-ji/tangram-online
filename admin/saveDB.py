'''
Pull all database results.
Run in venv: source venv/bin/activate
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import listdir
from os.path import isfile, join
from datetime import datetime, timezone
import matplotlib.pyplot as plt
from collections import defaultdict
import csv 
import json

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


data = {
  'annotations':[],
  'assignments':[],
  'counts':[],
  'files':[],
  'users':[]
}

def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()

for collection in ['annotations','assignments','counts','files','users']:
  docs = db.collection(collection).stream()
  for doc in docs:
    d = doc.to_dict()
    data[collection].append(d)
  print('done!: ', collection)


with open('./db/0625-pilot3.json', 'w') as outfile:
  json.dump(data, outfile, default = myconverter)


