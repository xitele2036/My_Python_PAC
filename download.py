#!/usr/bin/python
#encoding:utf-8
import http
import shutil
import urllib.request
import os
import datetime


hourtime = datetime.datetime.now().strftime("%M%S")
print(hourtime)
target = "D:\Pworktest\JBUS\\"+hourtime
os.makedirs(target)


for a in range(1,100):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
	chaper_url = "https://img2.wnacg.download/data/0842/57/%s.jpg" %(str(a).zfill(3))
	print (chaper_url)
	f = urllib.request.Request(url=chaper_url, headers=headers)
	# f = urllib.request.urlopen(url)
	try:
		data = urllib.request.urlopen(f).read()
	except(http.client.IncompleteRead) as e:
		data = e.partial
	with open("%s.jpg" %(str(a).zfill(3)),"wb") as code:
			code.write(data)
	shutil.move("%s.jpg"%(str(a).zfill(3)),target)






