


import tweepy
import urllib.request
import glob as gb
import cv2
import io
import os

from google.cloud import vision
from google.cloud.vision import types

# Part 1 Twitter API
# Twitter API credentials
consumer_key = "consumer key"
consumer_secret = "consumer secret"
access_token = "access token"
access_token_secret = "access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# specify the username and how many tweets will be involved
tweets = api.user_timeline(id='(TwitterID)', count = 100)

imgName=0

for tweet in tweets:
    media = tweet.entities.get('media', [])
    
    if(len(media) > 0):
        imgName+=1
        imgPath = media[0]['media_url']
        # download the pics to a specified path
        f = open('(your output path)'+ str(imgName)+".jpg", 'wb')
        f.write((urllib.request.urlopen(imgPath)).read())
f.close()


# Part 2 Pics to Video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

# input path of the pics
img_path=gb.glob("D:\\EC601\\*.jpg")

# output video will be in the same path as the python file 
# define the output name, resolution, fps and etc. of the video
videoWriter=cv2.VideoWriter('result.mp4',fourcc,6,(1024,512))

for path in img_path:
    img=cv2.imread(path)
    img=cv2.resize(img,(1024,512))
    videoWriter.write(img)


# Pics Annotation
client = vision.ImageAnnotatorClient()

# The path for the image file to annotate
pic_path = 'C:\\Users\\64483\\Documents\\EC601\\result\\EC601\\'

lists = os.listdir(pic_path)
lists.sort()

# Save labels to a .txt file
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
        print(label.description, end = ' ', file=doc)
    print('',file = doc)
doc.close()