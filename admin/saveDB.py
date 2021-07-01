'''
Pull all database results.
Run in venv: source venv/bin/activate
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


data = {
  'annotations':{},
  'assignments':{},
  'counts':{},
  'files':{},
  'users':{}
}

def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()

for collection in ['annotations','assignments','counts','files','users']:
  docs = db.collection(collection).stream()
  for doc in docs:
    d = doc.to_dict()
    data[collection][doc.id] = d
  print('done!: ', collection)


with open('./batch1.json', 'w') as outfile:
  json.dump(data, outfile, default = myconverter)


