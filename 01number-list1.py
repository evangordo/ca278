#!/usr/bin/env python

numbers = []

n = input("Please enter a number (-1 to stop):")

while n != -1:
	numbers.append(n)
	n = input("Please enter a number (-1 to stop):")

print numbers
