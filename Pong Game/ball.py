# ball object with width 20, height 20, x_pos, y_post at 0, 0 initially

from turtle import Turtle

class Ball(Turtle):
	def __init__(self):
		super().__init__()
		self.shape("circle") # historically it was a square
		self.color("white")
		self.penup()
		# no need to go to center
		self.x_move = 10
		self.y_move = 10
		self.move_speed = 0.1

	def move(self):
		new_x = self.xcor() + self.x_move
		new_y = self.ycor() + self.y_move
		self.goto(new_x, new_y)

	def bounce_y(self):
		self.y_move *= -1 # define x and y increments in init and flip y using syntatic sugar during a bounce
		# upon next move() + update() in the while loop, y_direction will be flipped

	def bounce_x(self):
		self.x_move *= -1 # upon next move() + update() in the while loop, x-direction will be flipped

	def reset_position(self):
		self.goto(0, 0)
		self.bounce_x()
