#!/usr/bin/env python

import sys
filename = sys.argv[1]
with open(filename, 'r') as file:
   names = file.readlines()
   for name in names:
   	print name.split()[0]
