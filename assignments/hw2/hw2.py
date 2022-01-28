"""
Name: Zachary Sika
hw2.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    upper_bound = eval(input("What is the upper bound?"))
    lower_bound = eval(input("What is the lower bound?"))



def multiplication_table():
    pass

def triangle_area():
    a_variable = eval(input("Enter side a length"))
    b_variable = eval(input("Enter side b length"))
    c_variable = eval(input("Enter side c length"))
    s_variable = (a_variable + b_variable + c_variable)/2
    area = math.sqrt(s_variable*(s_variable-a_variable)*(s_variable-b_variable)*(s_variable-c_variable))
    print (area)


def sum_squares():
    sum = 1
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    for i in range(lower_range, upper_range):
        sum = sum * i
    print(sum)

def power():
    sum = 1
    base = eval(input("Enter base:"))
    exponent = eval(input("Enter exponent"))
    for i in range (exponent):
        sum = sum * base
    print(base, "^", exponent, "=", sum)

if __name__ == '__main__':
    pass
