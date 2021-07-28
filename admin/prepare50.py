
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import listdir
from os.path import isfile, join
import datetime


cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

f = open("25+25+12.txt", "r")
samples=[]
i=0
for x in f:
  samples.append(x.replace('\n','.svg'))
  i+=1
print(i)
# print(','.join(samples))


# mypath = '../public/assets/'
# files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# i=0

# for f in files:
#   if f.startswith('page') and f not in samples:
#     doc = db.collection(u'files').document(f).get()
#     print(doc.to_dict())
#     break
# k=0
# for f in files:
#   if f.startswith('page'):
#     db.collection(u'files').document(f).update({
#       'sampled': f in samples
#     })
#     print(i,":",f, ' ',f in samples)
#     if f in samples:
#       k+=1
#     i+=1
# print(i,k)


#check
k=0
for s in samples:
    doc = db.collection(u'files').document(s).get()
    if doc.to_dict()['count'] <50:
      print(doc.to_dict()['name'],'\n', doc.to_dict()['count'])


