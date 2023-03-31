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

if os.path.exists(dldir):
	filesindir = os.listdir(dldir)
	print("Directory " + newdirname + " already exists!" + "It has " + str(len(filesindir)) + " files")
	userc = input("Do you want to continue? Y or N \n")
	if userc.lower() in ['y','yes']:
		print("Y")
	elif userc.lower() in ['n','no']:
		print("N")
	else:
		print("Fuck You!")
	#sys.exit()
else:
	os.makedirs(dldir)

dlsize = input("Enter list size : ")
bar = IncrementalBar('Processing', max=(int(dlsize)+1-int(sp)))

for x in range(int(sp),int(dlsize)+1):
	#print(x)
	urltemp = ''.join(urlkey) + str(x) + ".jpeg"
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