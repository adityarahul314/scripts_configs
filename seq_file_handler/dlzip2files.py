import requests
import imghdr
import os
import os.path
import sys
from progress.bar import IncrementalBar

#Current directory and New Directory
rootdir = os.getcwd()
dldir = rootdir + '/ragadl/'
file1 = dldir + '16.jpg'
file2 = dldir + '20.jpg'
img1 = open(file1,'rb')
img2 = open(file2,'rb')
imgdata1 = img1.read()
imgdata2 = img2.read()
img1size = img1.tell()
img2size = img2.tell()
imgcsld = open('ragazip.jpg','wb')
imgcsld.write(imgdata1)
imgcsld.write(imgdata2)
imgcsld.close()

imgcsld = open('ragazip.jpg','rb')
#imgcsld.seek(0,0)
temp = imgcsld.read(img1size)
imgf1 = open('newimg1.jpg','wb')
imgf1.write(temp)
imgf1.close()

#imgcsld.seek(img1size,0)
temp = imgcsld.read(img2size)
imgf2 = open('newimg2.jpg','wb')
imgf2.write(temp)
imgf2.close()
