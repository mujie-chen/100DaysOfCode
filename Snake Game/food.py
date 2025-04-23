# setting up the food class

from turtle import Turtle
import random

class Food(Turtle): # food to inherit turtle initialisation
    def __init__(self):
        super().__init__()
        self.shape("circle") # a class Food, with food properties; rather than a class Turtle assigned to a food name
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self): # factor out the varying attributes every time food is eaten
        random_x = random.randint(-200, 200)
        random_y = random.randint(-200, 200)
        self.goto(random_x, random_y)
