#!/usr/bin/env python

a = input()
b = input()
c = input()

if a == b == c:
	print "equilateral"

elif a == b:
	print "isosceles"
elif b == c:
	print "isosceles"
elif a == c:
	print "isosceles"
else:
	print "neither"
