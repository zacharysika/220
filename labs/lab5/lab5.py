"""
Name: Zachary Sika
lab5.py

Problem: user creates graphic entries from input

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
def triangle():
    pass


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")
    for i in range(5):
        msg = "Enter color values between 0 - 255\nClick window to color shape"
        inst = Text(Point(win_width / 2, win_height - 20), msg)
        inst.draw(win)

        shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
        shape.draw(win)

        red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
        red_set = Entry(red_text_pt.clone(),50)
        red_text = Text(red_text_pt, "Red: ")
        red_text.setTextColor("red")

        green_text_pt = red_text_pt.clone()
        green_text_pt.move(0, 30)
        green_set = Entry(red_text_pt.clone(),50)
        green_text = Text(green_text_pt, "Green: ")
        green_text.setTextColor("green")

        blue_text_pt = red_text_pt.clone()
        blue_text_pt.move(0, 60)
        blue_set = Entry(red_text_pt.clone(),50)
        blue_text = Text(blue_text_pt, "Blue: ")
        blue_text.setTextColor("blue")

        # display rgb text
        red_text.draw(win)
        green_text.draw(win)
        blue_text.draw(win)
        win.getMouse()
        shape.setFill(color_rgb(red_set,green_set,blue_set))
    # Wait for another click to exit
    inst.undraw()
    exit_msg = "Click once more to exit"
    inst = Text(Point(win_width / 2, win_height - 20), exit_msg)
    inst.draw(win)
    win.getMouse()
    win.close()

def process_string():
    word_entry = input("Please enter a word")
    first_char = word_entry[0]
    last_char = word_entry[-1]
    first_last_char = first_char+last_char
    pos_2_5 = word_entry[2:5]
    first_three = word_entry[0:3]
    character_count = len(word_entry)
    print(first_char)
    print(last_char)
    print(pos_2_5)
    print(first_last_char)
    for i in range(10):
        print(first_three)
    for length in word_entry:
        print(length)
    print(character_count)
process-string()
def process_list():
    pt = Point(5,10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]



def another_series():
    terms = [2,4,6]
    series = eval(input("Please enter series of numbers"))
    continuation_series = (terms+terms) * series
    terms_sum = sum(continuation_series)
    print(terms_sum)

def target():
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")
    circle4 = Circle(Point(200,200),50)
    circle3 = Circle(Point(200,200),100)
    circle2 = Circle(Point(200,200),150)
    circle1 = Circle(Point(200,200),200)
    circle1.setFill("black")
    circle2.setFill("blue")
    circle3.setFill("red")
    circle4.setFill("yellow")
    circle1.draw(win)
    circle2.draw(win)
    circle3.draw(win)
    circle4.draw(win)
    win.getMouse()
    win.close()

