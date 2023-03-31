import requests
import imghdr
import os
import os.path
import sys
from progress.bar import IncrementalBar

url = input("Enter url : ")
urlkey = list(url)
del urlkey[len(urlkey)-5:len(urlkey)]

sp = input("Enter Deviant : ")

def ragadl(x):
	print(x)

#ragadl("worked?")

#Current directory and New Directory
rootdir = os.getcwd()
urlkey2 = ''.join(urlkey)
if urlkey2.find('/'):
	newdirname = urlkey2.rsplit('/',1)[1]

dldir = rootdir + '/ragadl/' + newdirname + '/'

dlsize = input("Enter list size : ")
bar = IncrementalBar('Processing', max=int(dlsize))

for x in range(int(sp),int(sp)+int(dlsize)+1):
	#print(x)
	urltemp = ''.join(urlkey) + str(x) + ".jpg"
	#print(urltemp)
	res = requests.get(urltemp)
	if urltemp.find('/'):
		name = dldir + urltemp.rsplit('/', 1)[1]
		#print(name)
	open(name, 'wb').write(res.content)
	datatype = imghdr.what(name)
	#print(datatype)
	if datatype == None:
		os.remove(name)
	bar.next()
	x = x+1
bar.finish()