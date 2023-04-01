import os
from PIL import Image
import PIL
import binascii
from array import array

img = Image.new('RGB', (28, 28))
img.save('pil_num.png')
f = open("pil_num.png", "rb")
print(binascii.hexlify(f.read()))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
raw_data = "89504e470d0a1a0a0000000d494844520000001c0000001c0802000000fd6f48c30000001949444154789cedc13101000000c2a0f54f6d076fa00000780d094c0001f597c2980000000049454e44ae426082"
enc_data = bytearray(raw_data,'utf8')

file_o = open('pil_num.png','rb')
data_o = file_o.read()
print('~~~')
print(data_o)
print('~~~')
size_o = file_o.tell();
print(size_o)
file_m = open('pil_mod.png','wb')
file_m.write(data_o)

img_create = Image.new('L',(7000,6720))
pixels = img_create.load()

mnistF = open('digit_raw.bin','rb')
mnistD = mnistF.read()
mnistS = int.from_bytes(b'\xFF','big')
#print(mnistS)
x = 0
y = 0
z = 16

while x < 7000 :
	while y < 6720:
		pixel_bin = mnistD[z:z+1]
		pixel = int.from_bytes(pixel_bin,'big')
		print('index : ' + str(x) + ' : ' + str(y) + ' : ' + str(z) + ' : ' + str(pixel))
		z = z+1
		pixels[x,y] = pixel
		y = y+1
	y = 0
	x = x+1

img_create.save('test.bmp')