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

docs = db.collection(u'users').stream()

def convertLang(l):
  rs = []
  for details in l.values():
    rs.append(details['language']+'('+details['proficiency']+')')
  rss = ', '.join(rs)
  return rss


rs = {} # workerid: {engfirst, wherelearn, languages}
for doc in docs:
  d = doc.to_dict()
  if 'languages' in d:
    rs[doc.id] = {
      'engFirst': d['engFirst'],
      'whereLearn': d['whereLearn'],
      'languages': convertLang(d['languages'])
    }

rows = []
for wid, d in rs.items():
  rows.append([wid, d['engFirst'], d['whereLearn'], d['languages']])

# writing to new csv file 
with open('./csv/languages-batch1.csv', 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
    csvwriter.writerow(['WorkerId','engFirst', 'whereLearn', 'languages'])
    # writing the data rows 
    csvwriter.writerows(rows)