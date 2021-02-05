#!/usr/bin/env python

age = input('Please enter your age:')

basic_charge = 0.75

if age < 5:
  print "You go free!"
elif age >= 65:
  print "You go free!"
elif 5 <= age <= 16:
  print "Your fare is: " + str(basic_charge) + " euro."
elif 17 <= age <= 20:
  print "Your fare is: " + str(basic_charge + 0.50) + " euro."
else:
  print "Your fare is: " + str(basic_charge + 0.75) + " euro."
