
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import listdir
from os.path import isfile, join
import datetime


cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# f = open("25+25+12.txt", "r")
# samples=[]
# i=0
# for x in f:
#   samples.append(x.replace('\n','.svg'))
#   i+=1
# print(i)


mypath = '../public/assets/'
files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
i=0

original = ['page-A.svg','page-B.svg','page-C.svg','page-D.svg','page-E.svg','page-F.svg','page-G.svg','page-H.svg','page-I.svg','page-J.svg','page-K.svg','page-L.svg']

# for f in files:
#   if f.startswith('page') and f not in samples:
#     doc = db.collection(u'files').document(f).get()
#     print(doc.to_dict())
#     break

# i=1
# for f in original:
#   db.collection(u'files').document(f).set({
#         'name': f.strip('.svg'),
#         'count': 0,
#         'available': True,
#         'lastClaimed': datetime.datetime.now() - datetime.timedelta(hours=1),
#         'completedWorkers': [],
#         'claimedWorkers': []
#       })
#   db.collection(u'counts').document(u'counts').set({
#     f.strip('.svg'): 0
#   },
#   merge = True)
#   print(i,":",f)
#   i+=1



k=0
i=0
for f in files:
  if f.startswith('page'):
    db.collection(u'files').document(f).update({
      'original': f in original
    })
    print(i,":",f, ' ',f in original)
    if f in original:
      k+=1
    i+=1
print(i,k)

#check
# k=0
# for s in samples:
#     doc = db.collection(u'files').document(s).get()
#     if doc.to_dict()['count'] <50:
#       print(doc.to_dict()['name'],'\n', doc.to_dict()['count'])


