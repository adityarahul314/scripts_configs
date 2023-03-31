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

retid = 'hash58E1BD81'

c.execute('''SELECT name, s1, e1, s2, e2, hashv, ttime, tsize FROM place_holder WHERE hashv=?''', (retid,))
ractress = c.fetchone()
print(ractress[0] + " " + ractress[5])