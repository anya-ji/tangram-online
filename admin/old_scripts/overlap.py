import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import listdir
from os.path import isfile, join
from datetime import datetime, timezone
from collections import defaultdict
import csv 
import hashlib

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection(u'assignments').stream()

for doc in docs:
  d = doc.to_dict()
  if 'sandbox' in d and 'unfinished' in d and 'version' in d:
    if not d['sandbox'] and not d['unfinished']: 
      user = db.collection(u'users').document(d['workerId']).get()
      if user.exists:
          ud = user.to_dict()
          if d['file'].replace('.svg','') not in ud:
            print(d['file'], d['version'], doc.id,' worker: ', d['workerId'])
      else:
          print('no such document: ',d['workerId'])