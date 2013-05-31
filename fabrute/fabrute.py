#!/usr/bin/python
import string
import sys


def count_chars(data):
	dic = {}
	for char in data:
		if char in dic.keys():
			dic[char] += 1
		else:
			dic[char] = 1
	return dic


EN_FREQ = ' etaoinshrdlcumwfgypbvkjxqz'
dataaux = open(sys.argv[1]).read()
data =dataaux.replace('\n','')

chars = count_chars(data.lower())
foo=[]
for i in reversed(sorted(chars.iteritems(), key=lambda t: t[1])):
	if i[0] in EN_FREQ:
		foo.append(i)
print foo

dic = {}

for i in range(len(EN_FREQ)):
	try:
		dic[foo[i][0]] = EN_FREQ[i]
	except:
		dic[foo[i][0]] = dic[foo[i][0]]

print dic 
dec = ''
for c in data:
	try:
		dec += dic[c.lower()]
	except:
		dec += c
print dec
