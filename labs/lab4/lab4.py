"""
Zachary Sika
lab4.py
Valentine's Day greeting card program
I have created this on my own
"""
from graphics import *

def greeting_card():
    win = GraphWin("Happy Valentine's Day", 500,500)
    win.setBackground("pink")
    message = Text(Point(230,125), "Happy Valentines Day!")
    message.setFace('helvetica')
    message.setSize(18)
    message.setTextColor('red')
    arrow = Line(Point(250,250), Point(250,250))
    arrow.setArrow("last")
    polygon = Polygon(Point(152, 215), Point(235,375), Point(323,215))
    circle = Circle(Point(200,215), 46)
    circle2 = Circle(Point(275,215), 46)
    circle.setFill('red')
    circle2.setFill('red')
    polygon.setFill('red')
    circle.draw(win)
    circle2.draw(win)
    polygon.draw(win)
    message.draw(win)
    arrow.draw(win)
    time.sleep(1)
    win.getMouse()



greeting_card()
