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

version = 'batch1'

rs={}
i=0
for doc in docs:
  d=doc.to_dict()
  if 'version' in d:
    if d['version']==version and not d['unfinished']:
      i+=1
    if 'feedback' in d and d['feedback'] != '' and d['version']==version:
      c = d['feedback']
      n = doc.id
      rs[n] = c
     
      print(d['file'], '(worker:',d['workerId'],'): ', c,'\n')

print(version,'-completed: ', i)
# print(rs)


