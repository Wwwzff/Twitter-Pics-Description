import tweepy
import urllib.request
import glob as gb
import cv2
import io
import os

from google.cloud import vision
from google.cloud.vision import types
import pymysql

# Part 1 Twitter API
# Twitter API credentials
def credentials(consumer_key,consumer_secret,access_token,access_token_secret):
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)
        print('Successfully linked with tweepy')
        return api
    except:
        exit(1)

# Download pictures
def downloadPics(auth,name,number,path):
    tweets = auth.user_timeline(id=name, count = number)
    imgName=0
    for tweet in tweets:
        media = tweet.entities.get('media', [])
        if(len(media) > 0):
            imgName+=1
            imgPath = media[0]['media_url']
            # download the pics to a specified path
            f = open( path + str(imgName)+".jpg", 'wb')
            f.write((urllib.request.urlopen(imgPath)).read())
    f.close()
    print('Pictures Downloaded')
    return imgName

# Part 2 convert Pics to Video
def pic2video(path,filename,fps,resolution):
    # Part 2 Pics to Video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # input path of the pics
    img_path=gb.glob( path + "*.jpg")

    # output video will be in the same path as the python file 
    # define the output name, resolution, fps and etc. of the video
    videoWriter=cv2.VideoWriter(filename,fourcc,fps,resolution)
    for path in img_path:
        img=cv2.imread(path)
        img=cv2.resize(img,(1024,512))
        videoWriter.write(img)
    print('Convertion Completed')

# Part 3 using Cloud API to label pictures
def labeller(sourcepath):
    try:
        client = vision.ImageAnnotatorClient()
        print('Cloud API Linked')
    except:
        exit(1)
    pic_path = sourcepath
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
    print('Finished')

# for Miniproject3
# write infos in a mysql database
def writeDBmySQL(twitterID,imgNumber,descriptor):
    db = pymysql.connect("localhost","root","123456","MiniProject3",3306)   #localhost,DBusername,password,DBname,Port
    cursor = db.cursor()
    sql = """insert into userinfo values (null,default,"""+'"'+twitterID+'"'+","+str(imgNumber)+',"'+descriptor+'");'   # e.g. insert into userinfo values (null,default,"linkinpark",'50',"guitar");
    cursor.execute(sql)
    db.commit()
    db.close()

def find_most_frequent_word(filename):
#find the most frequent word in the descriptor
	resultdict={}
	with open(filename)as fp:
		for i in fp:
			wordlist=i.split()
			for j in wordlist:
				if j!='Labels' and j!='for':
					if j not in resultdict:
						resultdict[j]=1
					else:
						resultdict[j]+=1
	sort_resultdict=sorted(resultdict.items(),key=lambda x:x[1],reverse=True)
	return sort_resultdict[0][0]

####################################################################################################

path = "D:\\EC601\\"
twitterID = 'linkinpark'
consumer_key = "EaRJCL2n7WW7oGqZPGW8LjT2g"
consumer_secret = "LpSj2RWRpW2MNTETotE6LIHizGyzdQNNS3vXOUEHDnwO0y07ws"
access_token = "1038532509942857730-Sn24COVvc7Zt7rY6WM0GugU4JuUXr9"
access_token_secret = "mpRtlWQtrw0YRdIkMUqHPoldxbDgpXSgxB4Vx6D3ybNOb"


api = credentials(consumer_key,consumer_secret,access_token,access_token_secret)
imgNumber = downloadPics(api,twitterID,100,path)
pic2video(path,"result.mp4",6,(1024,512))
labeller(path)
descriptor = find_most_frequent_word('./out.txt')
writeDBmySQL(twitterID,imgNumber+1,descriptor)

