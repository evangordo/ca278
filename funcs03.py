#!/usr/bin/env python

import time

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

def every_second(l1,l2):
  l3 = []
  i = 0
  while i < len(l1):
    if i % 2 == 1:
      l3.append(l1[i])
    i += 1
  i = 0
  while i < len(l2):
    if i % 2 == 1:
      l3.append(l2[i])
    i += 1
  return l3

def is_neg(num):
  if num < 0:
    return True
  else:
    return False

def remove_neg(lst):
  negative = []
  for number in lst:
    if number < 0:
      negative.append(number)
  for num in negative:
    lst.remove(num)

def countdown(num):
  while num > 0:
    print num
    num -= 1
    time.sleep(.1)
  print "LIFT OFF!"

def search(str,letter):
  if letter in str:
    return True
  else:
    return False

def index(str,letter):
  return str.find(letter)

def previous_two(n):
  i = 1
  sequence = [0,1]
  while i < n:
    sequence.append(sequence[i] + sequence[i - 1])
    i += 1
  return sequence[n]
