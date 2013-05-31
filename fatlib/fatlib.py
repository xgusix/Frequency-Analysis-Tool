#!/usr/bin/python
########TO DO#########
# Improve output
# Add more information:
#	- count all pairs and trios (not only words)
# Add parameters
######################
import re

def count_chars(data):
	dic = {}
	for char in data:
		if char in dic.keys():
			dic[char] += 1
		else:
			dic[char] = 1
	return dic

def countNchars_words(data,n):
	reg = r"((?<=\s)[^\s]{" +str(n)+"}(?=\Z|\s)|(?<=^)[^\s]{"+str(n)+"}(?=\Z|\s))"
	regex = re.compile(reg)
	groups_list = regex.findall(data)
	dic= {}
	for word in groups_list:
		if word in dic.keys():
			dic[word] += 1
		else:
			dic[word] = 1
	return dic