import os
from PIL import Image, ImageOps

img_create = Image.new('L',(7000,6720))
pixels = img_create.load()

mnistF = open('digit_raw.bin','rb')
mnistD = mnistF.read()
mnistS = int.from_bytes(b'\xFF','big')

trackIndex = 0

def crapsingle(a,b) :
	x = a*28
	y = b*28
	global trackIndex

	while x < (a+1)*28 :
		while y < (b+1)*28:
			pixel_bin = mnistD[trackIndex:trackIndex+1]
			pixel = int.from_bytes(pixel_bin,'big')
			#print('index : ' + str(x) + ' : ' + str(y) + ' : ' + str(z) + ' : ' + str(pixel))
			trackIndex = trackIndex + 1
			pixels[x,y] = pixel
			y = y+1
		y = b*28
		x = x+1
	#print('fuck you : ' + str(a) + " : " + str(b))

def megacrap() :
	m = 0
	n = 0
	while m < 250 :
		while n < 240 :
			crapsingle(m,n)
			n = n + 1
		n = 0
		m = m + 1

megacrap()
img_create = ImageOps.mirror(img_create)
img_create = img_create.rotate(90)
img_create.save('test.bmp')