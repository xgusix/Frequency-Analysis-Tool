#!/usr/bin/python
########TO DO#########
# Improve output
# Add more information:
#	- count all pairs and trios (not only words)
# Add parameters
######################
import sys
import operator
sys.path.insert(0,'fatlib')
import fatlib

try:
	fs = open(sys.argv[1],'r')
	data = fs.read()
	fs.close()
except:
	print "Error reading the file "+argv[1]
	exit(2)

chars = fatlib.count_chars(data)
chars = sorted(chars.iteritems(), key=lambda t: t[1])
pair = fatlib.countNchars_words(data,2)
pair = sorted(pair.iteritems(), key=lambda t: t[1])
trio = fatlib.countNchars_words(data,3)
trio = sorted(trio.iteritems(), key=lambda t: t[1])


for char in reversed(chars): print char
for p in reversed(pair): print p
for t in reversed(trio): print t