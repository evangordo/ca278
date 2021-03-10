#!/usr/bin/env python

class Employee:

    def __init__(self, name, job_desc, salary):
        self.name = name
        self.job_desc = job_desc
        self.salary = salary
    
    def net_salary(self):
        return self.salary*0.8


if __name__ == '__main__':      
    name = raw_input("Enter the employee name:\n")
    job = raw_input("Enter the employee job description:\n")
    sal = input("Enter the employee salary:\n")

    p = Employee(name, job, sal)
    print "Net Salary:x", p.net_salary()
