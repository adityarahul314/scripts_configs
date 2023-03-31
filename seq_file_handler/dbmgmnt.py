import os
import hashlib

def takeurl():
	while True:
		raw_url = input("Enter url : ")
		url_ext = raw_url[len(raw_url)-4:len(raw_url)]
		if (url_ext=='.jpg' or url_ext=='.png'):
			#print('valid url')
			base_url = raw_url[0:len(raw_url)-int(takedeviant())]
			break
		else:
			print('url not found. Please try again')
			base_url = ''
	return base_url

def takedeviant():
	while True:
		digit_rem = input("Enter deviant : (deafult is 1) : ")
		try:
			if digit_rem=='':
				digit_rem = '1'
				print('taking default value 1')
				digit_rem = str(int(digit_rem) + 4)
				break
			elif int(digit_rem) > 4 :
				print('deviant too large. Try again')
			elif int(digit_rem) < 1 :
				print('deviant must be > 0')
			else:
				#print('deviant is ' + str(digit_rem))
				digit_rem = str(int(digit_rem) + 4)
				break
		except:
			print("Invalid input")
	return digit_rem

def takerange():
	while True:
		raw_range = input('Input range(s) : ')
		given_range = raw_range.split()

		if len(given_range)%2==0 and len(given_range)>0:
			if numtuple(given_range):
				break
			else:
				print("Invalid input")
		elif len(given_range)==1:
			break
		else:
			print('Invalid input')
	return given_range

def numtuple(given_list):
	index_track = 0
	numbool = True
	while index_track < len(given_list):
		if not given_list[index_track].isdigit():
			numbool = False
		index_track = index_track + 1
	return numbool

def sessionid(bu,gr):#bu:baseurl,gr:giverange
	session_data = (bu+''.join(gr)).encode('utf-8')
	sessionhash = hashlib.md5(session_data)
	session_digest = sessionhash.hexdigest()
	return session_digest
	#print("Session Id is : " + session_digest)

keyurl = takeurl()
ranges = takerange()
SId = sessionid(keyurl,ranges)
#os.system('cls')
print(keyurl)
print(ranges)
print(SId)