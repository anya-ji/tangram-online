'''
Pull database results.
Run in venv: source venv/bin/activate
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import listdir
from os.path import isfile, join
from datetime import datetime, timezone
from collections import defaultdict

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

docs = db.collection(u'assignments').stream()

i=0
for doc in docs:
  d = doc.to_dict()
  if not d['unfinished']:
    i+=1
  else:
    lasted = (datetime.now(timezone.utc) - d["lastClaimed"]).seconds/60
    if lasted >= 12:
      print("expired")
    else:
      print("in progress: ", lasted, " minutes")
    
print("Total finished assignments: ", i)