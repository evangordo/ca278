#!/usr/bin/env python

s = raw_input("Will you have a cup of tea, Father?")

while s != "yes" and s != "YES":
  s = raw_input("Ah go on?")

print "Here you are."
