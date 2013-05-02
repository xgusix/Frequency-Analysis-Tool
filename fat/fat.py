#!/usr/bin/python
########TO DO#########
# Improve output
# Add more information:
#	- count all pairs and trios (not only words)
# Add parameters
######################
import sys
import re
import operator

def count_chars(data):
	dic = {}
	for char in data:
		if char in dic.keys():
			dic[char] += 1
		else:
			dic[char] = 1
	return dic

def countNchars_words(data,n):
	reg = r"(?<=\s)[^\s]{"+str(n)+"}(?=\Z|\s)"
	regex = re.compile(reg)
	groups_list = regex.findall(data)
	dic= {}
	for word in groups_list:
		if word in dic.keys():
			dic[word] += 1
		else:
			dic[word] = 1
	return dic



try:
	fs = open(sys.argv[1],'r')
	data = fs.read()
	fs.close()
except:
	print "Error reading the file "+argv[1]
	exit(2)

chars = count_chars(data)
chars = sorted(chars.iteritems(), key=lambda t: t[1])
pair = countNchars_words(data,2)
pair = sorted(pair.iteritems(), key=lambda t: t[1])
trio = countNchars_words(data,3)
trio = sorted(trio.iteritems(), key=lambda t: t[1])


for char in reversed(chars): print char
for p in reversed(pair): print p
for t in reversed(trio): print t