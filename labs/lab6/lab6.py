"""
Name: Zachary Sika
lab6.py

Problem: Encodes a message given by the user created through a keyword given.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
def vigenere():
    win = GraphWin("Vigenere", 550, 400)
    message_code = Text(Point(100,50),("Message to code"))
    enter_keyword = Text(Point(100,100),("Enter Keyword"))
    box_var = Entry(Point(350,50),30)
    box_var2 = Entry(Point(325,100),20)
    click_close = Text(Point(245,350),("Click Anywhere to Close Window"))
    button = Text(Point(225,175),("Encode"))
    resulting_message_text = Text(Point(245,225),("Resulting Message"))
    button_shape = Rectangle(Point(175,200),Point(275,150))
    button.draw(win)
    button_shape.draw(win)
    enter_keyword.draw(win)
    message_code.draw(win)
    box_var.draw(win)
    box_var2.draw(win)
    win.getMouse()
    text_var = box_var.getText()
    text_var2 = box_var2.getText()
    text_var2.draw(win)
    click_close.draw(win)
    button.undraw()
    button_shape.undraw()
    resulting_message_text.draw(win)
    win.getMouse()
vigenere()