#!/usr/bin/env python2.7
# coding=utf-8


class Employee(object):
    # Common base class for all employees
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print 'Total Employee %d' % Employee.emp_count

    def display_employee(self):
        print 'Name: ', self.name
        print 'Salary: ', self.salary


if __name__ == '__main__':
    print 'This would create first object of Employee class'
    emp1 = Employee('Zara', 2000)
    print 'This would create second object of Employee class'
    emp2 = Employee('Manni', 5000)
    emp1.display_employee()
    emp1.display_employee()
    print 'Total Employee %d' % Employee.emp_count
