import requests
import imghdr
import os
import os.path
import sys
import sqlite3

conn = sqlite3.connect('raga.db')
c = conn.cursor()

raga = [('place holder',1,128,1000,1028,'hash3AH678D4',122,99999)]

actressdb = """
CREATE TABLE ragalahari (
	name text NOT NULL,
	s1 integer NOT NULL,
	e1 integer NOT NULL,
	s2 integer NOT NULL,
	e2 integer NOT NULL,
	hashv text PRIMARY KEY,
	ttime integer NOT NULL,
	tsize integer NOT NULL)"""

c.execute(actressdb)