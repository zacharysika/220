"""
Name: Zachary Sika
hw8.py

Problem: Uses conditional arguments to return a true or false from user input

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math
def add_ten():
    nums = input("Please enter numbers")
    nums_list = nums.split()
    for index in range(len(nums_list)):
        nums_list[index] = int(nums_list[index]) + 10

def square_each():
    list_items = []
    number_amount = int(input("How many numbers are there?"))
    for i in range(number_amount):
        nums = input("Please enter number:")
        list_items.append(int(nums) ** 2)
    print(list_items)

def sum_list():
    list_items = []
    number_amount = int(input("How many numbers are there?"))
    for i in range(number_amount):
        numbers = int(input("Enter Number:"))
        list_items.append(numbers)
    print(sum(list_items))

def to_numbers(nums):
    pass


def sum_of_squares(nums):
    pass


def starter():
    wins = int(input("How many times has this player won?"))
    weight = int(input("How much does this player weigh?"))
    if (weight >= 150 and weight < 160 and wins <= 5):
        print("They are at the starter position")
        starter = True
    elif (weight>199 or wins>20):
        print("They are at the starter position")
        starter = True
    else:
        print("They are not at the starter position")
        starter = False
    print(starter)
def leap_year():
    year = int(input("Enter Year:"))
    if year % 4 != 0:
        print("not a leap year")
    elif year % 100 != 0:
        print("leap year")
    elif year % 400 != 0:
        print("not a leap year")
    else:
        print("leap year")
def circle_overlap(circle_one,circle_two,distance,radius_sum):
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)
    text_alert = Text(Point(5,5), "Click twice to draw circles")
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
    distance = math.sqrt((center.getX() - center2.getX()) ** 2 + (center.getY() - center2.getY()) ** 2)
    if (distance < radius_sum):
        return True
    else:
        return False
    win.getMouse()
    win.close()
def did_overlap(circle_one, circle_two,distance,radius_sum):


 #if __name__ == '__main__':
        ## add_ten()
        ## square_each()
        ## sum_list()
        ## to_numbers(nums)
        ## sum_of_squares(nums)
        ## starter()
        ## leap_year()
        ## circle_overlap(circle_one, circle_two)
