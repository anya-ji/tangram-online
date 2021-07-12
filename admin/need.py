import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json
from datetime import datetime

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()



# dic = {'page1-108': 9, 'page1-64': 9, 'page1-70': 9, 'page2-113': 9, 'page2-126': 9, 'page2-134': 9, 'page2-143': 9, 'page2-148': 9, 'page2-163': 9, 'page2-166': 9, 'page2-17': 9, 'page2-173': 9, 'page2-182': 9, 'page2-184': 9, 'page2-187': 9, 'page2-189': 9, 'page2-191': 9, 'page2-22': 9, 'page2-48': 9, 'page2-49': 9, 'page2-54': 9, 'page2-70': 9, 'page2-72': 9, 'page2-76': 9, 'page3-122': 9, 'page3-133': 9, 'page3-17': 9, 'page3-180': 9, 'page3-185': 9, 'page3-21': 9, 'page3-30': 9, 'page3-32': 9, 'page3-39': 9, 'page3-4': 9, 'page3-42': 9, 'page3-45': 9, 'page3-47': 9, 'page3-54': 9, 'page3-55': 9, 'page3-66': 9, 'page3-74': 9, 'page3-92': 9, 'page4-108': 9, 'page4-128': 9, 'page4-15': 9, 'page4-176': 9, 'page4-192': 9, 'page4-2': 9, 'page5-60': 9, 'page5-87': 9, 'page7-149': 9, 'page7-230': 9}

# for file, count in dic.items():
#     f = file+'.svg'
#     db.collection('files').document(f).update({'count': count})
#     db.collection('counts').document('counts').update({db.field_path(file):count})

i=1
docs = db.collection('files').where('count','<',10).stream()
for doc in docs:
    print(i)
    print(f"{doc.id} => {doc.to_dict()['count']}")
    i+=1