#!/usr/bin/env python

scores = raw_input("Please enter a list of scores:").split()

category = {
  "Wins" : 0,
  "Draws" : 0,
  "Losses" : 0,
}

for score in scores:
  if score == "3":
    category["Wins"] = category["Wins"] + 1
  elif score == "1":
    category["Draws"] = category["Draws"] + 1
  else:
    category["Losses"] = category["Losses"] + 1

print "Draws:", category["Draws"]
print "Losses:", category["Losses"]
print "Wins:", category["Wins"]
