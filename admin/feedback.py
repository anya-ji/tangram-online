'''
Get feedback.
Run in venv: source venv/bin/activate
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import listdir
from os.path import isfile, join
from datetime import datetime, timezone
from collections import defaultdict
import csv 

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection(u'assignments').stream()

rs={}
for doc in docs:
  if 'feedback' in doc.to_dict() and doc.to_dict()['feedback'] != '':
    c = doc.to_dict()['feedback']
    n = doc.id
    rs[n] = c

print(rs)


