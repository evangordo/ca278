#!/usr/bin/env python

numbers = []
count = {}

n = input("Please enter a number (-1 to stop):")

while n != -1:
	if n not in numbers:
		numbers.append(n)
		count[n] = 1
	else:
		count[n] = count[n] + 1
	n = input("Please enter a number (-1 to stop):")

print numbers
for number in count: 
	print number, "occured", count[number], "times"

