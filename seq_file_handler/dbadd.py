import requests
import imghdr
import os
import os.path
import sys
import sqlite3
import random
import string

conn = sqlite3.connect('raga.db')
c = conn.cursor()

rhash = 'hash' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

c.execute('''INSERT INTO ragalahari(name, s1, e1, s2, e2, hashv, ttime, tsize)
	VALUES(?,?,?,?,?,?,?,?)''', ('naga bhargavi',1,128,1000,1032,rhash,149,34292))

conn.commit()