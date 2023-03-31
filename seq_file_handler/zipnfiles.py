import os

rootdir = os.getcwd()
dldir = rootdir + '/ragadl'
print(dldir)
imglist = os.listdir(dldir)

nzip = open('nfiles.jpg','wb')
sizedata = open('metadata.dat','w')

for x in range(0,len(imglist)):
	print(imglist[x])
	imgpath = dldir + imglist[x]
	imgfile = open(imgpath,'rb')
	imgdata = imgfile.read()
	imgsize = imgfile.tell()
	print(imgsize)
	nzip.write(imgdata)
	sizedata.write(str(imgsize) + '\n')

nzip.close()
sizedata.close()