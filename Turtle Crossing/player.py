# turtle which will be controlled to cross the screen

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.go_to_start()
        
    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(0, new_y)

        # or self.forward(MOVE_FORWARD)

    def go_to_start(self):
        self.goto(STARTING_POSITION)
