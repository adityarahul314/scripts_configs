import os

rootdir = os.getcwd()
zipfile = rootdir + '/nfiles.jpg'
sizedata = rootdir + '/metadata.dat'

zfile = open(zipfile,'rb')
sdata = open(sizedata,'r')

sdatalist = sdata.read().split('\n')

for x in range(0,len(sdatalist)-1):
	print(sdatalist[x])
	print(zfile.tell())
	currentimgdata = zfile.read(int(sdatalist[x]))
	currentimgfile = open('img' + str(x) + '.jpg','wb')
	currentimgfile.write(currentimgdata)
	currentimgfile.close()
