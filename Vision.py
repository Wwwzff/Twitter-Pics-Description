
import io
import os
import cv2




from google.cloud import vision
from google.cloud.vision import types


client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = os.path.join(
    os.path.dirname(__file__),
    '1.jpg')

# Loads the image into memory
with io.open(file_name, 'rb') as image_file:
    content = image_file.read()

image = types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

doc = open ('out.txt','w')

print('Labels:')
for label in labels:
    print(label.description)
    #save the result into a txt file
    print(label.description, file=doc)

doc.close()