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
import matplotlib.pyplot as plt
from collections import defaultdict
import csv 

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# field names 
fields = ['index','tangram', 'whole', '1', '2', '3', '4', '5', '6', '7', 'workerId', 'assignmentId', 'hitId', 'submittedAt'] 
    
# data rows of csv file 
rows = [] 
    
# name of csv file 
filename = "./results.csv"

# data
docs = db.collection(u'annotations').stream()

index = 0

for doc in docs:
    file = doc.to_dict()
    for workerId, d in file.items():
        index += 1
        rows.append([index, doc.id, d["whole-annotation"]["wholeAnnotation"], d["piece-annotation"]["1"],
        d["piece-annotation"]["2"], d["piece-annotation"]["3"], d["piece-annotation"]["4"], d["piece-annotation"]["5"],
        d["piece-annotation"]["6"], d["piece-annotation"]["7"], workerId, d["assignmentId"], d["hitId"], d["submittedAt"]])

    
# writing to csv file 
with open(filename, 'w') as csvfile: 
    # creating a csv writer object 
    csvwriter = csv.writer(csvfile) 
        
    # writing the fields 
    csvwriter.writerow(fields) 
        
    # writing the data rows 
    csvwriter.writerows(rows)
