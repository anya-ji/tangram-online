import firebase_admin
import json
from collections import defaultdict
from os import listdir
from os.path import isfile, join
from firebase_admin import credentials, initialize_app, storage
'''
Add images to storage
'''

cred = credentials.Certificate("./tangram-online-firebase-adminsdk-pkuk1-c623f892a3.json")
initialize_app(cred, {'storageBucket':'tangram-online.appspot.com'}) # no gs://!!

bucket = storage.bucket()

# urls = {}

images_path = '../../tangram-dashboard/public/dev_images' ### change

with open('./storage_batches.json') as f:
  image_files = json.load(f)['5'] ### change batch

total = len(image_files)
print(total)

for i, img in enumerate(image_files):
  if i<1053:
    continue
  filename = img.split('/')[-1] 
  storage_path = 'dev_images/'+filename ### change: path in storage

  blob = bucket.blob(storage_path) # storage_path
  blob.upload_from_filename(img) # local path

  blob.make_public()
  print(i+1, '/', total, filename)
  # urls[filename]=blob.public_url

  # break

# print(urls)
