'''
Get new workers and grant bonus.
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
import hashlib

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

qualified = {} # hashed: actual

with open('passedPilot2.csv') as f:
    reader = csv.DictReader(f) 
    for row in reader:
      print(row['index'])
      hashed = hashlib.md5(row['WorkerId'].encode()).hexdigest()
      print(row['WorkerId'], '==hashed==>', hashed)
      qualified[hashed] = row['WorkerId']


docs = db.collection(u'assignments').stream()

bonusWorkers = []
bonusdict = {}

for doc in docs:
  d = doc.to_dict()
  if 'sandbox' in d and 'unfinished' in d and 'version' in d:
    if not d['sandbox'] and not d['unfinished'] and d['version']=='pilot2':
      if d['workerId'] in qualified and not d['workerId'] in bonusdict:
        bonusdict[d['workerId']] = (qualified[d['workerId']],doc.id)
        
print('# bonus workers: ', len(bonusdict))

for hashed, (workerId, assignment) in bonusdict.items():
  bonusWorkers.append([workerId, hashed, assignment])


# writing to csv file 
with open('bonus-pilot2.csv', 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(['WorkerId','Hashed', 'Assignment'])
    # writing the data rows 
    csvwriter.writerows(bonusWorkers)