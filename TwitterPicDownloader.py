


import tweepy
import urllib.request


#Twitter API credentials
consumer_key = "consumer key"
consumer_secret = "consumer secret"
access_token = "access token"
access_token_secret = "access token secret"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#specify the username and how many tweets will be involved
tweets = api.user_timeline(id='IKEAUSA', count = 100)

imgName=0

for tweet in tweets:
    media = tweet.entities.get('media', [])
    
    if(len(media) > 0):
        imgName+=1
        imgPath = media[0]['media_url']
        #download the pics to a specified path
        f = open('D:\\EC601\\'+ str(imgName)+".jpg", 'wb')
        f.write((urllib.request.urlopen(imgPath)).read())
f.close()