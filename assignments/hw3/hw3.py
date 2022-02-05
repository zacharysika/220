"""
Name: Zachary Sika
hw3.py

Problem: Creates average for tips, grades, and give the square root of a number using
newton's method.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def average():
    grade_total = 0
    grades = eval(input("how many grades will you enter?"))
    for i in range(grades):
        grade_total = eval(input("Enter grade")) + grade_total
    average = grade_total / grades
    print(average)


def tip_jar():
    passing_amount = 5
    tips = 0
    for i in range(passing_amount):
        tips = eval(input("how much would you like to donate?")) + tips
    print(tips)

def newton():
    approx = eval(input("What number do you want to square root?"))
    x = eval(input("How many times should we improve the approximation?"))
    approx_total = (approx + (x/approx)) / 2
    print(approx_total)



def sequence():
    pass


def pi():
    pass


if __name__ == '__main__':
    pass
