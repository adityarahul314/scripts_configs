import requests
import imghdr
import os
import os.path
import sys
from progress.bar import IncrementalBar

url = input("Enter url : ")
urlkey = list(url)
del urlkey[len(urlkey)-5:len(urlkey)]

#Current directory and New Directory
rootdir = os.getcwd()
urlkey2 = ''.join(urlkey)
if urlkey2.find('/'):
	newdirname = urlkey2.rsplit('/',1)[1]
print(urlkey2)
dldir = rootdir + '/anya/' + newdirname + '/'

dl_startC = input('Enter first char : ')
dl_endC = input('Enter last char : ')
dl_startN = ord(dl_startC)
dl_endN = ord(dl_endC)
dlsize = int(dl_endN) - int(dl_startN) + 11
bar = IncrementalBar('Processing', max=dlsize)
print(dlsize)

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

for x in range(0,9):
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
for x in range(int(dl_startN),int(dl_endN)+1):
	#print(x)
	urltemp = ''.join(urlkey) + chr(x) + ".jpg"
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