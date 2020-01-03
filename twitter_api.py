#!/usr/bin/python3

import  tweepy,time

consumer_key=""
consumer_sec=""

access_token="1110138809461755911-SZ3YzhSHEJNSDrxwnYehz2fEUs7WH2"
access_sec=""

#  now connecting with api gateway 
auth=tweepy.OAuthHandler(consumer_key,consumer_sec)
#  now we are going to auth state in next step as access token , sec

auth.set_access_token(access_token,access_sec)
#  now connecting with API
api_connect=tweepy.API(auth)
# now we can search 
tweets=api_connect.search('modi',count=10)
#print(tweets)
for  i  in  tweets:
	print(i.text)
	print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
	print("@@@                         @@")
	print("@@@                         @@")
	print("@@@                         @@")
	print("@@@                         @@")
	time.sleep(1)


