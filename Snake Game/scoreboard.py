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
        with open("data.txt") as data:
            self.high_score = int(data.read()) # add new attribute to track high score, read from save file
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear() # clear() moved from increase_score() here; prevent duplicate in reset()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT) # using global constants here

    def increase_score(self):
        self.score += 1
        self.clear() # so it does not overlap
        self.update_scoreboard() # rewrite the new score; abstracted out as its the same as inititialisation

    # def game_over(self):
    #    self.goto(0, 0)
    #    self.write("GAME OVER", align=ALIGNMENT, font=FONT)
     
    def reset(self):
        if self.score > self.high_score: # update to all time high_score
            self.high_score = self.score
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}") # converts integer to string, writes to original file
        self.score = 0 # reset game's score to zero
        self.update_scoreboard()
        