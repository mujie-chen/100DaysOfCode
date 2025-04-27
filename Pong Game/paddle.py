# a responsive paddle class with width of 20, height 100, with x_pos at 350/-350 (fixed), y_pos at 0 (starting)

from turtle import Turtle

class Paddle(Turtle):
	def __init__(self, position): # not (x_cor, y_cor) as a tuple, simply a variable name
		super().__init__()
		self.shape("square") # default 20 x 20
		self.color("white")
		self.shapesize(stretch_wid=5, stretch_len=1) # becomes 100 x 20
		self.penup()
		self.goto(position) # can be initialised as left and right paddle using the same class

	def go_up(self): # methods always have the first argument as self
		new_y = self.ycor() + 20
		self.goto(self.xcor(), new_y)

	def go_down(self):
		new_y = self.ycor() - 20
		self.goto(self.xcor(), new_y)
