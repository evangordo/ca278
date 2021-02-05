#!/usr/bin/env python

def get_price(age):
	price = 10
	if age <= 16:
		price = 5
	elif age > 60:
		price = 7
	return price


def weird_case(some_str):
  string_out = ""
  words = some_str.split()
  position = 0
  for word in words:
    for character in word:
      if position % 2 == 0:
        string_out += character.upper()
      else:
        string_out += character.lower()
      position += 1
    string_out += " "
  return string_out.strip()

if __name__ == '__main__':
	print weird_case('Totally')

def every_second(l1,l2):
	
