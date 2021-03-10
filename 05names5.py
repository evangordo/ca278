#!/usr/bin/env python

class Person:
    ''' a class to represent a person'''
    def __init__(self, n, a):
    	self.name = name
    	self.age = age
        
    def get_surname(self):
        return self.name.split()[1]

    def get_firstname(self):
        return self.name.split()[0]

    def __str__(self):
    	firstname = self.get_firstname()
    	surname = self.get_surname()
        return surname + ", " + firstname + " (" + self.age + ")"

if __name__ == '__main__':
	name = raw_input("What is your name?")
	age = raw_input("How old are you?")
	person = Person(name, age)
	print "Hello", person.get_firstname()
	print "Here are your details:\n", person.__str__()

