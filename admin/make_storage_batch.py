import json
from os import listdir
from os.path import isfile, join

'''
make batches to upload images
'''

images_path = '../../tangram-dashboard/public/dev_images' ### change

image_files = [join(images_path, f) for f in listdir(images_path) if isfile(join(images_path, f)) and f.endswith('.png')]
total = len(image_files)
print(total)

rs={}

count = 0
batch = 0
imgs = []
for i, img in enumerate(image_files):
  count +=1
  imgs.append(img)

  if count==4000:
    print(len(imgs))
    rs[batch] = imgs
    batch+=1
    imgs = []
    count = 0

#last batch
rs[batch] = imgs
print(len(imgs))

print(rs.keys())


with open('./storage_batches.json', 'w') as f:
  json.dump(rs, f)


 