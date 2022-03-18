"""
Name: Zachary Sika
lab8.py

Problem: A graphics program that simulates bumper cars

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

import time
from random import randint
from graphics import *
import math
def did_collide():
        colors= ["red","green","yellow","blue","orange","black","white","purple",]
        run = True
        random_x = randint(1, 9)
        random_y = randint(1, 9)
        random_x2 = randint(1, 9)
        random_y2 = randint(1, 9)
        win = GraphWin("Circle",700,700)
        circle_ball = Circle(Point(350, 300), 100)
        circle_ball2 = Circle(Point(250,50),100)
        circle_ball_radius = circle_ball.getRadius()
        circle_ball2_radius = circle_ball2.getRadius()
        circle_ball.setFill("blue")
        circle_ball2.setFill("green")
        circle_ball.draw(win)
        circle_ball2.draw(win)

        yFloor = circle_ball_radius
        yCeiling = win.getHeight() - circle_ball_radius
        xFloor = circle_ball_radius
        xCeiling = win.getWidth() - circle_ball_radius

        while (run ==True):
                distance = math.sqrt((random_x - random_x2) ** 2 + (random_y2 - random_y) ** 2)
                random_selection = randint(0,7)
                color_selection = colors[random_selection]
                time.sleep(.01)
                circle_ball.move(random_x,random_y)
                circle_ball2.move(random_x2,random_y2)
                if circle_ball.getCenter().getY() <= yFloor or circle_ball.getCenter().getY() >= yCeiling:
                        random_y = -random_y
                        circle_ball.setFill(color_selection)
                elif circle_ball.getCenter().getX() <= xFloor or circle_ball.getCenter().getX() >= xCeiling:
                        random_x = -random_x
                        circle_ball.setFill(color_selection)
                elif circle_ball2.getCenter().getY() <= yFloor or circle_ball2.getCenter().getY() >= yCeiling:
                        random_y2 = -random_y2
                        circle_ball2.setFill(color_selection)
                elif circle_ball2.getCenter().getX() <= xFloor or circle_ball2.getCenter().getX() >= xCeiling:
                        random_x2 = -random_x2
                        circle_ball2.setFill(color_selection)
                elif (distance < (circle_ball_radius + circle_ball2_radius)):
                        print("true")
                        random_x2 = -random_x2
                        random_x = -random_x
                        random_y = -random_y
                        random_y2 = -random_y2

did_collide()
