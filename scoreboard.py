from turtle import Turtle

# constants
ALIGNMENT = "center"
FONT = ("courier", 20, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(x=0, y=270)
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font= FONT)
        self.hideturtle()

    def increase_score(self):
        self.score +=1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

