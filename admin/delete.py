import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
from datetime import datetime
from collections import defaultdict

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()
# deleted=defaultdict(int)

# docs = db.collection('annotations').stream()
# for doc in docs:
#   d=doc.to_dict()
#   file=doc.id
#   for user, detail in d.items():
#     if user in ['d4d4e36f68cc4de5a7217310e7011065']:
#       ref = db.collection(u'annotations').document(file)
#       ref.update({
#           user: firestore.DELETE_FIELD
#       })
#       # print(file)
#       deleted[file]+=1

# print(deleted)
# print(sum(deleted.values()))

#change count in ann and counts
# update = {'page-A': 5, 'page-B': 5, 'page-C': 5, 'page-D': 5, 'page-E': 5, 'page-F': 5, 'page-G': 5, 'page-H': 5, 'page-I': 5, 'page-J': 5, 'page-K': 5, 'page-L': 5, 'page1-0': 3, 'page1-105': 4, 'page1-116': 4, 'page1-119': 3, 'page1-128': 4, 'page1-129': 3, 'page1-69': 4, 'page2-112': 3, 'page2-131': 3, 'page2-137': 3, 'page2-34': 4, 'page3-121': 4, 'page3-128': 3, 'page3-136': 4, 'page3-182': 3, 'page3-35': 3, 'page3-41': 3, 'page3-72': 3, 'page3-85': 3, 'page4-10': 3, 'page4-128': 4, 'page4-157': 3, 'page4-162': 3, 'page4-24': 3, 'page4-93': 3, 'page5-128': 4, 'page5-136': 4, 'page5-153': 3, 'page5-178': 4, 'page5-186': 4, 'page5-200': 3, 'page5-232': 3, 'page5-244': 3, 'page5-28': 3, 'page5-59': 3, 'page5-64': 4, 'page5-75': 4, 'page6-143': 3, 'page6-149': 4, 'page6-162': 3, 'page6-164': 3, 'page6-180': 3, 'page6-203': 3, 'page6-78': 3, 'page6-99': 3, 'page7-105': 3, 'page7-107': 3, 'page7-14': 3, 'page7-180': 3, 'page7-197': 3, 'page7-218': 4, 'page7-248': 3, 'page7-26': 4, 'page7-81': 3, 'page8-159': 3, 'page8-183': 3, 'page8-21': 4, 'page8-234': 3, 'page8-235': 3, 'page9-13': 3, 'page9-27': 4, 'page9-46': 4}
# update={'page-C': 1, 'page-E': 1, 'page-I': 1, 'page-L': 3, 'page3-182': 1, 'page3-41': 4, 'page5-186': 1, 'page5-59': 3, 'page5-64': 2, 'page5-75': 2, 'page6-143': 1, 'page6-164': 1, 'page6-78': 4, 'page7-107': 4, 'page7-180': 1, 'page7-26': 2, 'page8-159': 1, 'page8-234': 1}

update={'page-A': 1, 'page5-107': 1, 'page6-78': 1}

for f,v in update.items():
  name=f+'.svg'
  db.collection('files').document(name).update({
    'count':firestore.Increment(-v)
  })
  db.collection('counts').document('counts').update({
    db.field_path(f):firestore.Increment(-v)
  })
  print(f, v)


print(len(update))
print(sum(update.values()))