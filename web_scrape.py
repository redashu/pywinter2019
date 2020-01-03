#!/usr/bin/python3

import  requests,time
from  bs4  import BeautifulSoup
#  browsing this URL 
url="http://54.175.150.87/login.html"
#  now downloading source code
webdata=requests.get(url)
print(webdata)  #  this will give response code
#  if 200 then ok if 404 then check typo

# now to get original content of page 
#print(webdata.content)
time.sleep(2)
myhtmldata=webdata.text
# now we can apply  BS4
souped=BeautifulSoup(myhtmldata,'html5lib')
#print(souped.findAll('a'))
#print(souped.find('a'))
for  i  in  souped.findAll('a'):
	print(i)
	time.sleep(1)


