# setting up the scoreboard class, which is also a turtle

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal") # font as a tuple

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT) # using global constants here

    def increase_score(self):
        self.score += 1
        self.clear() # so it does not overlap
        self.update_scoreboard() # rewrite the new score; abstracted out as its the same as inititialisation

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        