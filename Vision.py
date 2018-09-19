
import io
import os

from google.cloud import vision
from google.cloud.vision import types

pic_path = 'C:\\Users\\64483\\Documents\\EC601\\result\\EC601\\'

client = vision.ImageAnnotatorClient()

lists = os.listdir(pic_path)
lists.sort()

doc = open ('out.txt','w')
for pic in lists:


    with io.open(pic_path + pic, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

# Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations


    print('Labels for ' + pic +':', file = doc)
    for label in labels:
    #save the result into a txt file
        print(label.description, end = ' ', file=doc)
    print('',file = doc)
doc.close()