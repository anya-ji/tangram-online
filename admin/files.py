'''
Initialize the database with files.
Run in venv: source venv/bin/activate
'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from os import listdir
from os.path import isfile, join
import datetime

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

mypath = '../public/assets/'

# files = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# print(files)

# 27 for pilot
files = ['page1-5.svg','page1-13.svg','page1-29.svg','page1-34.svg','page2-138.svg',
'page2-155.svg','page2-185.svg','page3-101.svg','page3-123.svg','page3-163.svg',
'page3-191.svg','page4-56.svg','page4-64.svg','page4-73.svg','page4-228.svg','page5-0.svg',
'page5-11.svg','page5-64.svg','page6-83.svg','page6-109.svg','page7-29.svg','page7-87.svg',
'page8-165.svg','page8-218.svg','page9-4.svg','page9-31.svg','page9-45.svg']

# initial_files = {}
i=0

for f in files:
  # initial_files[f.strip('.svg')] = 0
  if f != 'check.py':
    db.collection(u'files').document(f).set({
      'name': f.strip('.svg'),
      'count': 0,
      'available': True,
      'lastClaimed': datetime.datetime.now(),
      'completedWorkers': []
    })
    print(i,":",f)
    i+=1