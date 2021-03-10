#!/usr/bin/ env python

import sys
file = sys.argv[1]

with open(filename, 'r'). as file:
	s = file.readlines()

surname = raw_input("Pleas enter a surname:")

i = 0
surname = []
while i < len(s):
	token = s[i].strip("\n")
	token = token.split()
	for surname.lower() == token[1].lower():
		surnmelist.append(token[0])
	i = i + 1

if len(surnamelist) > 0:
	print surnamelist
else:
   print "No-one has that surname"