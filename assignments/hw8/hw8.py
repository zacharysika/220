"""
Name: Zachary Sika
hw8.py

Problem: Uses conditional arguments to return a true or false from user input

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math
def add_ten(nums):
    nums = [50,54,-1,53,-70]
    for index in range(len(nums)):
        nums[index] = int(nums[index]) + 10

def square_each(nums):
    for index in range(len(nums)):
        nums[index] = int(nums[index]) ** 2

def sum_list(nums):
    return sum(nums)

def to_numbers(nums):
    for i in nums:
        "".join(str(i))
    num_list = int(i)
def sum_of_squares(nums):
    pass


def starter(weight,wins):
    if (weight >= 150 and weight < 160 and wins >= 5):
        return True
    elif (weight > 199 or wins > 20):
        return True
    else:
        return False
def leap_year(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
    text_alert = Text(Point(5, 5), "Click twice to draw circles")
    text_alert.draw(win)
    center = win.getMouse()
    circumference_point = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    radius2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, radius2)
    circle_two.setFill("green")
    circle_two.draw(win)

def did_overlap(circle_one, circle_two):
    distance = math.sqrt((circle_one.getCenter().getX() - circle_two.getCenter().getX()) ** 2 + (circle_one.getCenter().getY() - circle_two.getCenter().getY()) ** 2)
    radius_sum = circle_one.getRadius() + circle_two.getRadius()
    if (distance < radius_sum):
        return False
    else:
        return True
if __name__ == '__main__':
    pass