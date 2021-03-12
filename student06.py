#!/usr/bin/env python

class Student:
	''' a class to represent a student'''
	Id = 0
	def __init__(self, name, exam, ca):
		self.name = name
		self.exam = exam_score
		self.ca = ca_mark
		Student.Id += 1
		self.Id = Student.Id
		

	def get_average(self):
	  return float(self.exam + self.ca)/2

	def __str__(self):
		return "Id: " + str(self.Id) + ", Name: " + self.name + ", Average: " + str(self.get_average())


if __name__ == '__main__':
	with open("students.txt", "r") as f:
		for student in f:
			student_deets = student.split(",")
			name = student_deets[0]
			exam_score = int(student_deets[1])
			ca_mark = int(student_deets[2])
			student = Student(name, exam_score, ca_mark)
			print student.__str__()
