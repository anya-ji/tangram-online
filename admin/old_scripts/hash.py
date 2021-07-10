import csv 
import hashlib

# with open('failedPilot2.csv') as f:
#     reader = csv.DictReader(f) 
#     for row in reader:
#       print(row['index'])
#       hashed = hashlib.md5(row['WorkerId'].encode()).hexdigest()
#       print(row['WorkerId'], '==hashed==>', hashed)

hashed = hashlib.md5('A2ACP1XRAMISKL'.encode()).hexdigest()
print(hashed)