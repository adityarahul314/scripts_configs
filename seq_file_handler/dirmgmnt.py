import hashlib
import os
import platform
import sys
import random
import string

#randomstr = ''.join(random.choices(string.ascii_lowercase, k=6))
#os.makedirs(rootdir + '/' + newdirname + '/' + randomstr )

print(platform.system())
rootdir = os.getcwd()

def dirmgmnt(url):
	print(url)
	newdirname = url.rsplit('/',1)[1]
	print(newdirname)
	if os.path.exists(newdirname):
		filesindir = os.listdir(newdirname)
		print("Directory " + newdirname + " already exists!" + "It has " + str(len(filesindir)) + " files")
		userc = input("Do you want to overwrite?\nY : overwrite existing files\nN : Creates new Directory\nQ : Quit\n")
		if userc.lower() in ['y','yes']:
			return(newdirname)
		elif userc.lower() in ['n','no']:
			dirnum = 1
			while(True):
				newnumdir = newdirname + '-' + str(dirnum)
				print(newnumdir)
				if not os.path.exists(newnumdir) :
					os.makedirs(newnumdir)
					return newnumdir
					break
				dirnum = dirnum + 1
		elif userc.lower() in ['q', 'quit']:
			print("Exiting")
		else:
			print("Fuck You!")
			dirmgmnt(url)
		sys.exit()
	else:
		os.makedirs(newdirname)
		return(newdirname)

temp_url = 'http://szcdn1.raagalahari.com/mar2017/hd/sony-charishta-swimming/sony-charishta-swimming1.jpg'
raw_range = '1 4 10 23'
given_range = raw_range.split()

currentdir = dirmgmnt(temp_url)
print('current working Directory is ' + currentdir)
