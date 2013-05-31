#!/usr/bin/python

import sys
sys.path.insert(0,'fatlib')
import theparser

print """ ______        _______                  _       _
|  ____/\     |__   __|                | |     | |
| |__ /  \       | |_ __ __ _ _ __  ___| | __ _| |_ ___  _ __
|  __/ /\ \      | | '__/ _` | '_ \/ __| |/ _` | __/ _ \| '__|
| | / ____ \     | | | | (_| | | | \__ \ | (_| | || (_) | |
|_|/_/    \_\    |_|_|  \__,_|_| |_|___/_|\__,_|\__\___/|_|
--------------------------------------- By xGUSIx @ PHT-------"""

def usage():
        print 'USAGE: ./'+sys.argv[0]+' <file encrypted> <dictionary>'
        exit(0)


if len(sys.argv)<3:
        usage()

try:
        fd= open(sys.argv[1],'r')
        encrypted= fd.read()
#        print encrypted
        fd.close()
except:
        print 'Error: opening file'
        sys.exit(2)

dic = theparser.dividerDict(sys.argv[2],'->')
#print dic
decrypted=''
for c in encrypted:
        try:
                decrypted += dic[c]
        except:
                decrypted += c
#print decrypted
try:
        fd= open(sys.argv[1]+'decrypted','w')
        fd.write(decrypted)
except:
        print 'Error: writing file'
        sys.exit(2)
