"""
Name: Zachary Sika
hw2.py

Problem: Solves problems of arithmetic through python from user input.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math


def sum_of_threes():
    pass
def multiplication_table():
    num = 1
    for i in range(1,11):
        sum = (num*i)+sum
    print(sum)

def triangle_area():
    a_variable = eval(input("Enter side a length"))
    b_variable = eval(input("Enter side b length"))
    c_variable = eval(input("Enter side c length"))
    s_variable = (a_variable + b_variable + c_variable)/2
    area = math.sqrt(s_variable*(s_variable-a_variable)*
           (s_variable-b_variable)*(s_variable-c_variable))
    print (area)


def sum_squares():
    sum = 0
    lower_range = eval(input("Enter lower range: "))
    upper_range = eval(input("Enter upper range: "))
    for i in range(lower_range,upper_range + 1):
        sum= (i*i) + sum
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
