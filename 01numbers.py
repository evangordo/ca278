#!/usr/bin/env python

n = input("Enter a number:")

total = 0
print "\n" + str(n)

while n > 0:
	total += n
	n -= 1
	print n

print "\n" + str(total)
