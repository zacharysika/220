"""
Name: Zachary Sika
hw4.py

Problem: Creates a interactable graphical interface from python.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *


def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), Point(50,50))
    shape.setWidth(50)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        clone = shape.clone()
        clone.draw(win)
        shape.move(change_x, change_y)
    message = Text(Point(175,125), "Click again to close")
    message.draw(win)
    win.getMouse()
    win.close()

def rectangle():
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)
    point1 = click.getX()
    point2 = click.getY()
    shape = Rectangle(Point(point1), Point(point2))
    shape.draw(win)
    message = Text(Point(175,125), "Click again to close")
    message.draw(win)
    win.getMouse()
    win.close()
rectangle()

def circle():



def pi2():
    pass


if __name__ == '__main__':
    pass
