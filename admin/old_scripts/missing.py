'''
Test.
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

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

mypath = '/Users/anyaji/Desktop/tangram-mturk-pilot/production-results'
files = [f.replace('.json','').split("-",1)[1]  for f in listdir(mypath) if isfile(join(mypath, f))]

a = []

docs = db.collection(u'annotations').stream()

for doc in docs:
    file = doc.to_dict()
    for workerId, d in file.items():
        a.append(d["assignmentId"])

for f in files:
  if f not in a:
    print(f)
