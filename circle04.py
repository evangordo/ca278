#/usr/bin/env python

from math import pi

class Circle:
  '''a class to represent a circle'''
  def __init__(self, radius):
	self.radius  = radius

  def get_area(self):
	'''get_area()  returns the area of the cirlce'''
	return pi * self.radius**2

  def get_circumference(self):
	'''get_circumference() returns the circumference of the circle'''
	return 2 * pi * self.radius

if __name__ == '__main__':
  radius = input("Enter the radius: ")
  c = Circle(radius)
  print "Area:", c.get_area()
  print "circumference", c.get_circumference()
