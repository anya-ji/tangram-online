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

# ppl have the qual
qualified = {} # hashed: actual

with open('./csv/passedPilot3.csv') as f:
    reader = csv.DictReader(f) 
    for row in reader:
      print(row['index'])
      print(row['WorkerId'], '==hashed==>', row['Hashed'])
      qualified[row['Hashed']] = row['WorkerId']


docs = db.collection(u'assignments').stream()

bonusdict = {} # hashed: (workerId, assignment, version)
version = 'pilot3'# change version

for doc in docs:
  d = doc.to_dict()
  if 'sandbox' in d and 'unfinished' in d and 'version' in d:
    if not d['sandbox'] and not d['unfinished'] and d['version']==version: 
      if d['workerId'] in qualified and not d['workerId'] in bonusdict:
        bonusdict[d['workerId']] = (qualified[d['workerId']],doc.id,version)
        
#delete already received
with open('./csv/receivedBonus.csv') as f:
    reader = csv.DictReader(f) 
    for row in reader:
      if(row['Hashed'] in bonusdict):
        print(row['WorkerId'],' hashed: ',row['Hashed'],' received bonus for ', row['Version'])
        del bonusdict[row['Hashed']]

print('# bonus workers: ', len(bonusdict))

#rows of new bonus workers
bonusWorkers = []
for hashed, (workerId, assignment, taskVersion) in bonusdict.items():
  bonusWorkers.append([workerId, hashed, assignment, taskVersion])


# writing to new csv file 
with open('./csv/bonus-pilot3.csv', 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(['WorkerId','Hashed', 'Assignment', 'Version'])
    # writing the data rows 
    csvwriter.writerows(bonusWorkers)

# add to received bonus file
with open('./csv/receivedBonus.csv', 'a', newline='') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    # writing the data rows 
    csvwriter.writerows(bonusWorkers)