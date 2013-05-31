#!/usr/bin/python

import theparser
import sys

dickey = theparser.dividerDict('key.txt',divider='->')

cleartext = open(sys.argv[1],'r').read()
cryptext = ''

for c in cleartext:
	try:
		if c != c.lower():
			cryptext += dickey[c.lower()].upper()
		else:
			cryptext += dickey[c]
	except:
		cryptext += c

print cryptext



